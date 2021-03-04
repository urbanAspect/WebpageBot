numbers = [412, 667, 852, 858, 870, 875, 882, 883, 931, 938, 979, 1030, 1051, 1095, 1135, 1174]
pages = []
for i in range(len(numbers)):
    a = numbers[i] / 247
    b = a - int(a)
    c = b * 247
    pages.append(int(c))

print(pages)

