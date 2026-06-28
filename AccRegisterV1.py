import os
import time

# Variable
AppsName: str = "FENNEX.CO"

DataStore: dict = {}  # Create the DataKey Dictionary


# Funcs
def clr_Terminal():  # easily spam clear the terminal XD
    os.system("cls" if os.name == "nt" else "clear")


def divider():  # make a devider using "=" and multiply it with 36
    print("=" * 36)


## Pages
# Sign-up
def signup_page():
    clr_Terminal()
    divider()
    print("      Make a new fresh account!")
    divider()
    print("Type 'Back' at any prompt to return\n")

    sNameInput = input("Enter your username: \n").strip()
    if sNameInput.lower() == "back":
        clr_Terminal()
        return

    sPassInput = input("Enter your passwords: \n").strip()
    if sPassInput.lower() == "back":
        clr_Terminal()
        return

    DataStore[sNameInput] = sPassInput

    if sNameInput in DataStore:
        print("[SUCCESS] Your account has been registered!")
    else:
        print("[FAILED] Unavaiable to register your account! \n Usual reason: \n Username Taken \n Data Corrupted")

    time.sleep(3)
    clr_Terminal()


# Log-in
def login_page():
    clr_Terminal()
    divider()
    print("      Already have an account?")
    divider()
    print("Type 'Back' at any prompt to return\n")

    lNameInput = input("Enter your username: \n").strip()
    if lNameInput.lower() == "back":
        clr_Terminal()
        return

    lPassInput = input("Enter your passwords: \n").strip()
    if lPassInput.lower() == "back":
        clr_Terminal()
        return

    if lNameInput in DataStore and lPassInput == DataStore[lNameInput]:
        print(f"[SUCCESS] Welcome aboard captain! {lNameInput}")
    else:
        print(
            "[FAILED] Unavaiable to get into your account! \n Usual reason: \n Wrong username \n Wrong passwords \n Account didnt exist \n Data Corrupted"
        )

    time.sleep(3)
    clr_Terminal()


clr_Terminal()  # clear the terminal first for clean output.

while True:
    divider()
    print(f"\tWELCOME TO {AppsName}")
    divider()
    print("""Choose the number to go to the page.
      
   1.  Sign-Up
   2.  Log-In
   3.  Exit
      """)
    divider()

    Userpage_Input = input("Choose the page number: ")
    # print(f"User choose number: {Userpage_Input}") # Debugging

    ## Pages Shifter Logic (HardCoded)
    if Userpage_Input == "1":
        signup_page()
    elif Userpage_Input == "2":
        login_page()
    elif Userpage_Input == "3":
        print("Thanks for using our service.")
        time.sleep(2)
        clr_Terminal()
        break
    else:
        print("Wrong number/pages error. Pls try again later")
        time.sleep(1.5)
        clr_Terminal()
