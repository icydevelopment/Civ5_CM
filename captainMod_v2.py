numbers = list(range(40))
print(numbers)
rows = 10
cols = 4
player = [[0 for j in range(rows)] for i in range(cols)]
# print(len(player))
# print(len(player[0]))

for k in range(cols):
    # print(len(numbers))
    # print(numbers)
    print('k= '+ str(k))
    for m in range(rows):
        print(numbers)
        player[k][m] = numbers[0]
        numbers.pop(0)