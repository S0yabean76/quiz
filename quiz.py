import sys


def get_questions():
    with open('questions.txt') as f:
            lines = f.readlines()
    return [(lines[i], lines[i+1].strip().lower()) for i in range(0, len(lines), 2)]

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
attempts = 3
guess = ''
for question, answer in questions:
    #check that the user still has guesses left and the answer was wrong
    while (attempts != 0) and guess != answer:
        guess = raw_input(question).lower()
        #if guess is correct add one to the score and reset the number of guesses
        if guess == answer:
            score+= 1
            attempts = 3
        #if the guess is wrong reduce the number of attempts and show prompt
        elif guess != answer:
            #check whether the answer is close enough
            mistakes = 0
            try:
                for i in range(len(answer)):
                    if guess[i] != answer[i]:
                        mistakes += 1
            except:
                #refine so that mistakes is the same as the number of missing digits - TO DO
                mistakes = 3
                print "Your answer is too short."
            if mistakes <= 2:
                score += 1
                attempts = 3
                print "That's close enough"
                break
            elif mistakes > 2:
                attempts -= 1
                print "Don't give up! You have %s more attempts" % attempts

print 'You got %s out of %s questions right' %(score, total)