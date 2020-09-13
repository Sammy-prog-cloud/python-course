balance = 1000
year = 0
target = 3 * balance
rate = 5.0
while balance < target:
    year += 1
    interest = balance * rate / 100
    balance += interest
print("The investment tripled after", year, "years.")