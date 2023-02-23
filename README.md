# Mixed-code
#!/bin/python3
from pygal import Bar
import time
import random
import numpy as np
age = []
p = True

which = input('begin the tutorial program first?: ')
which = which.strip()
which = which[0]
which = which.upper()
print(which)
if which == 'Y':
  p = True
  while p == True:
    #Username
    Uname = input('Hello user, what is your name?: ')
    print('')
    print('Hello ' + Uname + '. Please remember that your secret code can only compose of abcdefghijklmnopqrstuvwxyz!?1234567890: ')
    time.sleep(2.5)
    print('')
    
    # Set up data structures 
    alphabet = list('abcdefghijklmnopqrstuvwxyz!?1234567890 ')
    code = {}
    
    # Create the atbash code by reversing the alphabet
    def create_code():
      backwords = list(reversed(alphabet))
      
      for i in range (len(alphabet)):
        code[alphabet[i]] = backwords[i]
      #print(code)
    # Calculate the frequency of all letters in a piece of text
    
    
    
    # Make frequency chart
    
    
    
    # Encode/decode a piece of text — atbash is symetrical
    def atbash(text):
      text = text.lower()
      output = ''
      
      for letter in text:
        if letter in code:
          output += code[letter]
      
      return output
      
    
    
    # Fetch and return text from a file
    def get_text(filename):
      with open(filename) as f:
        text = f.read().replace('\n','')
      
      return text
  
  
    # Create a text-based menu system  
    def menu():
      choice =''
    
      while choice != 'c' and choice != 'f':
        choice = input('Please enter c to encode/decode text, or f to perform frequency analysis: ')
    
      if choice == 'c' or 'd':
        program = input('Would you like to encode/decode text?: ')
      program = program.strip()
      program = program[0]
      program = program.upper()
      if program == 'E':
          message = input('What is your secret code?: ')
          print('Running your code through the cypher…')
          code = atbash(message)
  
          print(code)
      elif program == 'D':
          message = input('What is your code?: ')
          print('Running your code through the cypher…')
          code = atbash(message)
          print(code)
      r = input('Would you like to continue with the rest of the program?: ')
      r = r.strip()
      r = r[0]
      r = r.upper()
      if (r != 'N'):
        p = False
  
    # Start up
    def main():
      create_code()
      #print (atbash('test'))
      menu()
    main()
q = input('did you begin the original or tutorial program first?: ')
q = q.strip()
q = q[0]
q = q.upper()
if q == 'T': 
  code = input('Create a passcode. Keep in mind that you can only use abcdefghijklmnopqrstuvwxyz!?134567890: ')
#if which == 'Y':
  S = ''
  while S == '':
    print('''
Welcome to the Test Security System''')
    print('******************************')
    password = code
    ex = input('What is the code: ')
    if ex == code:
      print('Access granted')
      time.sleep(2)
      print('We shall now check your age')
      print('***************************')

      time.sleep(2)
      age = int(input('Enter age: '))
      if age >= 18:
        print(' You are a Adult')
        age = ('Adult')
        age = ('Adult')
      elif age <= 10:
        print('You are a Child')
        age = ('Child')
        age = ('Child')
      elif age >=13 and age <=19:
        print('You are a Teen')
        age = ('Teen')
        age = ('Teen')
      elif age >= 10 and age <=13:
        print('You are a Tween')
        age = ('Tween')
        age = ('Tween')
      time.sleep(1)
      test = []
      print('We will now begin your ' + age + ' test: ')
      if age == 'Child':
        print('answer these 4 questions; ') # *25 4 %
        answer = input('What is 10*3: ')
        if answer == '30':
          test.append(1)
        answer = input('What is 13+44: ')
        if answer == '57':
          test.append(1)
        answer = input('What is 11*11: ')
        if answer == '121':
          test.append(1)
        answer = input('What is ((10+1)*1)*11: ')
        if answer == '121':
          test.append(1)
          ttest = sum(test)
        array = np.array(ttest)*25
        mltply = list(array)
      if age == 'Tween':
        print('answer these 5 questions;') # *20 4 %
        answer = input('What is 13*44: ')
        if answer == '572':
          test.append(1)
        answer = input('What is (12)²: ')
        if answer == '144':
          test.append(1)
        answer = input('Joe went to the shop with £5. He bought a pack of pencils for 45p, a bag for £2.35, and a school set for £8. However the school set was on sale, by how much percentage does the school set need to be so that Joe can afford it?: ')
        if answer == '72.5' or '72.5%':
          test.append(1)
        answer = input('Georgh got 62% on a test. What is the minimum questions to get 62%?: ')
        if answer == '62' or '62%':
          test.append(1)
        answer = input('There are 2 packs of chocolate. Each pack contains x chocolates. Everyone in the class eats 2 chocolates each, now there are 10 chocolates left (there are 15 more students than before). How many chocolates were in each box if there are 30 students?: ')
        if answer == '15':
          test.append(1)
        ttest = sum(test)
        array = np.array(test)*20
        mltply = list(array)
      if age == 'Teen':
        print('answer these 10 questions; ') # *10 4 %
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '': 
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        ttest = sum(test)
        array = np.array(test)*10
        mltply = list(array)
      if age == 'Adult':
        print('answer these 10 questions; ') # *10 4 %
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '': 
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        ttest = sum(test)
        array = np.array(test)*10
        mltply = list(array)
      print('Your grade is: ', mltply)
      grade = int(input('What was your grade?: '))
      if grade >= 80:
        print('You recieved...')
        time.sleep(1)
        print('Distinction')
        time.sleep(1)
      elif grade >= 70:
        print('You recieved...')
        time.sleep(1)
        print('Merit')
        time.sleep(1)
      elif grade >= 60:
        print('You recieved...')
        time.sleep(1)
        print('Pass')
        time.sleep(1)
      else:
        print('You recieved...')
        time.sleep(1)
        print('Fail')
        time.sleep(1)
if q != 'T':
  code = input('Create a passcode. Keep in mind that you can only use abcdefghijklmnopqrstuvwxyz!?134567890: ')
#if which == 'Y':
  S = ''
  while S == '':
    print('''
Welcome to the Test Security System''')
    print('******************************')
    password = code
    ex = input('What is the code: ')
    if ex == code:
      print('Access granted')
      time.sleep(2)
      print('We shall now check your age')
      print('***************************')

      time.sleep(2)
      age = int(input('Enter age: '))
      if age >= 18:
        print(' You are a Adult')
        age = ('Adult')
        age = ('Adult')
      elif age <= 10:
        print('You are a Child')
        age = ('Child')
        age = ('Child')
      elif age >=13 and age <=19:
        print('You are a Teen')
        age = ('Teen')
        age = ('Teen')
      elif age >= 10 and age <=13:
        print('You are a Tween')
        age = ('Tween')
        age = ('Tween')
      time.sleep(1)
      test = []
      print('We will now begin your ' + age + ' test: ')
      if age == 'Child':
        print('answer these 4 questions; ') # *25 4 %
        answer = input('What is 10*3: ')
        if answer == '30':
          test.append(1)
        answer = input('What is 13+44: ')
        if answer == '57':
          test.append(1)
        answer = input('What is 11*11: ')
        if answer == '121':
          test.append(1)
        answer = input('What is ((10+1)*1)*11: ')
        if answer == '121':
          test.append(1)
          ttest = sum(test)
        array = np.array(ttest)*25
        mltply = list(array)
      if age == 'Tween':
        print('answer these 5 questions;') # *20 4 %
        answer = input('What is 13*44: ')
        if answer == '572':
          test.append(1)
        answer = input('What is (12)²: ')
        if answer == '144':
          test.append(1)
        answer = input('Joe went to the shop with £5. He bought a pack of pencils for 45p, a bag for £2.35, and a school set for £8. However the school set was on sale, by how much percentage does the school set need to be so that Joe can afford it?: ')
        if answer == '72.5' or '72.5%':
          test.append(1)
        answer = input('Georgh got 62% on a test. What is the minimum questions to get 62%?: ')
        if answer == '62' or '62%':
          test.append(1)
        answer = input('There are 2 packs of chocolate. Each pack contains x chocolates. Everyone in the class eats 2 chocolates each, now there are 10 chocolates left (there are 15 more students than before). How many chocolates were in each box if there are 30 students?')
        if answer == '15':
          test.append(1)
        ttest = sum(test)
        array = np.array(test)*20
        mltply = list(array)
      if age == 'Teen':
        print('answer these 10 questions; ') # *10 4 %
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '': 
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        ttest = sum(test)
        array = np.array(test)*10
        mltply = list(array)
      if age == 'Adult':
        print('answer these 10 questions; ') # *10 4 %
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '': 
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        answer = input()
        if answer == '':
          test.append(1)
        ttest = sum(test)
        array = np.array(test)*10
        mltply = list(array)
      print('Your grade is: ', mltply)
      grade = int(input('What was your grade?: '))
      if grade >= 80:
        print('You recieved...')
        time.sleep(1)
        print('Distinction')
        time.sleep(1)
      elif grade >= 70:
        print('You recieved...')
        time.sleep(1)
        print('Merit')
        time.sleep(1)
      elif grade >= 60:
        print('You recieved...')
        time.sleep(1)
        print('Pass')
        time.sleep(1)
      else:
        print('You recieved...')
        time.sleep(1)
        print('Fail')
        time.sleep(1)
#  else:
 #   print('Access denied')
  #  time.sleep(0.5)
   # print('The program will restart')
    #time.sleep(2)
    #s = 'redo'

# == equal to, != not equal to, > Greater than, < Less than, >= Greater than or equal to, <= Less than or equal to33'
