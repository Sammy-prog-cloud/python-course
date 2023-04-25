#number = int(input())
#for i in range(1, number):
    #print(str(), i**i)
#data = str(4)
#print(data)

rand_string = "This is an important string"
rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()

orig_string = input("Enter in Acronymn : ")
orig_string = orig_string.upper()
list_of_words = orig_string.split()
for word in list_of_words:
    print(word[0], end="")
print()
