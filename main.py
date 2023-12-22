import random


status_picture = 0
amount_of_words = 0
amount_of_words_see = 0
last_letter = ""
tab = []


def getName():
    file = open("names.txt")
    content_of_file = file.readlines()
    name = content_of_file[(random.randint(0,len(content_of_file)))-1]
    name_final = name.strip("\n")
    return str(name_final) # wydaje zmienna Słowa w stringu


def checkIt(clientInput,name,list1):
    global status_picture
    name_ = name.split(',') # Słowo zawarte w liscie
    # print(name_)
    word_len = len(name_) # długość Słowa jako lista
    global amount_of_words
    amount_of_words = word_len
    clientInput_len = len(clientInput) # długość wprowadzonych danych

    if clientInput in name:
        position = name_.index(clientInput)  # sprawdzamy pozycje litery w liscie ze Słowem
        global last_letter
        last_letter = str(name_[len(name_)-1]) # ostatnia litera w Słowie
        list1[position] = clientInput
        print(list1)
        global amount_of_words_see
        amount_of_words_see += 1
    elif clientInput == "q":
        print("Thanks for playing! :) ")
        quit()

    else:
        print("The Word doesn't contain this letter. {} mistake".format(status_picture))
        status_picture += 1
        print(list1)

def printStatusHangman(status_picture):

    if status_picture == 1:
        print('''
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "-------------------------------------"''')
    if status_picture == 2:
        print(
            '''
            "       | --------------              "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "-------------------------------------"'''
        )
    if status_picture == 3:
        print(
            '''
            "       | --------------              "
            "       |              |              "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "-------------------------------------"'''
        )
    if status_picture == 4:
        print(
            '''
            "       | --------------              "
            "       |              |              "
            "       |             /~\\             "
            "       |             \\_/             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "       |                             "
            "-------------------------------------"'''
        )
    if status_picture == 5:
        print(
            '''
            "       | --------------              "
            "       |              |              "
            "       |             /~\\            "
            "       |             \\_/            "
            "       |              |              "
            "       |              |              "
            "       |              |              "
            "       |              |              "
            "       |                             "
            "       |                             "
            "-------------------------------------"'''
        )
    if status_picture == 6:
        print(
            '''
            "       | --------------              "
            "       |              |              "
            "       |             /~\\            "
            "       |             \\_/            "
            "       |            \\ | /           "
            "       |             \\|/            "
            "       |              |              "
            "       |              |              "
            "       |                             "
            "       |                             "
            "-------------------------------------"'''
        )
    if status_picture == 7:
        print(
            '''
            "       | --------------              "
            "       |              |              "
            "       |             /~\\            "
            "       |             \\_/            "
            "       |            \\ | /           "
            "       |             \\|/            "
            "       |              |              "
            "       |             /|\\            "
            "       |            /   \\           "
            "       |                             "
            "-------------------------------------"'''
        )

def wordAppend(name, list):
    name_ = name.split(',')  # Słowo zawarte w liscie
    for x in range(0, len(name_)):
        list.append("_") #wypelnianie listy podłogami
    for a in list:
        print("'"+a+"'", end =" ")


Slowo = getName() #losuje Słowo
status_picture += 1
qst = input("\n Type 'q' if you want to exit")

wordAppend(Slowo, tab)
while qst != "q":
    
    qst1 = input("\n Type letter >>> ")
    checkIt(qst1, Slowo, tab)
    printStatusHangman(status_picture)
    if status_picture == 7:
        print("Lose!")
        break
    if (amount_of_words_see == amount_of_words) and (last_letter == qst1):
        print("Win!")
        break








