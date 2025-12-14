import random

f_names = ["James", "Michael", "Christopher", "Joshua", "Matthew", "David", "Daniel", "Andrew", "Joseph",
           "Justin", "Jessica", "Ashley", "Brittany", "Amanda", "Melissa", "Stephanie", "Jennifer"]
l_names = ["Smith", "Johnson", "Williams", "Moore", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Anderson",
           "Thomas", "Jackson", "Moore"]


def create_student(how_many):
    for i in range(how_many):
        f_name = f_names[random.randint(0, len(f_names) - 1)]
        l_name = l_names[random.randint(0, len(l_names) - 1)]
        sex = random.choice(['M', 'F'])
        print(f"INSERT INTO student(f_name, l_name, sex) VALUES('{f_name}', '{l_name}', '{sex}');")


create_student(10)


def create_test_scores(num_tests, num_studs):
    for i in range(1, num_tests + 1):
        for j in range(1, num_studs + 1):
            score = random.randrange(1, 25)
            print(f"INSERT INTO test_score VALUES({j}, {i}, {score});")


create_test_scores(4, 10)

