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

Error_re_send_message = []

# print the eorrer message with red colour and an [!] 
def error_sys_T(error_message, Print=None):
    """Saves errors silently if Print='no', and replays them when 're' is called."""


    # 1. If it's a new error, always save it to history first
    if error_message != "re":
        Error_re_send_message.clear()
        Error_re_send_message.append(error_message)
        
        # 2. Print immediately ONLY if Print is NOT "no"
        if Print != "no":
            print(f"\n{sys_T_red_TEXT} [!] {error_message}... {END}\n")
            
            
    # 3. If 're' is called, repeat all saved errors
    elif error_message == "re":
        for item in Error_re_send_message:
            print(f"\n{sys_T_red_TEXT} [!] {item}... {END}\n")

        Error_re_send_message.clear()
            
    

    
#--------------------------------------------------------------------------------------------------------------

# checks user enter an int / float that is
# more than a minimum (default minimum is zero)
# Allows exit code.
# Checks that the user enters a valid integer for the number of rounds.
# It also handles the "Infinite mode" trigger (empty input).
def int_check(question, low=None, high=None, exit_code=None, Infinite_mode=None,):

    while True: 
        response = input(question).lower().strip()

        if Infinite_mode == "yes":
            error_sys_T("Please enter a whole number", Print="no")
            if response == "":
                return "Infinite"
        else:
            error_sys_T("Please enter a number",Print="no")

        
        if response == exit_code:
            return response
        try:
            response = float(response)

            # If the question mode, block by a decimals manually by triggering the error
            if Infinite_mode == "yes" and response % 1 != 0:
                raise ValueError

            if low is not None and response < low:
                error_sys_T("Your number is to low please enter a higher number")
            elif high is not None and response > high:
                error_sys_T("You number is too high please enter a lower number")
            else:
                #  Clean up whole numbers (e.g., 5.0 --> 5) while leaving true decimals alone
                return int(response) if response % 1 == 0 else response

                # check for infinite mode 
        except ValueError:
            error_sys_T("re")

#--------------------------------------------------------------------------------------------------------------

# Check that users have entered a valid
# option based on a list
# Check that users have entered a valid
# option based on a list9 
# Validates that the user types 'yes' or 'no' (or 'y'/'n') and handles errors.
def string_checker(Question, EHM_All_mode=None):

    """Checks the user enter in Hard, Medium, Easy, or Enter for All"""

    while True:

        # Get input and clean it with .strip() and .lower()
        user_response = input(Question).lower().strip()
        # checks for Hard Easy mode
        if EHM_All_mode == "yes":
            Valid_responce =( sys_H_password,'all', 'a','hard','h','medium','m','easy','e','',)
            error_sys_T("Please enter Hard, Medium, Easy, or Enter for All (Enter)", Print="no")
        else:
            Valid_responce = ("yes","y" , "no", "n")
            error_sys_T("Please enter in Yes or No", Print="no")
            if user_response == "yes" or user_response == "y":
                return "yes"
            elif user_response == "no" or user_response == "n":
                return "no" 

        # 2. Check if the input exists in your valid list
        if user_response in Valid_responce:
            return user_response  # Valid. Return and exit the while loop
        else:
            #print error if user does not enter something that is vaild 
            error_sys_T("re")


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

# Clears the board and displys dimed Tile.
def DIM_Tile():
    clear()
    print(Title_02_dimed)
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
want_instructions = string_checker(" [?] Would you like to see the instructions for the Quiz? ")

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
{BOLD}All answers need to be rounded 
 to two decimal place. {END}

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


MEHM_moded = string_checker(f" [?] Would you like your test Hard, Medium, Easy, or All (Enter)? ", EHM_All_mode= "yes")

if MEHM_moded == sys_H_password :
    DIM_Tile()
    Developer = 2
    print(f"{sys_T_grey_TEXT}Hello Bhavneet ~Developer mode~{END}")


    MEHM_moded = string_checker(f" [?] Would you like your test Hard, Medium, Easy, or All (Enter)? ", EHM_All_mode= "yes")

if MEHM_moded in ["all", "a", ""]:
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
DIM_Tile()

# Asks the user if they what the answers as there doing the quiz.
Answer_showing_after_question = string_checker(f" [?] Would you like to see your answers as you are doing your quiz? ")


DIM_Tile()
    

# Ask user for number of rounds / infinite mode 
num_rounds = int_check(f"{BOLD} [?] How many questions would you like? Push <enter> for infinite mode? {END}", Infinite_mode= "yes", low=1, high=1000)

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

   swap_rules = {
        "x": "/",
        "/": "*",
        "-": "+",
        "+": "-"
    }

    # Apply the rules instantly
   sign_01 = swap_rules.get(AMP)
   sign_02 = swap_rules.get(AMP_02)

        

   # Template Q1: Basic Equation format (Variable Operator Number = Result)   
    # Template Q2: Basic Equation format (Number Operator Variable = Result)  
     # Template Q3: Equation with result as the variable (Number Operator Number = Variable)   
   if question == "Q1" or question == "Q2" or question == "Q3":
        if AMP == "/" or "x":
            equation = f"{Num_03}{sign_01}{Num_01}"
        else:
            equation =f"{Num_02}{sign_01}{Num_01}"

        Answer_02 = f"{Num_03} {sign_01} {Num_01}"
        question= f"{XYZBC_chocie} {AMP} {Num_01} = {Num_03}"

        if question == "Q2":
            Answer_02 = f"{Num_03} {sign_01} {Num_01}"
            question= f" {Num_01} {AMP} {XYZBC_chocie} = {Num_03}"
        if question == "Q3":
            Answer_02 = f"{Num_02} {AMP} {Num_01}"
            question = f" {Num_02} {AMP} {Num_01} = {XYZBC_chocie} "


        # Template Q4: Multi-step equation (Variable Op Num Op Num = Result)
   elif question == "Q4":
        # Calculation logic for multi-step addition and subtraction
        question = f"{XYZBC_chocie} {AMP} {Num_01} {AMP_02} {Num_02} = {Num_03} "
        
        equation = f"{Num_03}{sign_01}{Num_01}{sign_02}{Num_02}"
        
        Answer_02 = f"{Num_03} {sign_01} {Num_01} {sign_02} {Num_02}"
        
        
        # Calculation logic for multi-step addition and subtraction
        if AMP == "/" or "x" and AMP_02 == "x" or "/":
            if AMP == "x" and AMP_02 == "/":
                equation = f"({Num_03}{sign_01}{Num_01}){sign_02}{Num_02}"
            else:
                equation = f"({Num_03}{sign_02}{Num_01}){sign_01}{Num_02}"
            
        # Calculation logic for multi-step addition and subtraction
        # Calculation logic for multi-step addition and subtraction

        elif AMP == "-" or "+" and AMP_02 ==  "x" or "/":
            equation = f"({Num_03} {sign_02} {Num_02}) {sign_01} {Num_01}"
            Answer_02 = f"({Num_03} {sign_02} {Num_02}) {sign_01} {Num_01}"
            

        elif AMP == "x" or "/" and AMP_02 == "-" or "+":
            equation = f"({Num_03} {sign_01} {Num_02}) {sign_02} {Num_01}"
            Answer_02 = f"({Num_03} {sign_01} {Num_01}) {sign_02} {Num_02}"
           

        # Template Q5: Equation with a coefficient (e.g., 2x + Num = Result)
   elif question == "Q5":
         question = f"2{XYZBC_chocie} {AMP} {Num_01} = {Num_03} "
         Answer_02 = f"({Num_03} {sign_01} {Num_01}) / 2"
         equation = f"({Num_03}{sign_01}{Num_01}) / 2"

# solves the answer:
   Answer = eval(equation)
   Answer = round(Answer, 2)

    # Display the question and capture user input
   print(rounds_heading)

   if Developer == 2:
        print(f"\nAnswer = {Answer} ")
        print(f"{sys_T_grey_TEXT}{Answer_02}{END}\n")
   print(question)
   user_choice = int_check(f"{XYZBC_chocie} = ",  exit_code= "xxx", low=-8000  , high=8000)
   # Logic to handle if user wants to quit early
   if user_choice == "xxx":
       print("Exit Qiez\n")
# pass/fail logic: compare user input to calculated Answer

   if user_choice == Answer:
    if Answer_showing_after_question == "yes":
        print("\nNice you got the anwser")
   else:
    if Answer_showing_after_question == "yes":
        print(f"\nyou got it wrong the answer was {Answer}")
    rounds_fail += 1

   rounds_played += 1
    # Break out of loop if exit code was entered
   if user_choice == "xxx":
       rounds_played -=1
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
          history_item = f""" 
 {question} 

 {XYZBC_chocie} = {Answer}

"""
          test_history.append(history_item)
   else:
        history_item = f""" 
 {question} 

 You  {sys_T_grey_TEXT}|  {XYZBC_chocie} = {user_choice} |

 Answer [ {XYZBC_chocie} = {Answer} ] 

  {sys_T_grey_TEXT} {Answer_02} = {Answer} {END}

"""
        test_history.append(history_item)

        


# End-of-game statistics calculation and display


# Game History / Statistics area 
rounds_pass = rounds_played - rounds_fail
percent_passed = rounds_pass / rounds_played * 100
percent_lost = rounds_fail / rounds_played * 100

DIM_Tile()

print("\n---Marks---")
print(f"o Pass: {percent_passed:.2f}\t")
print(f"o Failed: {percent_lost:.2f}\t")

# Ask the user if they wish to view the chronological log of their rounds
see_history = string_checker(f"\n{BOLD}\n[?] Do you wnat to see the marks? {END}")
if see_history == "yes" and total_rounds == 0:
    clear()
    print(f"""
{sys_T_red_TEXT}{BOLD}                  YOU FAILED 
        YOU DID NOT EVEN DO ANY THING 
ANSWER THE QUESTIONS MABEY YOU WOULD GET SOME MARK{END}
""")
elif see_history == "yes":
    DIM_Tile()
    for item in test_history:
        print(item)

print(f"{BOLD}You Passed {rounds_pass} out of {rounds_played}{END}")

print(f"{BOLD}\nPercent of Pass and Failed{END}")    
print(f"- Pass: {percent_passed:.2f}\t")
print(f"- Failed: {percent_lost:.2f}\t")



# Game loop ends here

