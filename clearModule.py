from os import system
from sys import stdout

cls = lambda: system("cls")

print = stdout.write

def makeRequirementsTxt():
    system("pip3 freeze -> requirements.txt")

def notified():
    cls()
    makeRequirementsTxt()
    print("The followings are the modules will be uninstalled\n")
    with open("requirements.txt") as o:
        r = o.readline()
        print(r.split("==")[0]+"\n")
    print("\n")
    system("pause")

def confirm():
    cls()
    Input = input("confirm uninstall (Y/N)")
    if Input.casefold() in ["y", "yes", "1"]: return True
    elif Input.casefold() in ["n", "no" , "0"]: return False
    else:
        raise ValueError("InputError")

def main():
    makeRequirementsTxt()
    notified()
    if confirm():
        system("pip3 uninstall -r requirements.txt")
        print("uninstall successed")
    else:
        print("cancel uninstall")
    system("del requirements.txt")

if __name__ == "__main__":
    main()