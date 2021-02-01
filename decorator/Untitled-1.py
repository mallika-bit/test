def t(s):
    def ti(x,y):
        print("confirm")
        r = s(x,y)
        print(r)

    return ti

    

    

@t
def tr(x,y):
    return x+y

tr("hello","world")