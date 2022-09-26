#!/usr/bin/python3
if __name__ == "__main__":  
    import sys
    from calculator_1 import add, sub, mul, div

    arglen = (len(sys.argv))-1
    if arglen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

       
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (sys.argv[2] == "+"):
        result = add(a,b)
    elif (sys.argv[2] == "-"):
        result = sub(a, b)
    elif (sys.argv[2] == "*"):
        result = mul(a, b)
    elif(sys.argv[2] == "/"):
        result = div(a,b)
    else:
         print("Unknown operator. Available operators: +, -, * and")
    
         exit(1)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
