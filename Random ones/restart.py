import os

restart=input("Do you want to restart your PC:  ")
if restart=="no":
    exit()

elif restart=="yes":
    os.system("shutdown /r /t 1")

else:
    print("Invalid response!")