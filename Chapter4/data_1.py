with open("data.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

new_list = []

for i in data:
    word = i.split()
    new_list.append(word)

print(new_list)

a = "島袋"
b = "098"
new_list.append([a, b])

with open("data.txt", "a") as f:
    f.write('\n'+a+','+b)
