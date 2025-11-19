import re

rand_str = "412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, rand_str)
print("Matches :", len(matches))
for i in matches:
    print(i)

rand_str2 = "Hello Hello world "
regex2 = re.compile(r".{4}")
matches2 = re.findall(regex2, rand_str2)
print("Matches :", len(matches2))
for i in matches2:
    print(matches2)
