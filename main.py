from pathlib import Path
import os

def readfileandfolder():
    path = Path('') # current file path
    items = list(path.rglob('*')) # recursive globe
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)
            print(f"File Created succefully")
        else:
            print("this file already exist")
    except Exception as e:
        print(f"An Error occured {e}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)

            print("Readed Successfully")
        else:
            print("the file doesnot exist")

    except Exception as e:
        print(f"An Error occured {e}")

def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overighting the data of your file")
            print("Press 3 for appending some content in your file")

            res = int(input("tell your response: "))

            if res == 1:
                name2 = input("tell your new name of file: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwrite the data: ")
                    fs.write(data)
            
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append: ")
                    fs.write(""+data)

    except Exception as e:
        print(f"An Exception occured {e}")

def deletefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file removes successfully")
        else:
            print("No such file exist")
    except Exception as e:
        print(f"An Exception occured {e}")
    


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("please tell tour response: "))

if check == 1:
    createfile()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()

elif check == 4:
    deletefile()

else:
    print("Press only below:\n")
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deletion a file")
    