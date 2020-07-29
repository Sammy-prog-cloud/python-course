sea_creatures = ('shark', 'octopus', 'whale', 'crab')
print(sea_creatures[1])
print(sea_creatures[2])
print(sea_creatures[3])
print(sea_creatures[0])

print(sea_creatures[1:4])
print(sea_creatures[:4])
print(sea_creatures[2:])
print(sea_creatures[-3:-1])
print(sea_creatures[-4:1])
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(numbers[1:11:2])
print(numbers[::3])
sea_creatures = ['shark', 'octopus', 'blobfish',
'mantis', 'shrimp', 'anemone']
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern',
'Arctic']
print(sea_creatures+oceans)
sea_creatures = sea_creatures + ['yeti crab']
print(sea_creatures)
print(sea_creatures*3)
print(oceans*2)
for x in range(1, 4):
    sea_creatures += ['fish']
print(sea_creatures)
del(sea_creatures[1])
print(sea_creatures)
fish = ['barracuda', 'cod', 'devil ray', 'eel']
print(fish)
fish.append('dracula')
print(fish)
sea_creatures.append('starfish')
print(sea_creatures)
fish.insert(0, 'anchovy')
print(fish)
more_fish = ['fingerlings', 'tilapia', 'duer']
fish.extend(more_fish)
print(fish)
del(fish[1])
print(fish)
fish.remove('devil ray')
print(fish)
print(fish.pop(3))
print(fish)
fish.copy()
fish_2 = (fish.copy())
print(fish_2)
ss = "Sammy_Shark!"
print(ss[5:])
print(ss[:5])
print(ss[0:12:2])
print(ss[6:11])
print(ss[6:11:1])
print(len(ss))
print(len("let's print the length of this string."))
print(ss.count("a"))
print(ss.count("S"))
print(ss.count("m"))
print(ss.count("m")*2)
likes = "Sammy likes to swim in the ocean, likes to spin up the server, likes to smile, likes to eat food and play at all times"
print(likes.count("likes"))
print(ss.find("m"))
print(likes.find("likes"))
print(likes.find("likes", 9))
f = '57'
print(float(f))
print(str(12))
user = "Sammy"
lines = '50'
print("Congratulations, " + user + "! you just wrote " + str(lines) + "  lines of code.")
print("Congratulations, " + user + "! you just won 1 million naira and " + str(lines) + " packs of indomie noodles")
print("Congratulations, " + user + "! you have been awarded scholarship into our honourable school!" + " and you are expected to resume fully within one week")
print(user + " things are beginning to work together for your good!")
Lines_yesterday = "50"
Lines_today = "108"
lines_more = int(Lines_today) - int(Lines_yesterday)
print(lines_more)
Total_Point = "5524.53"
New_point = "45.30"
New_total_points = float(Total_Point) + float(New_point)
print(New_total_points)
print(tuple(['pull request', 'repository', 'open source']))
print(tuple('sammy'))
print(tuple(str(1000)))
print(list(('waghorn', 'beetle', 'magenta', 'repository')))
print(list('shark!'))
print(list(('Sammy' + 'is going to the' + 'bank later today')))
print(list('sammy is going to the bank later today'))
print(str("sammy is going to the bank later today"))
print(list('feathers'))
print(list("feathers")*2)
print(len(list('sammy is going to the bank later today')))
ss = "sammy is the most loved one among the whole of the class"
print(ss[:5])
my_int = 103204934813
print(my_int)
print(my_int-813)
x = 76 + 145
print(x)
my_string = 'Hello, World!'
my_flt = 45.06
my_bool = 5 > 9 #A Boolean value will return either
var = True or False
my_list = ['item_1', 'item_2', 'item_3', 'item_4']
my_tuple = ('one', 'two', 'three')
my_dict = {'letter': 'g', 'number': 'seven', 'symbol':
'&'}
print(my_string)
print(my_flt)
print(my_bool)
print(my_list)
print(my_tuple)
print(my_dict)
print(list(my_string))
print(len(list('my_flt')))
#Assign x to be an integer
x = 76
print(x)
#Reassign x to be a string
x = "Sammy"
print(x)
x = y = z = 0
print(x)
print(y)
print(z)
j, k, l = "Shark", 2.05, 15
print(j)
print(k)
print(l)
print("Sammy has {} balloons.". format(5))
new_open_string = "Sammy loves {}{}."
print(new_open_string.format("Open-Source", " Software"))
#Create a global variable, outside of a function
glb_var = "global"
#Print global variable outside function
print(glb_var)
print("Twinkle, Twinkle , little star, How i wonder what you are Up above the world so high like a diamond in the sky"*(2))
print("Sammy intends cooking {} {} and taking {} bottle of maltina today".format("two", "cups of rice", 2))
print("Sammy ate {0:.3f} percent of pizza".format(75.2345))
print("Sammy ate {0:.0f} percent of Pizza".format(75.23245))
x = 24
input("Guess a number")
if x > 3:
        print("x is positive")
elif x < 3:
        print("x is negative")
else:
        print(float("x is zero"))
l = "length of the triangle"
b = "breadth of the triangle"
Rectangle = 'lb'
input("value of b")
input("value of l")
print(Rectangle)







































































































