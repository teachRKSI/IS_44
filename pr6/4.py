#4.1
print("4.1")

str = "  Python — это здорово!  "
str.strip()
str.lower()
print(str)
print(len(str))

#4.2
print("\n4.2")
str = "яблоко,банан,вишня"
str = str.upper()
split_str = str.split(",")
for i in split_str:
    print(i)

#4.3
print("\n4.3")

string = input("Проверить строку: ")
string = string.lower().replace(" ", "")
print("палиндром") if string == string[::-1] else print("не палиндром")

#4.4
print("\n4.4")
helloworld = "hello world"
print(helloworld.replace(" ", "_"))