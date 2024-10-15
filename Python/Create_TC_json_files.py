"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Create all the .json files needed to perform TC 
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

import os
import json

json_file = r'C:\Users\emart429\Desktop\SOMEIP_Tool\ICS_254_methods\v2ControlMode_ARM_Id255_p255_UPDATE.json' # .json base file used to create all the other methods
d = {} #Empty dictionary to add values into

def print_json_file():
    print("-----------get keys and values from dict----------------")
    with open(json_file, 'r') as fh:
        json_data = json.load(fh)
    
    for key, value in json_data.items():
        print(key, ": ", type(key), value, ": ", type(value))
        for key2, value2 in value.items():
            print(key2, ": ", value2, "  ")
    
    
def create_json_files():
    with open(json_file, 'r') as fh:
        json_data = json.load(fh)
    
    #___________ Create 254 method .json files ___________
    start = 1
    stop = 256
    step = 1
    for i in range(start, stop, step):
        #___________ Replace priority value ___________
        json_data["3"]["value"] = str(i)
        print(json_data["3"]["value"])
        
        #___________ Create method file ___________
        ## method_name = "__m" + str(i) + "__.json"
        method_name = "v2ControlMode_ARM_Id255____p" + str(i) + "____UPDATE" + ".json"
        method_file = os.path.join(os.path.dirname(json_file), method_name)
        with open(method_file, 'w') as f:
            json.dump(json_data, f, indent=4)
        
        #___________ Create method directory ___________
        d[i] = str(method_file)
        
    #___________ Create method dictionary file ___________
    dictionary_file = os.path.join(os.path.dirname(json_file), "method_dictionary.txt")
    with open(dictionary_file, 'w') as f:
        f.write(json.dumps(d))
        
        
        
if __name__ == "__main__":
    create_json_files()
    