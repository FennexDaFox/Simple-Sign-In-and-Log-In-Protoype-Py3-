from utils import wait, cls, divider

# Configures
AppsName: str = "FENNEX.CO"

# Create the DataKey Dictionary
DataStore: dict = {}


## Pages
# Sign-up
def signup_page():
    cls()
    divider()
    print("      Make a new fresh account!")
    divider()
    print("Type 'Back' at any prompt to return\n")

    sNameInput = input("Enter your username: \n").strip()
    if sNameInput.lower() == "back":
        cls()
        return

    sPassInput = input("Enter your passwords: \n").strip()
    if sPassInput.lower() == "back":
        cls()
        return

    DataStore[sNameInput] = sPassInput

if sNameInput in DataStore:
    print("[FAILED] Username already taken!")
else:
    DataStore[sNameInput] = sPassInput

    wait(3)
    cls()


# Log-in
def login_page():
    cls()
    divider()
    print("      Already have an account?")
    divider()
    print("Type 'Back' at any prompt to return\n")

    lNameInput = input("Enter your username: \n").strip()
    if lNameInput.lower() == "back":
        cls()
        return

    lPassInput = input("Enter your passwords: \n").strip()
    if lPassInput.lower() == "back":
        cls()
        return

    if lNameInput in DataStore and lPassInput == DataStore[lNameInput]:
        print(f"[SUCCESS] Welcome aboard captain! {lNameInput}")
    else:
        print(
            "[FAILED] Unavaiable to get into your's account! \n Usual reason: \n Wrong username \n Wrong passwords \n Account didnt exist \n Data Corrupted"
        )

    wait(3)
    cls()


cls()  # clear the terminal first for clean output.

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
        cls()
        print("Thanks for using our service.")
        wait(2)
        cls()
        break
    else:
        print("Wrong number/pages error. Pls try again later")
        wait(1.5)
        cls()
