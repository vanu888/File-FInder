import os
import sys
import platform
import subprocess


def run_again ():
    run = str(input("Do you want to find something again (y/n): "))
    if run == "y":
        program()
    elif run == "n":
        sys.exit
    else: 
        print("Please, restart the program!")

def program():

    #Get input for directory path
    #or you can use the permanent directory path 
    dir_path = str(input("Enter directory path here: "))
    directory = dir_path

    #Get input for file that want to find (Enter filename with file type)
    filename = input("Enter the filename to search for: ")

    file_path = os.path.join(directory, filename)

    if os.path.exists(file_path):
        print(f"File '{filename}' found in the specified directory.")
    
        if platform.system() == "Windows":
            os.startfile(file_path)
            run_again()
        else:
            subprocess.Popen(["xdg-open", file_path])
            run_again()
    else:
        print(f"File '{filename}' not found in the specified directory.")
        run_again()

print ("Welcome!")
print ("Hi, you can use this program to find files whose paths you don't remember. ")
program()
