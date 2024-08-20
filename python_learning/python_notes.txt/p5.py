''' Accept average score from the student of his exam and print his result as follows:
0 to 49 is Fail 
50 to 74 is second class 
75 to 90 is first class 
91 to 100 is distinction 
Also check for invalid score

'''
student_score=int(input('Enter the average score of Exam for result:'))
if student_score >=91 and student_score<=100:
    print('The result of the student is Distinction')
elif student_score >=75 and student_score<=90:
     print('The result of the student is First class')
elif student_score >=50 and student_score<=74:
     print('The result of the student is Second class')
elif student_score >=0 and student_score>=0<=49:
     print('The result of the student is Fail')
else:
    print('Invalid input: please enter the valid input')
    
    
    
