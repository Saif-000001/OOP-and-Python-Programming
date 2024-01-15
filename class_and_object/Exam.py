class Exam:
    def __init__(self, subject):
        self.subject = subject
        self.min_number = 33
        self.max_number = 80
    def great_mark(self, number):
        if number < self.min_number:
            print(f'Get {number} numer person called fail')
        elif number >= self.max_number:
            print(f'Get {number} number person called A+')
        else:
            print(f'Get {number} number person called pass')

math = Exam('Math')
math.great_mark(80)
math.great_mark(33)
math.great_mark(32)