#!/bin/python3
from pygal import Bar
from frequency import english
import time
import random
age = []
p = True

which = input('Have you began this program or the tutorial program first?: ')
which = which.strip()
which = which[0]
which = which.upper()
if which == 'Y':
  while p == False:
    #Username
    Uname = input('Hello user, what is your name?: ')
    print('')
    print('Hello ' + Uname + '. Please remember that your secret message can only compose of abcdefghijklmnopqrstuvwxyz!?1234567890')
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
        choice = input('Please enter c to encode/decode text, or f to perform frequency analysis')
    
      if choice == 'c':
        program = input('Would you like to encode/decode text?')
      
        if program == 'encode' or 'e':
          message = input('What is your secret message?')
          print('Running your message through the cypher…')
          code = atbash(message)
  
          print(code)
        elif program == 'decode' or 'd':
          message = input('What is your code?')
          print('Running your code through the cypher…')
          code = atbash(message)
          print(code)
        r = input('Would you like to continue with the rest of the program?:')
        r = r.strip()
        r = r[0]
        r = r.upper()
        if (r != 'Y'):
          p = False
  
    # Start up
    def main():
      create_code()
      #print (atbash('test'))
      menu()
    main()
if which != 'Y':
  q = input('Do you want to begin the original or tutorial program?: ')
  q = q.strip()
  q = q[0]
  q = q.upper()
if q != 'T':
  code = input('Can you add your code from the previous program here?: ')
#if which == 'Y':
  S = ''
  while S == '':
    print('''
Welcome to PGO Security System''')
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
      test = [0]
      print('We will now begin your ' + age + ' test: ')
      if age == 'Child':
        print('answer these 4 questions; ') # *25 4 %
        answer = input('What is 10*3: ')
        if answer == 30:
          test.append(1)
        answer = input('What is 13+44: ')
        if answer == 57:
          test.append(1)
        answer = input('What is 11*11: ')
        if answer == 121:
          test.append(1)
        answer = input('What is ((10+1)*1)*11: ')
        if answer == 121:
          test.append(1)
        test*25
      if age == 'Tween':
        print('answer these 5 questions;') # *20 4 %
      if age == 'Teen':
        print('answer these 10 questions; ') # *10 4 %
      if age == 'Adult':
        print('answer these 10 questions; ') # *10 4 %
      print('Your grade is: ', test)
      grade = int(input('What was your grade?: '))
      if grade >= 80:
        print('Distinction')
      elif grade >= 70:
        print('Merit')
      elif grade >= 60:
        print('Pass')
      else:
        print('Fail')
#  else:
 #   print('Access denied')
  #  time.sleep(0.5)
   # print('The program will restart')
    #time.sleep(2)
    #s = 'redo'

# == equal to, != not equal to, > Greater than, < Less than, >= Greater than or equal to, <= Less than or equal to33'
