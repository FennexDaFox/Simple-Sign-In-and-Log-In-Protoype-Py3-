from utils import wait, cls, divider
from pages import signup_page, login_page

# Configures
AppsName: str = "FENNEX.CO"

# Create the DataKey Dictionary
DataStore: dict = {}


cls()  # clear the terminal first for clean output.

while True:
    divider(36)
    print(f"\tWELCOME TO {AppsName}")
    divider(36)
    print("""Choose the number to go to the page.
      
   1.  Sign-Up
   2.  Log-In
   3.  Exit
      """)
    divider(36)

    Userpage_Input = input("Choose the page number: ")
    # print(f"User choose number: {Userpage_Input}") # Debugging

    ## Pages Shifter Logic (HardCoded)
    if Userpage_Input == "1":
        signup_page(DataStore)
    elif Userpage_Input == "2":
        login_page(DataStore)
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
