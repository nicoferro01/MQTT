import MQTT
import Telegram
import threading

temperaturaIst = 0
temperatura1mn = 0
temperatura10mn = 0
temperatura1hr = 0
altitudineIst = 0
altitudine1mn = 0
altitudine10mn = 0
altitudine1hr = 0
pressioneIst = 0
pressione1mn = 0
pressione10mn = 0
pressione1hr = 0
luceIst = 0
luce1mn = 0
luce10mn = 0
luce1hr = 0

def main():

    threadMqtt = threading.Thread(target = MQTT.mqttStart)
    threadTelegram = threading.Thread(target = Telegram.start)
    threadMqtt.start()
    threadTelegram.start()
if __name__ == "__main__":
    main()
