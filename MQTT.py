import paho.mqtt.client as mqtt
import time
import master

i=0

def on_connect(client, userdata, flags, rc):
	print('Connessione al server Calvino...: {}'.format(mqtt.connack_string(rc)))
	client.subscribe('/#', qos = 0)

def on_subscribe(client, userdata, mid, granted_qos):
	print('Avviato con QoS: {}'.format(granted_qos[0]))

def on_message(client, userdata, msg):
    global i
    if msg.topic == "/calvino-05/temperatura":
        master.temperaturaIst=float(msg.payload.decode())
        if i%20==0:
            master.temperatura1mn = master.temperaturaIst
        if i%200==0:
            master.temperatura10mn = master.temperaturaIst
        if i%1200==0:
            master.temperatura1hr = master.temperaturaIst
    elif msg.topic == "/calvino-05/altitudine":
        master.altitudineIst=(float(msg.payload.decode()))
        if i % 20 == 0:
            master.altitudine1mn = master.altitudineIst
        if i % 200 == 0:
            master.altitudine10mn = master.altitudineIst
        if i % 1200 == 0:
            master.altitudine1hr = master.altitudineIst
    elif msg.topic == "/calvino-05/pressione":
        master.pressioneIst = (float(msg.payload.decode()))
        if i % 20 == 0:
            master.pressione1mn = master.pressioneIst
        if i % 200 == 0:
            master.pressione10mn = master.pressioneIst
        if i % 1200 == 0:
            master.pressione1hr = master.pressioneIst
    elif msg.topic == "/calvino-05/luce":
        master.luceIst = (float(msg.payload.decode()))
        if i % 20 == 0:
            master.luce1mn = master.luceIst
        if i % 200 == 0:
            master.luce10mn = master.luceIst
        if i % 1200 == 0:
            master.luce1hr = master.luceIst
        i+=1
        print(i)

def mqttStart():
	client = mqtt.Client(protocol = mqtt.MQTTv311)
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe
	client.on_message = on_message
	client.username_pw_set("calvino00","0123456789")

	client.connect(host = 'broker.shiftr.io', port = 1883, keepalive = 60)

	try:
		client.loop_forever()
	except KeyboardInterrupt:
		print()