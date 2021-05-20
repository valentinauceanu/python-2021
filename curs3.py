import random
print("Curs3")
elements = [x for x in range(11)]
# print(choices)
while True:
    random_choice = random.choice(elements)
    if random_choice % 3 == 0:
        break
    print(f"Random choice is {random_choice}")
print(f"Exit random choice is {random_choice}")

for i in range(11):
    if i % 2 != 0:
        continue
    else:
        print(f"Numar par: {i}")

# pass are rol de placeholder
my_sum = 0


def get_sum(a,b):
    #global my_sum
    my_sum = a+b
    print(my_sum)


get_sum(1, 2)
print(my_sum)


def my_function(*args, **kwargs):
    for arg in args:
        print(f"arg is {arg}")

# control slash


my_function(1,2,3,4, "ana", "are", "oboseala")


def function2(nume, prenume, *args, **kwargs):
    # for arg in args:
      #  print(f"{arg}")
     # tail = ' '.join(args) # functioneaza doar pe stringuri
     for key in kwargs.keys():
         print(f"key {key}, has value {kwargs[key]}")


function2("ana", "maria", '1', '2', '3', job = "student i guess", age = 11)

