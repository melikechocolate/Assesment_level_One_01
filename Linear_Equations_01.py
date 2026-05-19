import math, random, os, sys, time 

# sys text and user face
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

# make text bold and adds colour too
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

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)
#---------------------------------------------------------------

# Checks for yes or no or gives error
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

#defines intstruction and imports intstraution
def instructions():
    """gives instructions"""

    print("""
=============================   
   **** Instructions ****            
=============================        
    """)
#---------------------------------------------------------------

# Varbles: 

# Tilite one not dimed
Title_01 = f"""

        ***Quiz***
    ====================
      Linear Equations
    ====================
"""
#tile two deimed.
Title_02_dimed = f"""{sys_T_grey_TEXT}

        ***Quiz***
    ====================
      Linear Equations
    ====================
{END}
"""
#---------------------------------------------------------------

#tile 
print(Title_01)

# main rountine here

Num_01 = random.randrange(1,10)
Num_02 = random.randrange(1,10)
Num_03 = Num_01 * Num_02


AMP_item = [
    "-",
    "x",
    "+",
    "/"
]

AMP = random.choice(AMP_item)

items = [
   "a",
   "b",
   "c",
   "𝑥",
   "y",
   "z",
   "m"
]

XYZBC_chocie = random.choice(items)

item_question = [
    "Q1",
    "Q2",
    "Q3"
]

    # f"{XYZBC_chocie} {AMP} {Num_01} = {Num_03}",
    # f"{XYZBC_chocie} {AMP} {Num_01} {AMP} {Num_01} = {Num_03}"   

question = random.choice(item_question)



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
elif question == "Q3":

    if AMP == "x":
        Answer = Num_02 * Num_01

    if AMP == "+":
        Answer = Num_02 + Num_01

    if AMP == "-":
        Answer = Num_02 - Num_01
    question = f" {Num_01} {AMP} {Num_02} = {XYZBC_chocie} "
elif question and AMP == "Q3" and "/":
    if AMP == "/":
        Answer = Num_03 / Num_01
    question = f" {Num_01} {AMP} {Num_03} = {XYZBC_chocie} "

print(question)

user_answer = int_check(f"{XYZBC_chocie} = ")


# else:
#         if AMP == "/":
#          Answer = Num_03 * Num_01 * Num_01

#         if AMP == "+":
#           Answer = Num_03 / Num_01 / Num_01

#         if AMP == "+":
#          Answer = Num_03 - Num_01 - Num_01

#         if AMP == "-":
#          Answer = Num_03 + Num_01 + Num_01



if user_answer == Answer:
    print("\nNice you got the anser")
else:
    print(f"\nyou got it wrong the answer was {Answer}")

