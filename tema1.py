# declarare lista
hw_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# printare lista ordonata fara modificare
print(sorted(hw_list))
# printare lista ordonata descrescator fara modificare
print(sorted(hw_list, reverse=True))
# printare numere pare din lista utilizand slice
print((sorted(hw_list))[1::2])
# printare numere impare din lista utilizand slice
print((sorted(hw_list))[::2])
# printare elemente multipli ai lui 3
for element in hw_list:
    if element % 3 == 0:
        print(element)
# alta varianta, cu slice
print((sorted(hw_list))[2::3])
