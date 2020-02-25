import requests
from bs4 import BeautifulSoup

class Poet:
    def __init__(self, name, details):
        self.name = name
        self.details = details


class Script:
    def __init__(self, content):
        self.content = content

class Poem(Script):
    def __init__(self, content):
        super().__init__(content)

class Mesra(Script):
    def __init__(self, content):
        super().__init__(content)


class Beyt():
    def __init__(self, mesra1, mesra2):
        self.mesra1 = mesra1
        self.mesra2 = mesra2

    def print_b(self, sep):
        beyt_content = self.mesra1.content + sep + self.mesra2.content
        print(beyt_content)


def reformat(txt):
    txt = str(txt)
    txt1 = txt.replace("<p>", "")
    txt2 = txt1.replace("</p>", "")
    return txt2


def poem(poet, kind, num):
    r = requests.get("https://ganjoor.net/{}/{}/sh{}/".format(poet, kind, num))
    soup = BeautifulSoup(r.content, 'html.parser')
    allElement = list(soup.children)
    html = allElement[2]
    body = list(html.children)[3]
    m1 = soup.find_all('div', class_='m1')
    m2 = soup.find_all('div', class_='m2')
    all_beyts = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            mes1 = m1[i].find('p')
            mesr1 = reformat(mes1)
            mesra1 = Mesra(mesr1)
            mes2 = m2[i].find('p')
            mesr2 = reformat(mes2)
            mesra2 = Mesra(mesr2)
            beyt = Beyt(mesra1, mesra2)
            all_beyts.append(beyt)
    return all_beyts

for num in range(1, 300):
    all_beyt = poem('hafez', 'ghazal', num)
    print("###" * 20)
    for beyt in all_beyt:
        beyt.print_b(' // ')
    print("###" * 20)
    print("\n" * 3)
