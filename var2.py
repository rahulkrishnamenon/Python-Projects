array = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: "))
    array.append(element)

array.sort()
print('Second largest number is:', array[-2])