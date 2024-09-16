prompt = input("Expression: ")
x,y,z=prompt.split(" ")
def operacoes(x,y,z):
    if y=="+":
        print("{:.1f}".format(float(x+y)))
    elif y=="-":
         print("{:.1f}".format(float(x-y)))
    elif y=="*":
        rint("{:.1f}".format(float(x*y)))
    elif y=="/":
        rint("{:.1f}".format(float(x/y)))