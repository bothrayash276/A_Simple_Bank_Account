# ------------------------------
# Simple Bank Account Program 
# Submittion by Yash Bothra (Associate)
# ------------------------------

# Function to display balance
def get_balance(current_balance):
    # TODO: Print the current balance
    print(f"Your Current Balance is {current_balance}")



# Function to deposit money
def deposit(current_balance, amount):
    # TODO: Check if amount is valid
    if(amount>0):
    # If valid, add to balance
      current_balance += amount
    # Return updated balance
      return current_balance
    else:
    # Otherwise, show error
      print("Invalid Amount Entered!")
      return current_balance



# Function to withdraw money
def withdraw(current_balance, amount):
    # TODO: Check if amount is valid and not more than balance
    if(amount<=current_balance and amount>0):
    # If valid, subtract from balance
      current_balance -= amount
    # Return updated balance
      return current_balance
    else:
    # Otherwise, show error
      print("Invalid Amount Entered")
      return current_balance




initial_balance = 100

# Create the main program loop with the use of conditionals and loop statements
# D --> Deposit
# W --> Withdraw
# C --> Check balance
# Q --> Quit

# The loop should stop only if user enters Q

print("D --> Deposit \nW --> Withdraw \nC --> Check balance \nQ --> Quit")

while True:
  
  user_choice = str(input("How do you wanna proceed: "))

  # Deposit System
  if(user_choice=='D'):
    user_deposit = int(input("Enter the amount to be deposited: "))
    initial_balance = deposit(initial_balance,user_deposit)
    get_balance(initial_balance)

  # Withdrawing System 
  elif(user_choice=='W'):
    user_withdraw = int(input("Enter the amount to be withdrawn: "))
    initial_balance = withdraw(initial_balance,user_withdraw)
    get_balance(initial_balance)

  # Checking the Balance System
  elif(user_choice=='C'):
    get_balance(initial_balance)

  # Exiting the System
  elif(user_choice=='Q'):
    break

  # If input entered other than W,D,C,Q
  else:
    print("Invalid Input!")
    continue
  
  # Keeping the code clear
  print("\n")


