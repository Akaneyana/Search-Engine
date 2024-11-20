def readFile(fileName):
    with open(fileName, "r") as file:
        return file.readlines()
    
file_lines = readFile("tekstfil.txt") # runs the function above called readFile

def get_input():
    menuchoice = input("Choose an option: ")
    menuchosen(menuchoice)

def menuchosen(choice):
    if choice == "1":
        printText()
    elif choice == "2":
        printWord()
    elif choice == "3":
        findWord()
    elif choice == "4":
        findLine()
    elif choice == "5":
        countWord()
    elif choice == "6":
        exit()
    else:
        newchoice = input("Invalid option. Choose an option: ")
        menuchosen(newchoice)

def printText():
    for line in file_lines:
        print(line, end="")  #end= makes it so there isnt a gap between each line
    get_input()

def printWord():
    pWord = input("Chose a word: ")
    for line in file_lines:
        if pWord in line:
            print(pWord)
            break
    else:
        print("Word not found")
    get_input()

def findWord():
    tfWord = input("Chose a word: ")
    for line in file_lines:
        if tfWord in line:
            print(True)
            break
    else:
        print(False)
    get_input()

def findLine():
    keyWord = input("Choose a word: ")
    for line in file_lines:
        if keyWord in line:
            print(line, end="")
    if not any(keyWord in line for line in file_lines):
        print(f"The word '{keyWord}' was not found.")
    get_input()

def countWord():
    wordCount = input("Choose a word: ")
    text_content = "".join(file_lines)
    x = text_content.count(wordCount)
    print(f"The word '{wordCount}' appears {x} times.")
    get_input()

get_input()
