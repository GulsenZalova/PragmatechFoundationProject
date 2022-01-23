x = input("Daxil et: ")

try:
    if type(eval(x)) == int:
        print(x, "number")    
    elif type(eval(x)) == bool:
        print(x, " boolean")      
except:
    print("string")