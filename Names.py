def name_letter (name):
    if name[0].lower() == 'e':
            return True
    else: 
          return False

user_input= input("Enter your Name: ")

if name_letter (user_input):
      print ("Your name starts with latter E ")

else:
      print (" Sorry but Your name doesn't start with letter E ")