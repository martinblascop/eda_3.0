import re
from game import Game

class Computer(Game):
    def __init__(self):
        self.pattern = '^\dG\s\dR$'
    def create_number(self):
        return Game.create_number(self)
    def check_number(self,number):
        return Game.check_number(self,number)
    def list_to_number(self,answer):
        return Game.list_to_number(self,answer)
    def number_to_list(self,answer):
        return Game.number_to_list(self,answer)
    def calculate(self,number,answer):
        return Game.calculate(self,number,answer)
    def next_four_digit_number(self,number,max_number):
        number += 1
        while not self.check_number(str(number)):
            number += 1
        if number > max_number:
            return 1023
        else:
            return number
    def check_answer(self,list,number):
        in_list = True
        for value in list:
            eval = self.calculate(value[0],number)
            eval = str(eval[0])+'G '+ str(eval[1])+'R'
            if eval != value[1]:
                in_list = False
                break
        return in_list
    def begin(self):
        list_answer = []
        max_number = 9876
        number = self.create_number()
        while True:
            print 'How about',self.list_to_number(number),'?'
            answer = raw_input('Your answer: ')
            if not re.match(self.pattern,answer):
                print '\nBad answer. Try again!'
                continue
            if answer == '4G 0R':
                break
            list_answer.append([number,answer])   
            next_number = self.number_to_list(self.next_four_digit_number(self.list_to_number(number),max_number))
            while not self.check_answer(list_answer,next_number):
                next_number = self.next_four_digit_number(self.list_to_number(next_number),max_number)
                next_number = self.number_to_list(next_number)
            number = next_number
