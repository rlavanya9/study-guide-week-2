# Create your classes here
class Student(object):

    def __init__(self, first_name,last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):

    def __init__(self, question,correct_answer):
        self.question = question
        self.correct_answer = correct_answer
    
    def ask_and_evaluate(self):
        for quest in self.question:
            user_answer = input(quest)
            if (self.correct_answer == user_answer):
                return True
            return False

class Exam(object):

    def __init__(self,name):
        self.question = []
        self.name = name
    
    def add_question(self, question):
        self.question.append(question)

    def administer(self,score = 0):
        for quest in self.question:
            if ask_and_evaluate():
                score += 1

class StudentExam():

    def __init__(self,student, exam, score):
        self.student = student
        self.exam = exam
        self.score = score


    def take_test(self):
        print("f{score}")

    def example():
        exam = []
        student = []
        exam.append(question 1)
        exam.append(question2)
        student.append("lav")
        student = StudentExam(student,exam)
        take_test()


