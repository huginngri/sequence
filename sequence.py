n = int(input("Enter the length of the sequence: ")) # Do not change this line

#Þrjár grunntölur
num_1 = 1
num_2 = 2
num_3 = 3
num_4 = 0
counter = 3
if n == 1:
    print(num_2)
elif n == 2:
    print(num_1,",", num_2)
elif n == 3:
    print(num_1,",", num_2, ",", num_3)
elif n < 1:
    print("Invalid length")
else:
    print(num_1,",", num_2,",", num_3, end=",")
    while counter < n:
        num_4 = num_1 + num_2 + num_3
        print(num_4, end=",")
        num_1 = num_2
        num_2 = num_3
        num_3 = num_4
        counter += 1
