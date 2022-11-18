# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абвМама мама абв мыла абвраму раму абвгд пара-пара-пам'
list = text.split()
print(list)

i= len(list)-1  # Идем с конца до первого элемента

while i >= 0:
    if 'абв' in list[i]:
        list.remove(list[i])
    i-=1
print(list)


# ------------------------------------------------
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример   AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

with open("RLE_text1.txt", 'w', encoding='utf_8') as file:
    a = file.write('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
 
list = []
list2 = []

count = 1

for i in range((a)):
    list.append(i)
print(list)
i=0
while i < (len(list)-1):
    if list[i] == list[i+1]:
        count += 1
    else:
        list2.append(str(count) + str(list[i]))
        
    i += 1
else: list2.append(str(count)+str(list[i]))
b = ''.join(list2)

print(b)


with open('RLE_text2.txt', 'w', encoding='utf8') as file:
    file.write(b)
