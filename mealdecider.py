#mealdecider.py

import random 

name = "Hungry Henry"
question = "What should I eat for breakfast?"

random_number = random.randint(1, 9)



#answers
if random_number == 1:
  answer = "Eggs on toasts!"
elif random_number == 2:
 answer = "Cocopops."
elif random_number == 3:
  answer = "Milk"
elif random_number == 4:
 answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
else:
  answer ="Very doubtful."

#time to print the convo!




#what if the user didn't fill their name?

if name == "" :
 print( "Question: " + question)
else:
 print( name + " asks: " + question)


#cont. print 

print("Magic 8-Ball's answer: " + answer )










