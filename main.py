# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# need a Morse Code Dictionary
MC_DICT = {"A": ".-",
           "B": "-...",
           "C": "-.-.",
           "D": "-..",
           "E": ".",
           "F": "..-.",
           "G": "--.",
           "H": "....",
           "I": "..",
           "J": ".---",
           "K": "-.-",
           "L": ".-..",
           "M": "--",
           "N": "-.",
           "O": "---",
           "P": ".--.",
           "Q": "--.-",
           "R": ".-.",
           "S": "...",
           "T": "-",
           "U": "..-",
           "V": "...-",
           "W": ".--",
           "X": "-..-",
           "Y": "-.--",
           "Z": "--..",
           " ": " ",
           "0": "-----",
           "1": ".----",
           "2": "..---",
           "3": "...--",
           "4": "....-",
           "5": ".....",
           "6": "-....",
           "7": "--...",
           "8": "---..",
           "9": "----.",
           ".": ".-.-.-",
           ",": "--..--",
           "?": "..--..",
           }

ans = input("Enter: ")

print(ans)
print(type(ans))

translated_str = ""

# Translate
for c in ans:
    try:
        translated_str += MC_DICT[c.upper()]
        translated_str += " "
    except KeyError:
        print("Character not found")
        break

print(translated_str)
print("Done.")