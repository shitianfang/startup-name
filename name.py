word_list = open('8EE4A3B1E8ADB8E7A8AFE8A8.txt', 'r', encoding='utf-8')
named_list = open("named-list.txt", 'w', encoding="utf-8")

for line in word_list:
    word = line.split()[0]
    named_list.write(
        f"{word}工具\n")

word_list.close()
named_list.close()
