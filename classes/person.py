import re
from game import Game

class Person(Game):
    def __init__(self):
        self.pattern = '^\d\d\d\d$'
    def create_number(self):
        return Game.create_number(self)
    def check_number(self,number):
        return Game.check_number(self,number)
    def list_to_number(self,answer):
        return Game.list_to_number(self,answer)
    def calculate(self,number,answer):
        return Game.calculate(self,number,answer)
    def begin(self):
        number = self.create_number()
        while True:
            answer = raw_input('Enter a four digit number: ')
            try:
                if not re.match(self.pattern,answer):
                    raise ValueError()
            except ValueError:
                print 'Only four digits numbers are accepted'
                continue
            answer = map(int,answer)
            try:
                if not self.check_number(str(self.list_to_number(answer))):
                    raise Exception()
            except Exception:
                print 'Digits cannot be repeated'
                continue
            eval = self.calculate(number,answer)
            if (eval[0] == 4):
                print '4G, you won!'
                break
            else:
                print "%dG" % eval[0],"%dR" % eval[1]
