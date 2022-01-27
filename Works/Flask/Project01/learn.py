def myFunction(): print("__name__deyeri evezlenir-"+ __name__)
def main(): myFunction()
if __name__=="__main__": main()

def inc(x):
    return x+1
def dec(x):
    return x-1
def calculate(func,x):
    result=func(x)
    return result
calculate(inc, 5)