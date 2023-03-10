import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for(index,row) in data.iterrows()}
print(phonetic_dict)

def generate():
    word=input("enter a word: ").upper()
    try:
        list=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry! Only alphabets please")
        generate()
    else:
        print(list)

generate()