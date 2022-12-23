#Declaring global variables
file_name = 'question1_input.txt'   #change this to take input from a diff file or when file is in different directory
# file_name = r'A2_2021507\question1_input.txt' 

#Declaring functions
def input_choice()->int:    #Function to input the choice from user
    try_count = 0
    while try_count < 3:
        try_count += 1
        try:
            num = int(input('Please enter your choice: ').strip())
            if ((num < 1) or (num > 5)):
                print('The input is should be between 1 and 5')
                continue
            return num
        except:
            print('Please enter a valid integer')
            continue
    print('Program Terminated due to multiple invalid inputs')
    return False

def input_word(msg:str)->str:      #Function to input a word from user
    try_count = 0
    while try_count < 3:
        try_count += 1
        try:
            string = input(msg).strip()
            if string == '':
                print('Please enter a non-empty string')
                continue
            if not(string.isalpha()):
                print('The word cannot have numbers or symbols')
                continue
            return string
        except:
            print('Please enter a valid input')
            continue
    print('Program Terminated due to multiple invalid inputs')
    return False

def count_occurrence(req_word:str):      #Function to find occurrences of a word
    cnt = 0
    req_word = req_word.lower()
    with open(file_name, 'r') as f_reader:
        for line in f_reader:
            line.split(r'\n')
            for word in line.split():
                if word.lower() == req_word:    #If a word is capitalised, its still treated the same
                    cnt += 1
    if cnt == 0:
        print(f'{req_word} is not present in the specified text')
        return
    print(f'The word \'{req_word}\' occurs {cnt} times in the text')
    return 

def unique_words():     #Funtion to find all the unique words in the text, words with numbers and symbols are not counted
    unique_words = set()
    with open(file_name, 'r') as f_reader:
        for line in f_reader:
            line.split(r'\n')
            for word in line.split():
                unique_words.add(word.lower())
    if(len(unique_words) == 0):
        print('The file is empty')
        return
    unique_words = list(unique_words)
    unique_words.sort()
    print(f'There are {len(unique_words)} unique words in the text, as folows:-')
    print(*unique_words, sep = '; ')
    return

def word_count():       #Function to count the occurrence of each word in the file
    word_count = dict()
    with open(file_name, 'r') as f_reader:
        for line in f_reader:
            line.split(r'\n')
            for word in line.split():
                word = word.lower()
                if word in word_count.keys():
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    print('The following is the number of occurence of each word in alphaberical order:-')
    for num, word in enumerate(sorted(word_count)):
        print(f'{num + 1}) {word.capitalize()} -> {word_count[word]}')
    return

def replace_with(prev_word:str, new_word:str):      #Replace a given word with another
    text = []
    with open(file_name, 'r') as f_reader:
        for line in f_reader:
            line.split(r'\n')
            new_line = ''
            for word in line.split():
                if word == prev_word:
                    new_line += new_word + ' '
                else:
                    new_line += word + ' '
            new_line += '\n'
            text.append(new_line)
    f_writer = open(file_name, 'w')
    f_writer.writelines(text)
    f_writer.close()
    print(f'Successfully replaced \'{prev_word}\' by \'{new_word}\' in the text')
    return

def main():
    try:    #Check if file exists and is non-empty
        f_test = open(file_name, 'r')
        data = f_test.read()
        if data == '':
            print('The specified file is empty')
            f_test.close()
            return
        f_test.close()
    except FileNotFoundError:
        print("File doesn't exist in current directory.")
        return
    menu = ['Display specific word count', 'Display all unique words', 'Display count of all words', 'Replace word', 'Quit']
    while True:
        print('Choose one of the following:-')
        for num, desc in enumerate(menu):
            print(f'{num + 1}) {desc}')
        choice = input_choice()
        print()
        if choice is False:
            return
        elif choice == 1:
            word = input_word('Please enter the word: ')
            print()
            count_occurrence(word)
        elif choice == 2:
            unique_words()
        elif choice == 3:
            word_count()
        elif choice == 4:
            prev_word = input_word('Please enter the word to replace: ')
            new_word = input_word('Please enter the word to replace with: ')
            print()
            replace_with(prev_word, new_word)
        elif choice == 5:
            print('Program Terminated')
            return
        print()
        print('~' * 15)
        print()

if __name__ == '__main__':
    print('-' * 100)
    main()
    print('-' * 100)