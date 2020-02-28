from poem_back import *
from time import sleep

ghazal = Kind("divan\\ghazals")
saadi = Poet("saadi", "D:\\programming\\ganjoor\\saadi")
# name = "3"
# poem1 = Poem(name, saadi, ghazal)
# poem1.load_poem_from_ganjoor()
# poem1.print_poem()
# poem1.save_poem_pickle()
# poem1_1 = Poem.load_poem_pickle("D:\\programming\\ganjoor\\saadi\\divan\\ghazals\\{}.pm".format(name))
# beyts = poem1_1['all_beyts']
# print(beyts[0].print_b())

for sh in range(1, 638):
    num = str(sh)
    # poem = Poem(num, saadi, ghazal)
    # poem.load_poem_from_ganjoor()
    # poem.save_poem_pickle()
    poem = Poem.load_poem_pickle("D:\\programming\\ganjoor\\saadi\\divan\\ghazals\\{}.pm".format(sh))
    beyts = poem['all_beyts']
    print(num)
    for beyt in beyts:
        print(beyt.print_b())
    print("############" * 5)
