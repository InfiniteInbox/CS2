# -*- coding: utf-8 -*-
"""FINAL Rust Removal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsSRvIZlHuddAzba1Dgy4Flh5_Yh9xzK
"""

'''
Created on Friday, September 17th, 2021

Bugs:

Initiative: This code was designed to calculate the price of shipping of a given package.

Bonus:

Authors:
Murphy, Elijah, 
Pauley, Andy
Jain, Yash
'''

def zipcodeCalculator(zipcodeStart, zipcodeFinal):
  '''
  zipcodeCalculator
  Takes in ZipcodeStart and ZipcodeFinal, both intigers, as a result of user input
  Outputs zoneDistance, an intiger.
  '''
    try:
        if int(zipcodeStart) < 7000: 
          #these nested if's find the start zone that the package was sent from. 
            startZone = 1
        elif int(zipcodeStart) < 20000:
            startZone = 2
        elif int(zipcodeStart) < 36000:
            startZone = 3
        elif int(zipcodeStart) < 63000:
            startZone = 4
        elif int(zipcodeStart) < 85000:
            startZone = 5
        elif int(zipcodeStart) <= 99999:
            startZone = 6
        if int(zipcodeFinal) < 7000:
          #these nested if's find the start zone that the package was sent from. 
            endZone = 1
        elif int(zipcodeFinal) < 20000:
            endZone = 2
        elif int(zipcodeFinal) < 36000:
            endZone = 3
        elif int(zipcodeFinal) < 63000:
            endZone = 4
        elif int(zipcodeFinal) < 85000:
            endZone = 5
        elif int(zipcodeFinal) <= 99999:
            endZone = 6
        zoneDistance = abs(startZone - endZone)
        #This calculates distance by subtracting the to by the from in absolute value
        return(zoneDistance)
    except:
      return("Incorrect Input, Zip code is invalid")  

def packageClass(width,length,height):
  PCLASS = 0

  if length >= 3.5 and length <= 4.25 and height >=3.5 and height <=6 and width >= 0.007 and width <= 0.015: 
  #These nested if's checks to see if the backage dimensions fits in a class.
    PCLASS = 1 #This is a regular post card
  elif length > 4.25 and length < 6 and height > 6 and height < 11.5 and width >= 0.007 and width <= 0.015:
    PCLASS = 2 #This is a large post card
  elif length >= 3.5 and length <= 6.125 and height >= 5 and height <= 11.5 and width > .016 and width < .25:
    PCLASS = 3 #This is a regular envelope
  elif length > 6.125 and length < 24 and height >= 11 and height <= 18 and width >= .25 and width <= .5:
    PCLASS = 4 #This is a large envelope
  elif 2*width + 2*height + length < 84 and length > 24 and height > 18 and width > .5:
    PCLASS = 5 #This is a regular package
  elif 2*width + 2*height + length > 84 and length < 130:
    PCLASS = 6 #This is a large package
  else:
    PCLASS = 0

  return PCLASS

def Equation(PCLASS , zoneDistance):
  if PCLASS == 1: 
  #These nested if's calculates the total price by adding the price
  #of the type of package and 3 cents times the zones it drives through
    cost =.20+.03*zoneDistance
  elif PCLASS == 2:
    cost =.37+.03*zoneDistance
  elif PCLASS == 3:
    cost =.37+.04*zoneDistance
  elif PCLASS == 4:
    cost =.60+.05*zoneDistance
  elif PCLASS == 5:
    cost =2.95+.25*zoneDistance
  elif PCLASS == 6:
    cost =3.95+.35*zoneDistance
  return cost
  
def main(): 
  while True:
    try:
      # Asks user for lengthgth widthth and heightght of the mail

      length = float(input("What is the length of the package:"))
      height = float(input("What is the height of the package:"))
      width = float(input("What is the width of the package:"))
      zipcodeStart = int(input("What is the zipcode it is being sent from:"))
      zipcodeFinal = int(input("What is the zipcode it is going to:"))
      # Asks user for length width and height of the mail and zips
      if 0 < zipcodeStart < 100000 and 0 < zipcodeFinal < 100000 and width > 0 and height > 0 and length > 0:
      #Making sure that each input is positive
        zoneDistance = zipcodeCalculator(zipcodeStart, zipcodeFinal)
        PCLASS = packageClass(width,length,height) 
        if PCLASS == 0:
          print("\nSorry! Not Mailable\n")
          main()
        cost = Equation(PCLASS, zoneDistance)
        currency = "${:,.2f}".format(cost)
        print("\nIt will cost you", currency, "to ship this item.\n")
      else:
        print("\nIncorrect Input, Invalid zipcode or dimensions\n")

    except ValueError as e:
      print(e)
    


if __name__ == "__main__": 
  print(r"""\
  ___  _____  _____ _      ______         _     _____  __  __ _          
 / _ \/  __ \/  ___| |     | ___ \       | |   |  _  |/ _|/ _(_)         
/ /_\ \ /  \/\ `--.| |     | |_/ /__  ___| |_  | | | | |_| |_ _  ___ ___ 
|  _  | |     `--. \ |     |  __/ _ \/ __| __| | | | |  _|  _| |/ __/ _ \
| | | | \__/\/\__/ / |____ | | | (_) \__ \ |_  \ \_/ / | | | | | (_|  __/
\_| |_/\____/\____/\_____/ \_|  \___/|___/\__|  \___/|_| |_| |_|\___\___|
                                                                         
                                                                         """)
  print("Welcome to the price calculator!\n")
  main()