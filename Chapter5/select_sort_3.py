data = ["Asahi", "Tokiya", "Seika", "Yu", "Keita", "Yoshiya", "Koma", "Takahiro", "Seiga", "Yukitaka", "Shunta", "Haruya", "Ken", "Koitsi", "Ryuki", "Ryuto"]
print(data, "名前")

for i in range(0, 15):
    m = i
    for j in range(i+1, 16):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]
    # print(data, i+1)

print(data, "ソート後のデータ")