import random, sys, time, os, math
# make text bold 
BOLD = '\033[1m'
END = '\033[0m'

# Checks that the user enters a valid integer for the number of rounds.
# It also handles the "Infinite mode" trigger (empty input).
def int_check_Q(Question):
    while True:

        error = "\n\033[91m  [!] Please enter an integer that is 1 or more. \033[0m\n"

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

# Making text bold and adds colour too
BOLD = '\033[1m'
END = '\033[0m'


 # loading bar before clearing the bord.
print(f"{BOLD}     -SYSTEM STATUS-{END}")

for i in range(11):
    b = '█'*i + '░'*(10-i)
    print(f'\rProgress: [{b}] {i*10}%', end=''); time.sleep(0.1)


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

#---------------------------------------------------------------

# checks user enter an int / float that is
# more than a minimum (default minimum is zero)
# Allows exit code.
def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = f"\n\033[91m [!] Please enter an integer more than 0\033[0m\n"


    elif low is not None and high is None:
        error = (f"\n\033[91m [!] Please enter an integer that is{END}"
                 f"\033[91m more than / equal to {low}...{END}\n")

    else:
        error = (f"\n\033[91m [!] Please enter an integer that{END}"
                 f"\033[91m is between {low} and {high} (inclusive{END}\n")

    while True:
        response = input(question).lower()
        # Checks if the user wants to quit using the exit code
        if response == exit_code:
            return response
        

        try:
            response = int(response)
            # Validates that input is within the specified low/high range
            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)
#---------------------------------------------------------------

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
#---------------------------------------------------------------

# Prints the instruction header for the user.
def instructions():
    """gives instructions"""

    print("""
=============================   
   **** Instructions ****            
=============================        
    """)
#---------------------------------------------------------------


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
item_question = [
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5"
]


# List to track the results of each round for the end-game summary.
test_history = []



# Main Routine Starts Here 

# Initialize tracking variables for the game state and statistics.
mode = "REGULAR"
rounds_played = 0
rounds_fail = 0 
total_rounds = 0

# Instuctions 

# Ask user for number of rounds / infinite mode 
num_rounds = int_check_Q("\n\033[96m  [?] How many rounds would you like? Push <enter> for infinite mode: \033[0m")

# Game Loop starts here 

# Set infinite mode flags if necessary.
if num_rounds == "Infinite":
    mode = "Infinite"
    num_rounds = 5

 
# Test Loop ends here
# Primary Test Loop: runs until the specified number of rounds is reached.
while rounds_played < num_rounds:
   # Display round number and mode type to the user.
   if mode == "Infinite":
       rounds_heading = f"\n{BOLD} Round {rounds_played +1}{END} (Infinite Mode) \n"
   else:
       rounds_heading = f"\n{BOLD} Round {rounds_played + 1} of {num_rounds} {END}\n"
    # Randomize numbers and operators for the current round's equation.
   Num_01 = random.randrange(1,10)
   Num_02 = random.randrange(1,10)
   Num_03 = Num_01 * Num_02
   AMP = random.choice(AMP_item)
   AMP_02 = random.choice(AMP_item)
   question = random.choice(item_question)
   XYZBC_chocie = random.choice(items)
   # Template Q1: Basic Equation format (Variable Operator Number = Result)        
   if question == "Q1":
        if AMP == "/":
            Answer = Num_03 * Num_01

        if AMP == "x":
            Answer = Num_03 / Num_01

        if AMP == "+":
            Answer = Num_03 - Num_01

        if AMP == "-":
            Answer = Num_03 + Num_01
        question= f"{XYZBC_chocie} {AMP} {Num_01} = {Num_03}"
        # Template Q2: Basic Equation format (Number Operator Variable = Result)
   elif question == "Q2":
        if AMP == "/":
            Answer = Num_03 * Num_01

        if AMP == "x":
            Answer = Num_03 / Num_01

        if AMP == "+":
            Answer = Num_03 - Num_01

        if AMP == "-":
            Answer = Num_03 + Num_01
        question= f" {Num_01} {AMP} {XYZBC_chocie} = {Num_03}"
        # Template Q3: Equation with result as the variable (Number Operator Number = Variable)
   elif question == "Q3":

        if AMP == "x":
            Answer = Num_02 * Num_01

        if AMP == "+":
            Answer = Num_02 + Num_01

        if AMP == "-":
            Answer = Num_02 - Num_01

        question = f" {Num_02} {AMP} {Num_01} = {XYZBC_chocie} "
    # Logic for division in Template Q3
   elif question and AMP == "Q3" and "/":
        if AMP == "/":
            Answer = Num_03 / Num_01

        question = f" {Num_01} {AMP} {Num_03} = {XYZBC_chocie} "
        # Template Q4: Multi-step equation (Variable Op Num Op Num = Result)
   elif question == "Q4":
        # Calculation logic for multi-step addition and subtraction
        question = f"{XYZBC_chocie} {AMP} {Num_01} {AMP_02} {Num_02} = {Num_03} "
        if AMP == "+" and AMP_02 == "-":
            Answer = Num_03 - Num_01 + Num_02

        if AMP  == "-" and AMP_02 == "+":
            Answer = Num_03 + Num_01 - Num_02

        if AMP  == "-" and AMP_02 == "-":
            Answer = Num_03 + Num_01 + Num_02

        if AMP  == "-" and AMP_02 == "-":
            Answer = Num_03 - Num_01 - Num_02
        
        # Calculation logic for multi-step addition and subtraction
        if AMP == "/" and AMP_02 ==  "x":
            Answer = Num_03 / Num_02 * Num_01

        if AMP == "x" and AMP_02 == "/":
            Answer = Num_02 / Num_01 * Num_02

        if AMP == "x" and AMP_02 ==  "x":
            Answer = Num_03 / Num_02 / Num_01

        if AMP == "/" and AMP_02 ==  "/":
            Answer = Num_03 * Num_02 * Num_01

        # Calculation logic for multi-step addition and subtraction
        if AMP == "-" and AMP_02 ==  "x":
            Answer = Num_03 / Num_02 + Num_01

        if AMP == "x" and AMP_02 == "-":
            Answer = Num_03 / Num_01 + Num_02

        if AMP == "+" and AMP_02 ==  "x":
            Answer = Num_03 / Num_02 - Num_01

        if AMP == "x" and AMP_02 ==  "+":
            Answer = Num_03 / Num_01 - Num_02

        # Calculation logic for multi-step addition and subtraction
        if AMP == "-" and AMP_02 ==  "/":
            Answer = Num_03 * Num_02 + Num_01

        if AMP == "/" and AMP_02 == "-":
            Answer = Num_02 * Num_01 + Num_02

        if AMP == "+" and AMP_02 ==  "/":
            Answer = Num_03 * Num_02 - Num_01

        if AMP == "/" and AMP_02 ==  "+":
            Answer = Num_03 * Num_01 - Num_02
        # Template Q5: Equation with a coefficient (e.g., 2x + Num = Result)
   elif question == "Q5":
         question = f"2{XYZBC_chocie} {AMP} {Num_01} = {Num_03} "
         if AMP == "/":
            Answer = Num_03 * Num_01 / 2

         if AMP == "x":
            Answer = Num_03 / Num_01 / 2

         if AMP == "+":
            Answer = Num_03 - Num_01 / 2 

         if AMP == "-":
            Answer = Num_03 + Num_01 / 2



    # Display the question and capture user input
   print(rounds_heading)
   print()
   print(question)
   user_choice = int_check(f"{XYZBC_chocie} = ",  exit_code= "xxx")
   # Logic to handle if user wants to quit early
   if user_choice == "xxx":
       print("Exit Qiez\n")
# pass/fail logic: compare user input to calculated Answer
   if user_choice == Answer:
    print("\nNice you got the anser")
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
       feedback = "You Pass"
   else:
       feedback = "You Fail"

   print()
   history_item = f" Rounds: {rounds_played} - {feedback} \t"
   test_history.append(history_item)
# End-of-game statistics calculation and display
if rounds_played > 0:

    # Game History / Statistics area 
    rounds_won = rounds_played - rounds_fail
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_fail / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    print()
    print("---Marks---")
    print(f"o Pass: {percent_won:.2f}\t")
    print(f"o Failed: {percent_lost:.2f}\t")

   # Ask the user if they wish to view the chronological log of their rounds
    see_history = yes_no(f"\n\033[96m{BOLD}\n[?] Do you wnat to see all your questions? {END}\033[0m")
    if see_history == "yes":
        for item in test_history:
            print(item)

    print()


print("num rounds: ", total_rounds)



# Game loop ends here sdewjruewoipurower29-84395832opri kewop

# Game History / Statistics area 