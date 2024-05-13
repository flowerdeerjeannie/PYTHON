name = input("enter your name")
print(f"\nhello,{name}")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

active = True
while active:
     message = input(prompt)

     if message == 'quit':
          active = False
     else:
          print(message)