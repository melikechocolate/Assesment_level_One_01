import random, sys, time, os, math
# make text bold 
BOLD = '\033[1m'
END = '\033[0m'

#--------------------------------------------------------------------------------------------------------------

# Setup for various ANSI escape codes for terminal text and background colors
sys_T_grey_TEXT = "\033[90m"
sys_T_red_TEXT = "\033[91m"
sys_T_green_TEXT = "\033[92m"
sys_T_yellow_TEXT = "\033[93m"
sys_T_blue_TEXT = "\033[94m"
sys_T_magenta_TEXT = "\033[95m"
sys_T_cyan_TEXT = "\033[96m"
sys_T_white_TEXT = "\033[97m"
sys_H_grey_white_TEXT = "\033[100m "
sys_H_red_black_TEXT = "\033[101m"
sys_H_green_black_TEXT = "\033[102m"
sys_H_yellow_black_TEXT = "\033[103m"
sys_H_blue_black_TEXT = "\033[104m"
sys_H_magenta_black_TEXT = "\033[106m"
sys_H_cyan_blue_black_TEXT = "\033[106m"
sys_H_white_black_TEXT = "\033[107m 18"
sys_H_password = "chocolateman"

#--------------------------------------------------------------------------------------------------------------

 # loading bar before clearing the bord.
print(f"{BOLD}     -SYSTEM STATUS-{END}")

for i in range(11):
    b = '█'*i + '░'*(10-i)
    print(f'\rProgress: [{b}] {i*10}%', end=''); time.sleep(0.1)

#--------------------------------------------------------------------------------------------------------------

# clear the bord for the user despaly.
def clear():
    """Wipes the terminal screen clean."""
    # 'nt' is the internal name for Windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise, it's Mac or Linux
    else:
        os.system('clear')

clear()

#--------------------------------------------------------------------------------------------------------------

# print the eorrer message with red colour and an [!]
def error(error_message):
    """print the colour and font for the error message"""
    error = print(f"{sys_T_red_TEXT} [!] {error_message}... {END}\n")


#--------------------------------------------------------------------------------------------------------------

# Checks that the user enters a valid integer for the number of rounds.
# It also handles the "Infinite mode" trigger (empty input).
def int_check_Q(Question):
    while True:

        error = (f"{sys_T_red_TEXT} [!] Please enter an integer that is 1 or more...{END}")

        to_check = input(Question)

        # check for infinite mode 
        if to_check == "":
            return "Infinite"


        try:

            response = int(to_check)

            #checks that the number is more than / equal to 13 
            if response < 1: 
                print(error)
            
            else :
                return response
            
        except ValueError:
            print(error)


#--------------------------------------------------------------------------------------------------------------

# checks user enter an int / float that is
# more than a minimum (default minimum is zero)
# Allows exit code.
def int_check(question, low=None, high=None, exit_code=None,):

    while True: 
        response = input(question).lower().strip()
        if response == exit_code:
            return response
        try:
            response = float(response) 
            if low is not None and response < low:
                error("Your number is to low please enter a higher number")
            elif high is not None and response > high:
                error("You number is too high please enter a lower number")
            else:
                # convert to int if it's a whole number for cleaner look
                return int(response) if response.is_integer() else response
        except ValueError:
            error("Please enter in a number")

#--------------------------------------------------------------------------------------------------------------

# Validates that the user types 'yes' or 'no' (or 'y'/'n') and handles errors.
def yes_no(Qustion):

    """code for yes or no"""


    while True:

        responce = input(Qustion).lower()

        #check the yes or no 
        if responce == "yes" or responce == "y":
            return "yes"
            print(instructions)
        elif responce == "no" or responce == "n":
            return "no"
        else:
            print("\033[91m [!] please enter yes or no...\033[0m")

#--------------------------------------------------------------------------------------------------------------

# Check that users have entered a valid
# option based on a list
# Check that users have entered a valid
# option based on a list
def string_checker(Question, valid_ans=( sys_H_password,'mix', 'mx','hard','h','medium','m','easy','e','')):
    error = f"\n{sys_T_red_TEXT} [!] Please enter Hard, Medium, Easy, or Enter for MIX? {END}\n"

    while True:
        # Get input and clean it with .strip() and .lower()
        user_response = input(Question).lower().strip()

        # 2. Check if the input exists in your valid list
        if user_response in valid_ans:
            return user_response  # Valid. Return and exit the while loop
        
        
        #print error if user does not enter something that is vaild 
        print(error)


#--------------------------------------------------------------------------------------------------------------

# Varbles: 

# Variables to store the visual styling of the game title.
Title_01 = f"""

        ***Quiz***
    ====================
      Linear Equations
    ====================
"""
# A version of the title using grey text for a "dimmed" effect.
Title_02_dimed = f"""{sys_T_grey_TEXT}

        ***Quiz***
    ====================
      Linear Equations
    ====================
{END}
"""
#---------------------------------------------------------------

# Displays the main title.
print(Title_01)


# List of math operators used for generating random questions.
AMP_item = [
    "-",
    "x",
    "+",
    "/"
]

# List of algebraic variables to be used in the equations.
items = [
   "a",
   "b",
   "c",
   "𝑥",
   "y",
   "z",
   "m"
]
# List used to randomly select which "template" of math question to generate.
# item_question = [
#     "Q1",
#     "Q2",
#     "Q3",
#     "Q4",
#     "Q5"
# ]
item_question = []

# Ask user if they what instructions:
want_instructions = yes_no(" [?] Would you like to see the instructions for the Quiz? ")

# Developer mode
Developer = 0

# Prints the instruction header for the user.
def instructions():
    """gives instructions"""

    print(f"""
=============================   
   **** Instructions ****

When you enter the Quiz you 
will be test on your skills 
  on{BOLD} Linear Equations{END}.

The first thing that you have
a choice of{BOLD} Easy, Hard, Medium,
            or Mix.{END}

 {BOLD}- Easy/E{END} 
Shows questions like...

- 8 / 1 = 𝑥 
- 4 + b = 9
- m x 6 = 12
-{sys_T_grey_TEXT} Q1, Q2, Q3{END}

 {BOLD}- Medium/M{END}
Shows questions like...

- c - 7 = 21
- 𝑥 / 5 - 1 = 5
- 1 / b = 3
-{sys_T_grey_TEXT} Q1, Q2, Q4{END}

 {BOLD}- Hard/H{END}
Shows questions like...

- 𝑥 x 9 + 3 = 27 
- 2b + 5 = 30
-{sys_T_grey_TEXT} Q4, Q5{END}

 {BOLD}- Mix/Mx/(enter){END}
 Shows questions like...

- 5 / y = 45
- 𝑥 - 6 x 5 = 30
- 2m - 4 = 4
- 6 x 6 = z
- m + 1 = 8
-{sys_T_grey_TEXT} Q1, Q2, Q3, Q4, Q5{END}

        ***Hints***

{BOLD}Example:
{END}
To get rid of on the left side,
 you must perform the inverse 
 (opposite) operation. The 
 opposite of adding 10 
 is{BOLD} subtracting 10.{END} 

Original: 𝑥 + 10 = 14
 

Action: Subtract 10 from both 
sides to keep the equation balanced:

        𝑥 + 10 - 10 = 14-10 

Result: 𝑥 = 14-10

Result: 𝑥 = 4


Because you subtracted 10 
from the left to cancel it out, 
it appears on the right side as "10"

{BOLD}The Shortcut: "Change Sides, Change Signs"{END}
|-------------------------------------------|
|     {BOLD}Original Sign{END}    |     {BOLD}Changes To {END}    |
|----------------------|--------------------|
| Addition (+)	       | Subtraction (-)    |
| Subtraction (-)      | Addition (+)       |
| Multiplication (x)   | Division (/)       |
| Division (/)	       | Multiplication (x) |
|-------------------------------------------|

        =============================
                  GOOD lUCK
        =============================        
    """)

# clear the bord and show the instucrtions if "YES".
if want_instructions == "yes":
    instructions()
    input(f"{sys_T_grey_TEXT} Pess enter to continue...{END}")
    clear()
else:
    clear()


# Ask the user to play Hard, Medium, or Easy which adds to list
# shows the tiltle 
print(Title_02_dimed)


MEHM_moded = string_checker(f" [?] Would you like your test Hard, Medium, Easy, or MIX (Enter)? ")

if MEHM_moded == sys_H_password :
    clear()
    Developer = 2
    print(f"{sys_T_grey_TEXT}Hello Bhavneet ~Developer mode~{END}")

    print(Title_02_dimed)

    MEHM_moded = string_checker(f" [?] Would you like your test Hard, Medium, Easy, or MIX (Enter)? ")

if MEHM_moded in ["mix", "mx", ""]:
 item_question.extend(["Q1", "Q2", "Q3", "Q4", "Q5"])

if MEHM_moded == "hard" or MEHM_moded ==  "h":
 item_question.extend([ "Q4", "Q5"])
 
if MEHM_moded == "medium" or MEHM_moded ==  "m":
 item_question.extend(["Q1", "Q2", "Q4"])

if MEHM_moded == "easy" or MEHM_moded ==  "e":
 item_question.extend(["Q1", "Q2", "Q3",])

print(sys_T_grey_TEXT, item_question, END)
# List to track the results of each round for the end-game summary.
test_history = []


# Main Routine Starts Here 

# Initialize tracking variables for the game state and statistics.
mode = "REGULAR"
rounds_played = 0
rounds_fail = 0 
total_rounds = 0

# shows the tiltle and clears the board too
input(f"{sys_T_grey_TEXT}Pess enter to cotinue...{END}")
clear()
print(Title_02_dimed)

# Ask user for number of rounds / infinite mode 
num_rounds = int_check_Q(f"{BOLD} [?] How many questions would you like? Push <enter> for infinite mode? {END}")

# Game Loop starts here 

# Set infinite mode flags if necessary.
if num_rounds == "Infinite":
    mode = "Infinite"
    num_rounds = 5
elif mode == "REGULAR":
    total_rounds = num_rounds

 
# Test Loop ends here
# Primary Test Loop: runs until the specified number of rounds is reached.
while rounds_played < num_rounds:
   # Display round number and mode type to the user.
   if mode == "Infinite":
       rounds_heading = f"\n{BOLD} question {rounds_played +1}{END}{sys_T_grey_TEXT} (Infinite Mode) {END}\n"
   else:
       rounds_heading = f"\n{BOLD} questions {rounds_played + 1}{END}{sys_T_grey_TEXT} of {num_rounds} {END}\n"
    # Randomize numbers and operators for the current round's equation.
   Num_01 = random.randrange(1,10)
   Num_02 = random.randrange(1,10)
   Num_03 = Num_01 * Num_02
   AMP = random.choice(AMP_item)
   AMP_02 = random.choice(AMP_item)
   question = random.choice(item_question)
   XYZBC_chocie = random.choice(items)

# changing the signs for the explaning of the answer
   if AMP == "x":
       sign_01 = "/"
   elif AMP == "/":
       sign_01 = "x"
   elif AMP == "-":
       sign_01 = "+"
   elif AMP == "+":
       sign_01 = "-"
   if AMP_02 == "x":
       sign_02 = "/"
   elif AMP_02 == "/":
       sign_02 = "x"
   elif AMP_02 == "-":
       sign_02 = "+"
   elif AMP_02 == "+":
       sign_02 = "-"

        

   # Template Q1: Basic Equation format (Variable Operator Number = Result)        
   if question == "Q1":
        if AMP == "/":
            Answer = Num_03 * Num_01

        elif AMP == "x":
            Answer = Num_03 / Num_01

        elif AMP == "+":
            Answer = Num_03 - Num_01

        elif AMP == "-":
            Answer = Num_03 + Num_01

        Answer_02 = f"{Num_03} {sign_01} {Num_01}"
        question= f"{XYZBC_chocie} {AMP} {Num_01} = {Num_03}"
        # Template Q2: Basic Equation format (Number Operator Variable = Result)
   elif question == "Q2":
        if AMP == "/":
            Answer = Num_03 * Num_01

        elif AMP == "x":
            Answer = Num_03 / Num_01

        elif AMP == "+":
            Answer = Num_03 - Num_01

        elif AMP == "-":
            Answer = Num_03 + Num_01
        Answer_02 = f"{Num_03} {sign_01} {Num_01}"
        question= f" {Num_01} {AMP} {XYZBC_chocie} = {Num_03}"
        # Template Q3: Equation with result as the variable (Number Operator Number = Variable)
   elif question == "Q3":

        if AMP == "x":
            Answer = Num_02 * Num_01

        elif AMP == "+":
            Answer = Num_02 + Num_01

        elif AMP == "-":
            Answer = Num_02 - Num_01

        Answer_02 = f"{Num_02} {AMP} {Num_01}"
        question = f" {Num_02} {AMP} {Num_01} = {XYZBC_chocie} "

        if AMP == "/":
            Answer = Num_03 / Num_01
            Answer_02 = f"{Num_03} {AMP} {Num_01}"
            question = f" {Num_03} {AMP} {Num_01} = {XYZBC_chocie} "
        # Template Q4: Multi-step equation (Variable Op Num Op Num = Result)
   elif question == "Q4":
        # Calculation logic for multi-step addition and subtraction
        question = f"{XYZBC_chocie} {AMP} {Num_01} {AMP_02} {Num_02} = {Num_03} "

        if AMP == "+" and AMP_02 == "+":
            Answer = Num_03 - Num_01 - Num_02

        elif AMP  == "+" and AMP_02 == "-":
            Answer = Num_03 - Num_01 + Num_02

        elif AMP  == "-" and AMP_02 == "+":
            Answer = Num_03 + Num_01 - Num_02

        elif AMP  == "-" and AMP_02 == "-":
            Answer = Num_03 + Num_01 + Num_02
        
        Answer_02 = f"{Num_03} {sign_01} {Num_01} {sign_02} {Num_02}"
        
        
        # Calculation logic for multi-step addition and subtraction
        if AMP == "/" and AMP_02 ==  "x":
            Answer = (Num_03 / Num_02) * Num_01
            Answer_02 = f"({Num_03} {sign_01} {Num_02}) {sign_02} {Num_01}"

        elif AMP == "x" and AMP_02 == "/":
            Answer = (Num_03 / Num_01) * Num_02
            Answer_02 = f"({Num_03} {sign_01} {Num_01}) {sign_02} {Num_02}"

        elif AMP == "x" and AMP_02 ==  "x":
            Answer = Num_03 / Num_02 / Num_01

        elif AMP == "/" and AMP_02 ==  "/":
            Answer = Num_03 * Num_02 * Num_01

        # Calculation logic for multi-step addition and subtraction
        elif AMP == "-" and AMP_02 ==  "x":
            Answer = (Num_03 / Num_02) + Num_01
            Answer_02 = f"({Num_03} {sign_01} {Num_02}) {sign_02} {Num_01}"

        elif AMP == "x" and AMP_02 == "-":
            Answer = (Num_03 / Num_01) + Num_02
            Answer_02 = f"({Num_03} {sign_01} {Num_01}) {sign_02} {Num_02}"

        elif AMP == "+" and AMP_02 ==  "x":
            Answer = (Num_03 / Num_02) - Num_01
            Answer_02 = f"({Num_03} {sign_01} {Num_02}) {sign_02} {Num_01}"

        elif AMP == "x" and AMP_02 ==  "+":
            Answer = (Num_03 / Num_01) - Num_02
            Answer_02 = f"({Num_03} {sign_01} {Num_01}) {sign_02} {Num_02}"

        # Calculation logic for multi-step addition and subtraction
        elif AMP == "-" and AMP_02 ==  "/":
            Answer = (Num_03 * Num_02) + Num_01
            Answer_02 = f"({Num_03} {sign_01} {Num_02}) {sign_02} {Num_01}"

        elif AMP == "/" and AMP_02 == "-":
            Answer = (Num_03 * Num_01) + Num_02
            Answer_02 = f"({Num_03} {sign_01} {Num_01}) {sign_02} {Num_02}"

        elif AMP == "+" and AMP_02 ==  "/":
            Answer = (Num_03 * Num_02) - Num_01
            Answer_02 = f"({Num_03} {sign_01} {Num_02}) {sign_02} {Num_01}"

        elif AMP == "/" and AMP_02 ==  "+":
            Answer = (Num_03 * Num_01) - Num_02
            Answer_02 = f"({Num_03} {sign_01} {Num_01}) {sign_02} {Num_02}"
        # Template Q5: Equation with a coefficient (e.g., 2x + Num = Result)
   elif question == "Q5":
         question = f"2{XYZBC_chocie} {AMP} {Num_01} = {Num_03} "
         Answer_02 = f"({Num_03} {sign_01} {Num_01}) / 2"
         if AMP == "/":
            Answer = (Num_03 * Num_01) / 2

         elif AMP == "x":
            Answer = (Num_03 / Num_01) / 2

         elif AMP == "+":
            Answer = (Num_03 - Num_01) / 2 

         elif AMP == "-":
            Answer = (Num_03 + Num_01) / 2



    # Display the question and capture user input
   print(rounds_heading)

   if Developer == 2:
        print()
        print(f"Answer = {Answer} ")
        print(f"{sys_T_grey_TEXT}{Answer_02}{END}")
   print()
   print(question)
   user_choice = int_check(f"{XYZBC_chocie} = ",  exit_code= "xxx",low=-8000  , high=8000)
   # Logic to handle if user wants to quit early
   if user_choice == "xxx":
       print("Exit Qiez\n")
# pass/fail logic: compare user input to calculated Answer
   if user_choice == Answer:
    print("\nNice you got the anwser")
   else:
    print(f"\nyou got it wrong the answer was {Answer}")
    rounds_fail += 1

   rounds_played += 1
    # Break out of loop if exit code was entered
   if user_choice == "xxx":
       break

        # if user are in infinite mode, incrwase number of rounds.
   if mode == "Infinite":
        num_rounds += 1
        total_rounds += 1
   # Record result for game history
   if user_choice == Answer:
       feedback = f"{sys_T_green_TEXT} Pass{END}"
   else:
       feedback = f"{sys_T_red_TEXT} Fail{END}"

   print()
   history_item = f" Questions: {rounds_played} - {feedback} \t\n"
   test_history.append(history_item)
   
   # Record result for game history
   if user_choice == Answer:
          history_item = f" {question} \n"
          test_history.append(history_item)
          history_item = f" {XYZBC_chocie} = {Answer}  \n"
          test_history.append(history_item)
   else:
          history_item = f" {question} \n"
          test_history.append(history_item)
          history_item = f" You  {sys_T_grey_TEXT}|  {XYZBC_chocie} = {user_choice} |\n{END}"
          test_history.append(history_item)
          history_item = f" Answer [ {XYZBC_chocie} = {Answer} ] \n"
          test_history.append(history_item)
          history_item = f"{sys_T_grey_TEXT} {Answer_02} = {Answer} \n{END}"
          test_history.append(history_item)

        


# End-of-game statistics calculation and display
if rounds_played > 0:


    # Game History / Statistics area 
    rounds_pass = rounds_played - rounds_fail
    percent_passed = rounds_pass / rounds_played * 100
    percent_lost = rounds_fail / rounds_played * 100
    percent_tied = 100 - percent_passed - percent_lost

    clear()
    print()
    print("---Marks---")
    print(f"o Pass: {percent_passed:.2f}\t")
    print(f"o Failed: {percent_lost:.2f}\t")

   # Ask the user if they wish to view the chronological log of their rounds
    see_history = yes_no(f"\n\033[96m{BOLD}\n[?] Do you wnat to see the marks? {END}\033[0m")
    if see_history == "yes" and total_rounds == 0:
        clear()
        print(f"{sys_T_red_TEXT}{BOLD}                  YOU FAILED {END}")
        print(f"{sys_T_red_TEXT}{BOLD}          YOU DID NOT EVEN DO ANY THING {END}")
        print(f"{sys_T_red_TEXT}{BOLD}ANSWER THE QUESTIONS MABEY YOU WOULD GET SOME MARK{END}")
    elif see_history == "yes":
        for item in test_history:
            print(item)

    print()


print("num rounds: ", total_rounds)



# Game loop ends here

# Game History / Statistics area 