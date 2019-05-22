from classes.person import Person
from classes.computer import Computer

print 'Welcome to four number game!'
print 'Wanna guess a number or let the computer guess?' 
try:
    option = raw_input('Choose 1 or 2 respectively: ')
    if option == '1':
        person = Person()
        person.begin()
    elif option == '2':
        computer = Computer()
        computer.begin()
    else:
        print 'Bad option. Try again!'
except KeyboardInterrupt:
    print '\nBye'
