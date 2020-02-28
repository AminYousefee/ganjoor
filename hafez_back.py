from poem_back import *
from time import sleep
##### this file is created to download and update from ganjoor, just that  #######
ghazal = Kind("ghazal")
hafez = Poet("hafez", "D:\\programming\\ganjoor\\hafez")
name = "2"
# poem1 = Poem(name, hafez, ghazal)
# poem1.load_poem_from_ganjoor()
# poem1.print_poem()
# poem1.save_poem_pickle()
poem1_1 = Poem.load_poem_pickle("D:\\programming\\ganjoor\\hafez\\ghazal\\{}.pm".format(name))
beyts = poem1_1['all_beyts']
print(beyts[0].print_b())
"""
for i in range(1, 496):
    name = str(i)
    poem = Poem.load_poem_pickle("D:\\programming\\ganjoor\\hafez\\ghazal\\{}.pm".format(name))
    Poem.print_saved_poem(poem)
target = "بوسه"
result_search_beyts = Poem.search_all("D:\\programming\\ganjoor\\hafez\\ghazal", target)
print(len(result_search_beyts), 'contains the word "{}" '.format(target))
for beyt in result_search_beyts:
    print(beyt.print_b(" // "))
"""
# beyts = poem1_1['all_beyts']
# print(beyts[0].print_b())
"""
for sh in range(469, 496):
    num = str(sh)
    poem = Poem(num, hafez, ghazal)
    poem.load_poem_from_ganjoor()
    poem.save_poem_pickle()
    sleep(2.5)
"""