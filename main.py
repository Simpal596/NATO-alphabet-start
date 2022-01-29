import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
name = (input("enter your name: ")).upper()
list = [code for (letter,code) in dict.items() if letter in name]
print(list)
