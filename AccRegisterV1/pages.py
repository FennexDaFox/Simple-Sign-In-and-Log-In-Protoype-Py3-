from utils import wait, divider, cls


# Sign-up
def signup_page(data_store):
    cls()
    divider(36)
    print("      Make a new fresh account!")
    divider(36)
    print("Type 'Back' at any prompt to return\n")

    sNameInput = input("Enter your username: \n").strip()
    if sNameInput.lower() == "back":
        cls()
        return

    if sNameInput in data_store:
        print("[FAILED] Username already taken!")
        wait(3)
        cls()
        return

    sPassInput = input("Enter your passwords: \n").strip()
    if sPassInput.lower() == "back":
        cls()
        return

    if sNameInput not in data_store:
        data_store[sNameInput] = sPassInput

    if sNameInput in data_store:
        print("[SUCCESS] Account registered successfully!")
    wait(3)
    cls()


# Log-in
def login_page(data_store):
    cls()
    divider(36)
    print("      Already have an account?")
    divider(36)
    print("Type 'Back' at any prompt to return\n")

    lNameInput = input("Enter your username: \n").strip()
    if lNameInput.lower() == "back":
        cls()
        return

    lPassInput = input("Enter your passwords: \n").strip()
    if lPassInput.lower() == "back":
        cls()
        return

    if lNameInput in data_store and lPassInput == data_store[lNameInput]:
        print(f"[SUCCESS] Welcome aboard captain! {lNameInput}")
    else:
        print(
            "[FAILED] Unavaiable to get into your's account! \n Usual reason: \n Wrong username \n Wrong passwords \n Account didnt exist \n Data Corrupted"
        )

    wait(3)
    cls()
