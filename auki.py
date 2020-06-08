import time
import sys
import turtle
import random
username = input("Username?")
sysKey = input("Save Code? Put N/A for new game.")
keyGenSuccess = "Success"
keyGenFailure = "Failure"
if sysKey == "N/A":
    print("Save key generation:", keyGenFailure)
    print("Debug mode initialized")
    time.sleep(1)
    username = "username"
    print("username reset")
    command = input("Please input command.  Else put none to continue.  Halt to end program.")
    if command == "Halt":
        sys.exit()
    elif command == "none":
        print("Program begin")
        time.sleep(1)
    elif command == "Finish":
        print("Congratulations!  You delivered to the right house!")
        print("Game end process")
    elif command == "Secret":
        haha = 420
        #This is secret.

else:
    print("Key loading failure. Reason: No checkpoint found matching that key.  Is the capitalization correct?")