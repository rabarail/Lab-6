"""Program name: User login system
Author: Rajani Baraili
Purpose: simulates a user login using dictionary to store usernames and passwords.
Starter code: None
Date:02/18/2026"""

users = {
    "guest": "guest",
    "rajani": "password1",
    "sana": "twice",
    "gwalters": "S3curePass!",
    "user1": "password2"
}

username = input("Enter username: ")
if username not in users:
    print("Username not found. Exiting.")

else:
    
    attempts = 0
    while attempts < 3:
        password = input("Enter password: ")
        if password == users[username]:
            if username == "guest":
                print("Welcome, guest! You have Guest access.")
            else:
                print("Welcome, " + username + ". You have Security Level 1.")
            break
        else:
            attempts += 1
            if attempts < 3:
                print("Incorrect password. Please try again.")
            else:
                print("Access Denied.")
                

           






