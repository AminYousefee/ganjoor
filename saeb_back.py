from poem_back import *
import os
from time import sleep
from playsound import playsound
import threading

ghazal = Kind("divan-saeb\\ghazalkasa")
saeb = Poet("saeb", "D:\\programming\\ganjoor\\saeb")
name = "2"
# poem1 = Poem(name, saeb, ghazal)
# poem1.load_poem_from_ganjoor()
# poem1.print_poem()
# poem1.save_poem_pickle()
poem1_1 = Poem.load_poem_pickle("D:\\programming\\ganjoor\\saeb\\divan-saeb\\ghazalkasa\\{}.pm".format(name))
beyts = poem1_1['all_beyts']
print(beyts[0].print_b())

#def play_alarm():
#    playsound("eme_alarm.mp3")

#t3 = threading.Thread(target=play_alarm)

#for sh in range(5701, 6996):
#    try:
#        num = str(sh)
#        poem = Poem(num, saeb, ghazal)
#        poem.load_poem_from_ganjoor()
#        poem.save_poem_pickle()
#        if sh % 25 == 0:
#            sleep(3)
#        if sh % 64 == 0:
#            playsound("notif2.mp3")
#    except:
#        t3.start()
#        input("check and then enter")
#playsound("finish.mp3")
