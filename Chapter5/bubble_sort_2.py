data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
n = len(data)
print('\033[32m', data, '\033[0m', '\033[32m'+'元のデータ'+'\033[0m')

for i in range(0, n-1):
    for j in range(0, n-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print('\033[31m', data, '\033[0m', '\033[31m'+'ソート後のデータ'+'\033[0m')
# print('\033[35m', data, '\033[0m',)
# print('\033[34m'+'赤色'+'\033[0m')