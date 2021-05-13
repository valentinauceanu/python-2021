print("Acesta este cursul 2")

nume = "Ana"
if nume == "Ana":
    print(nume)
else:
    print(names)
    print("nu stiu")

first_person = {"Name": "John"}
second_person = {"Name": "John"}

if first_person is second_person:
    print("They are the same")
else:
    print("They are not the same")


print(ord('b'))
print(chr(73))

my_str = 'Ana are mere'
print(my_str)

my_str2 = 'Owner\'s manual' #"Owner's manual"
print(my_str2)

m = 'Owner\'s \r manual' #ciudat
# r inainte de ' arata toate chestiile dinauntru
print(m)
#""" """ = multiline string

def my_function():
    """this function does something"""

mesaj = "{} is {} years old".format('Ion', 18)
print(mesaj)

msg = "{name} is {age} years old".format(name = 'Ion', age = 18)
print(msg)

ms = "{0} is {1} years old".format('Ion', 18)
print(ms)

name = 'Ion'
age = 18
msg = f"{name} is {age} years old" #interpolare
print(msg)

l = [1,2,3, 'Ana are mere', [4,5,6], True, False, None]
l[5] = '99'
print(l)

for thingie in l:
    print(thingie)
for index, value in enumerate(l):
    print(f'{value} cu index {index}')

print(l[-1])
