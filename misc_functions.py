import sys,subprocess
import time

# a function to check the user OS then implements correct command to clear terminal
def clear_screen():
    os = sys.platform
    if os == 'win32':
        subprocess.run('cls', shell=True)
    elif os == 'linux' or os == 'darwin':
        subprocess.run('clear', shell=True)


# This function prints a fancy message (looks like the output is being typed) 
# args: msg_txt = input txt msg_length is the amount of time displayed on screen and not the length of chars
def fancy_message(msg_txt,msg_length):
    clear_screen()
    input_string = msg_txt
    output_txt = ""
    for character in input_string:
        clear_screen()
        output_txt += character
        print(output_txt)
        time.sleep(0.1)
    time.sleep(msg_length)

#This function clears the terminal and displays a message
# args: msg_txt = input txt msg_length is the amount of time displayed on screen and not the length of chars
def message(msg_txt,msg_length):
    clear_screen()
    print(msg_txt)
    time.sleep(msg_length)

