import sys


def add_questions():
        add = raw_input('Would you like to add a question? (Y/N)\n')
        if add.lower() == 'y':
            question = raw_input('Please enter a question\n')
            f.write(question + "\n")
            answer = raw_input('Please enter the answer\n')
            f.write(answer + "\n")
            add_questions()
        elif add.lower() == 'n':
            print ('Bye for now!')
            sys.exit()
        else:
            print ('Please enter a valid response')
            add_questions()

with open('questions.txt', 'a') as f:
    add_questions()