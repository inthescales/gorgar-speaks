import getopt
import sys

from src.gorgarspeaks import speak

import botbuddy

def generate_speech():
    return speak()

def test_with_count(count):
    print("")
    for i in range(0, count):
        print(generate_speech())
        print("")

# Process command line input

if __name__ == '__main__' and len(sys.argv) > 0:
    
    mode = None
    count = None
    
    # Error cases
    def error_mode_conflict():
        print("> Error: can only select one mode from test or publish")
        sys.exit(1)
    
    # Get args
    try:
        opts, params = getopt.getopt(sys.argv[1:], "tpc:k:", ["test", "publish", "count="])
    except getopt.GetoptError:
        print('gorgar.py --publish')
        sys.exit(2)

    # Process args
    for opt, arg in opts:
        
        if opt in ["-t", "--test"]:
            if mode != None:
                error_mode_conflict()
            mode = "test"
        elif opt in ["-p", "--publish"]:
            if mode != None:
                error_mode_conflict()
            mode = "publish"
        elif opt in ["-c", "--count"]:
            count = int(arg)
    
    # Assign defaults
    
    if mode == None:
        print("> Defaulting to test mode")
        mode = "test"
        
    if mode == "test" and count == None:
        print("> Defaulting to count 1")
        count = 1

    # Perform action
        
    if mode == "publish":
        botbuddy.post(generate_speech)
    elif mode == "test":
        test_with_count(count)
            
        print("")
