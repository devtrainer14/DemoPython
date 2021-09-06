x = int(input("enter number"))
def drawboard(x):
    
    i = 0
    ho = " ---"
    ve = "|   "
    ho = ho * x
    ve = ve * (x+1)
    while i < x+1:
        print (ho)
        if not (i == x):
            print (ve)
        i += 1

drawboard(x)
