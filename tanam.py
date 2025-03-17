# """version one of the counter"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt))


# """version 2"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt.replace(" ", "")))


# word = input(f"Enter five phrases separated by |: ")
# word = word.split("|")
# for x in word:
#     print(x,":",len(x.replace(" ", "")))

def encrypt(salt, plaintxt):
    if(salt.find(plaintxt) >= 0):
        if(salt.find(plaintxt) % 2 == 0):
            ind = salt.find(plaintxt)
            replacement = salt[(ind+1)]
            return replacement
        else:
            ind = salt.find(plaintxt)
            replacement = salt[(ind-1)]
            return replacement
    else:
        return plaintxt
# def decrypt(cipher):

salt = "kajipotefu"
txt = input("Enter a letter: ")
txt = txt.lower()
txt = list(txt)
result = ""
for i in range(len(txt)):
    txt[i] = encrypt(salt, str(txt[i]))

for i in txt:
    result += i
print("The encrypted text: ", result)
