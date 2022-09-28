import sys
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    index = len(sys.argv)-1

    print(f"{index} arguments") 

    for i in range(len(sys.argv)-1):
        print(f"{i+1}:{sys.argv[i+1]}")
