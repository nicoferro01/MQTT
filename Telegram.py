import pzgram
import master
import MQTT


def inizio(chat, sender):
    chat.send("Ciao " + sender.first_name + ",\nsono il bot di Federico Pavesi e Nicolo' Ferrari.\nMi occupo di presentarvi dati raccolti nelle scuole Calvino di Modena.\n\nI dati riguardano:\n-Temperatura\n-Pressione\n-Altitudine\n-Luce\n\n\nDigita /bottoni per visualizzare i bottoni")

button = pzgram.create_button("instantanea", "instantanea")
button2 = pzgram.create_button("1 minuto", "Unminuto")
button3 = pzgram.create_button("10 minuti", "Dieciminuti")
button4 = pzgram.create_button("1 ora", "Unora")
Bottoni = [[button, button2],[button3, button4]]
pool_keyboard = pzgram.create_inline(Bottoni)

def bottoni(chat):
    chat.send("Scegli un bottone", reply_markup=pool_keyboard)

def instantanea(chat):
    chat.send("Misure raccolte istantaneamente: ")
    chat.send("Pressione: " + str(master.pressioneIst))
    chat.send("Temperatura: " + str(master.temperaturaIst))
    chat.send("Luce: " + str(master.luceIst))
    chat.send("Altitudine: " + str(master.altitudineIst))
    bottoni(chat)

def Unminuto(chat):
    chat.send("Misure raccolte in un minuto: ")
    chat.send("Pressione: " + str(master.pressione1mn))
    chat.send("Temperatura: " + str(master.temperatura1mn))
    chat.send("Luce: " + str(master.luce1mn))
    chat.send("Altitudine: " + str(master.altitudine1mn))
    bottoni(chat)

def Dieciminuti(chat):
    chat.send("Misure raccolte in 10 minuti: ")
    chat.send("Pressione: " + str(master.pressione10mn))
    chat.send("Temperatura: " + str(master.temperatura10mn))
    chat.send("Luce: " + str(master.luce10mn))
    chat.send("Altitudine: " + str(master.altitudine10mn))
    bottoni(chat)

def Unora(chat):
    chat.send("Misure raccolte in un'ora: ")
    chat.send("Pressione: " + str(master.pressione1hr))
    chat.send("Temperatura: " + str(master.temperatura1hr))
    chat.send("Luce: " + str(master.luce1hr))
    chat.send("Altitudine: " + str(master.altitudine1hr))
    bottoni(chat)

def start():
    bot = pzgram.Bot("662598430:AAFGsERMnrQdi1ugXjT5E6cpEIeiNDitlv0")
    bot.set_query({"instantanea" : instantanea , "Unminuto" : Unminuto, "Dieciminuti" : Dieciminuti, "Unora" : Unora})
    bot.set_commands({"start": inizio})
    bot.set_commands({"bottoni" : bottoni})
    bot.run()