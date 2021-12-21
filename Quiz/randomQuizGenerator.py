import random
import os
from datetime import date


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

##for quizNum in range(1,36):



for i in range(1,36):
    if os.path.exists('capitalsquiz%s.txt'%(i)) or os.path.exists('capitalsquiz_answers%s.txt' %(i)):
        os.remove('capitalsquiz%s.txt'%(i))
        os.remove('capitalsquiz_answers%s.txt' %(i))
    else:
        break

# Create the quiz and answer key files.
##quizFile = open('capitalsquizs.txt', 'w')
##answerKeyFile = open('capitalsquiz_answers.txt' , 'w')
### Write out the header for the quiz.
##quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
##quizFile.write((' ' * 20) + 'State Capitals Quiz (Form)')
##quizFile.write('\n\n')
### Shuffle the order of the states.
##states = list(capitals.keys())
##random.shuffle(states) 
##
##
##for questionNum in range(50):
##    correctAnswer=capitals[states[questionNum]]
##    wrongAnswers= list(capitals.values())
##    del wrongAnswers[wrongAnswers.index(correctAnswer)]
##    wrongAnswers=random.sample(wrongAnswers,3)
##    answerOptions=wrongAnswers+[correctAnswer]
##    random.shuffle(answerOptions)
##    
##    
##    quizFile.write('%s. What is the capital city of %s\n'%(questionNum+1, states[questionNum]))
##    for i in range(4):
##        quizFile.write('    %s. %s\n'%('ABCD'[i],answerOptions[i]))
##    quizFile.write('\n')
##
##    answerKeyFile.write('%s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
##    
##quizFile.close()
##answerKeyFile.close()

def create_file():
    try:
        global quizFile
        global answerKeyFile
        quizFile=open('capitalsquizss.txt', 'w')
        answerKeyFile=open('capitalsquiz_answerss.txt' , 'w')
        rstr='Date: '+str(date.today())
        quizFile.write(rstr.rjust(100,' ')+'\n\nName:\n\nGrade:\n\n')
        cstr='State Capitals Quiz (Form)'
        quizFile.write(cstr.center(100,' '))
        quizFile.write('\n\n')

    except FileExistsError as error:
        print(error+' Try to open the file on the system')
        
def shuffle_list():
    pass

def set_questions_and_answers():
    create_file()
    states=list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        correctAnswer=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        answerOptions=random.sample(wrongAnswers,3)+[correctAnswer]
        random.shuffle(answerOptions)

        try:
            quizFile.write('%s. What is the capital city of %s?\n'%(questionNum+1,states[questionNum]))
            for i in range(4):
                quizFile.write('    %s.  %s\n'%('ABCD'[i],answerOptions[i]))
            quizFile.write('\n')

            answerKeyFile.write('%s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
        except FileExistsError as error:
            print(error+ '\nFile not found')
    
    quizFile.close()
    answerKeyFile.close()

set_questions_and_answers()
