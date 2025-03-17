# """version one of the counter"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt))


# """version 2"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt.replace(" ", "")))


word = input(f"Enter five phrases separated by |: ")
word = word.split("|")
for x in word:
    print(x,":",len(x.replace(" ", "")))


