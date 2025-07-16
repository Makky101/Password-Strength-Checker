# Password Strength Checker
def check_password(password):

    # Rule 1: Check if password is at least 8 characters
    if len(password) < 8:
        return "Weak! Password must be at least 8 characters."
        
    
    # Rule 2: Check if it has at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return f"Weak! Add at least one uppercase letter to (like A, B, C)."
        

    # Rule 3: Check if it has at least one number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    if not has_number:
        return "Weak! Add at least one number to (e.g 1, 2, 3,)."

    # if all rules pass, it's strong!
    return "Strong password! Good job!"

stored_passwords = []

while True:
    print("====Password Strength Checker====")
    print("Enter a password to verify the strength of that password")
    print("You can also view recent tested passwords")

    password = input("Enter a password: ")
    stored_passwords.append(password)
    result = check_password(password)
    print(result)

    # Get tested passwords
    view = input("Do you want to view tested passwords (y/n): ").strip().lower()
    if view not in ("y", "n"):
        print(f"Enter y(yes) or n(no) and not {view}")
        continue

    if view == "y":
        if not stored_passwords:
            print("You have no saved recent passwords tested.")
        else:
            for t, views in enumerate(stored_passwords, 1):
                print(f"{t}. {views}")

    # Retry
    retry = input("Do you want to test again (y/n): ").strip().lower()
    if retry not in ("y", "n"):
        print(f"Enter y(yes) or n(no) and not {retry}")
        continue
    if retry == "n":
        break