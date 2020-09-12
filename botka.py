from pynput.keyboard import Key, Controller
import time 
import os 

os.system("clear")

print (''' \033[0;36m 
                    _           _       _    _ 
                   | |__   ___ | |_ ___| | _(_)
                   | '_ \ / _ \| __/ __| |/ / |
                   | |_) | (_) | |_\__ \   <| |
                   |_.__/ \___/ \__|___/_|\_\_|
                                       
                                          \033[0;37m  By Ahmed Saoud @ Mal4D
                                          
                                          
                                          

''')





kb = Controller()


print("\033[0;33m[+] Oeration Has Benn Started !!!! \n")

print("\033[0;33m[i] Please Click In Window FaceBook !!\n ")

while True : 
    time.sleep(2)
    kb.press("j")
    kb.release("j")
    
    kb.press("l")
    kb.release("l")
    
    kb.press(Key.enter)
    kb.release(Key.enter)
    
    time.sleep(2)
