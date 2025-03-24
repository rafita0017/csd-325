# example program that converts cups to fluid oz

def main():
    #display the intro screen.
    intro()

    try:
  #get number of cups
      cups_needed= int(input('Enter The number of cups:'))

  #convert cups to ounces
      cups_to_ounces(cups_needed)

    except:
      print("An execption occurred, try       again by entering only a number")
      print()
      main()

  #the intro function display an introduction screen
def intro():
      print('This program converts measurements')
      print('in cups to fluid ounces.         For your')
      print('reference the formula is:')
      print('1 cup= 8 fluid ounces')
      print()
  
  #the cups_to_ounces function accepts a number of
  # cups and displays the equivalent number of ounces.
def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to', ounces, 'ounces')

  #call the main function
main()