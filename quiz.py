import sys


def get_questions():

    with open('questions.txt') as f:
            lines = f.readlines()

    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


try:
    questions = get_questions()
except IOError:
    print 'Questions file not found'
    sys.exit()
except IndexError:
    print 'Error: All questions in the question file must have answers'
    sys.exit()

score = 0
total = len(questions)
for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score+= 1
print 'You got %s out of %s questions right' %(score, total)