import random

class Game():
    def create_number(self):
        number = random.sample(range(10),4)
        while number[0] == 0:
            number = random.sample(range(10),4)
        return number
    def list_to_number(self,list):
        return list[0]*1000 + list[1]*100+ list[2]*10 + list[3]
    def number_to_list(self,number):
        list = []
        for digit in str(number):
            list.append(int(digit))
        return list
    def check_number(self,number):
        uniq = set()
        for digit in number: 
            uniq.add(int(digit))
        if len(uniq) == 4:
            return True
        else:
            return False
    def calculate(self,number,answer):
        good = 0
        regular = 0
        for index,value in enumerate(number):
            for index2,value2 in enumerate(answer):
                if (value == value2):
                    if (index == index2):
                        good += 1
                    else:
                        regular += 1
        return [good,regular]
