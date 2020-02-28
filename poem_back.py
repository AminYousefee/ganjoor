import requests
from bs4 import BeautifulSoup
from time import sleep
import pickle
from os import listdir
from playsound import playsound
import threading


def play_music():
    playsound("cry.mp3")


class Kind:
    def __init__(self, name):
        self.name = name


class Mesra:
    def __init__(self, content):
        self.content = content


class Beyt:
    def __init__(self, mesras):
        self.mesras = mesras

    def print_b(self, sep=" // "):
        beyt_content = self.mesras[0].content + sep + self.mesras[1].content
        return beyt_content


class Poem:
    def __init__(self, name, poet, kind):
        self.all_beyts = []
        self.name = name
        self.poet = poet
        self.kind = kind
        self.url = "https://ganjoor.net/{}/{}/sh{}/".format(poet.name, kind.name.replace("\\", "/"), name)
        # self.file_address = self.poet.directory + "\\{}\\{}.pm".format(self.kind, self.name)

    def print_poem(self, sep=" // "):
        print("#########" * 15)
        for beyt in self.all_beyts:
            print(beyt.print_b(sep))
        print("#########" * 15)
        print("\n")

    def poem_content(self, sep="\n"):
        txt = ""
        for beyt in self.all_beyts:
            txt += beyt.print_b()
            txt += sep

    @staticmethod
    def print_saved_poem(dict_poem, sep=" // "):
        print("#########" * 15)
        for beyt in dict_poem['all_beyts']:
            print(beyt.print_b(sep))
        print("#########" * 15)
        # print("\n")

    @staticmethod
    def search_all(directory, target_word):
        print("searching...")
        search_result_beyts = []
        for file_name in listdir(directory):
            po_dic = Poem.load_poem_pickle(directory + "\\" + file_name)
            beyts = po_dic['all_beyts']
            for beyt in beyts:
                for mes in beyt.mesras:
                    if target_word in mes.content:
                        item = (beyt, po_dic['name'])
                        search_result_beyts.append(item)
                        break
        print("search is finished")
        print("total reasults:", len(search_result_beyts))
        return search_result_beyts

    def load_poems_from_ganjoor(self):
        pass

    def load_poem_from_ganjoor(self):
        print("connecting to ganjoor:  {}".format(self.url))
        try:
            r = requests.get(self.url)
            if not r.ok:
                t2 = threading.Thread(target=play_music)
                t2.start()
                print("wait for 10 second then I try again")
                sleep(10)
                print("connecting to ganjoor...")
                input("there is a problem check the connection and vpn and then press Enter")
                print("trying to connect again...")
                r = requests.get(self.url)
        except:
            # playsound("alarm.mp3")  must be multi thred
            print("wait for 10 second then I try again")
            t4 = threading.Thread(target=play_music)
            t4.start()
            sleep(10)
            print("connecting to ganjoor...")
            input("there is a problem check the connection and vpn and then press Enter")
            print("trying to connect again...")
            r = requests.get(self.url)
        print("connected to ganjoor!")
        soup = BeautifulSoup(r.content, 'html.parser')
        m1 = soup.find_all('div', class_='m1')
        m2 = soup.find_all('div', class_='m2')
        all_beyts = []
        if len(m1) == len(m2):
            for i in range(len(m1)):
                mes1 = m1[i].find('p')
                mes1 = mes1.get_text()
                mesra1 = Mesra(mes1)

                mes2 = m2[i].find('p')
                mes2 = mes2.get_text()
                mesra2 = Mesra(mes2)

                beyt = Beyt([mesra1, mesra2])
                all_beyts.append(beyt)
                self.all_beyts = all_beyts
        print("poem{} is loaded from ganjoor successfully".format(self.name))
        return all_beyts

    def save_poem_pickle(self):
        directory = self.poet.directory + "\\{}\\".format(self.kind.name)
        file_address = directory + self.name + ".pm"
        # print("file address:", file_address)
        poem_dict = self.__dict__
        with open(file_address, "wb") as file:
            pickle.dump(poem_dict, file)
        print("poem {} saved successfully".format(self.name))
        print("///////" * 10)

    @staticmethod
    def load_poem_pickle(file_address):
        with open(file_address, "rb") as file:
            poem = pickle.load(file)
        return poem


class Poet:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
