"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Open, configure and work with SOME/IP Tool to send 254 methods
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

import pyautogui
import time
import os
import json

secs_between_keys = 0.001
    
def open_someip_tool():
    #___________ Start SOME/IP Tool application ___________
    os.startfile(r'C:\Users\emart429\Desktop\SOMEIP_Tool\SOME-IP_9\SOME-IP\SOMEIPCore_Tool.exe')
    time.sleep(10)
    
    
def configure_someip_tool():
    #___________ Endpoints configuration ___________
    pyautogui.typewrite('local_addr=10.1.0.3 local_port=0 service_addr=10.1.0.50 service_port=16000 SD_timeout=5', interval=secs_between_keys)
    time.sleep(0.5)
    pyautogui.press('enter') 
    time.sleep(1.5)
    
    #___________ Timing configuration ___________    
    pyautogui.press('enter') 
    time.sleep(1.5)
 
    #___________ Subscribe to IntrusionInclinationService ___________    
    pyautogui.typewrite('s')
    pyautogui.press('enter') 
    time.sleep(0.5)
    pyautogui.typewrite('847 1 4 1', interval=secs_between_keys)
    pyautogui.press('enter') 
    time.sleep(6) 


#def method_dict(num):
#    switch={
#        1: r"C:\Users\emart429\Desktop\SOMEIP_Tool\ICS_254_methods\v2ControlMode_ARM_Id255_p255_UPDATE.json",
#        2: r"C:\Users\emart429\Desktop\SOMEIP_Tool\ICS_254_methods\v2ControlMode_ARM_Id255_p254_UPDATE.json"
#    }
#    return switch.get(num, "Method path not found") 


def method_dict(n):
    #___________ Switch to "n" method ___________  
    dict_dir= r"C:\Users\emart429\Desktop\SOMEIP_Tool\ICS_254_methods\method_dictionary.txt"
    with open(dict_dir, 'r') as dict_file:
        dict_data = json.load(dict_file)
    return dict_data[str(n)]


def iterate_through_methods():
    #___________ Send methods with SOME/IP Tool ___________  
    for i in range(253):
        time.sleep(3)
        #___________ Switch to next method ___________  
        mPath = method_dict(255-i)
        
        #___________ Send method with SOME/IP Tool ___________  
        pyautogui.typewrite('m', interval=secs_between_keys)
        pyautogui.press('enter') 
        time.sleep(.5) 
           
        pyautogui.typewrite("847 9 4 ", interval=secs_between_keys)
        pyautogui.typewrite(mPath)
        pyautogui.press('enter')
       
        
        
if __name__ == "__main__":
    open_someip_tool()
    configure_someip_tool()
    iterate_through_methods()
