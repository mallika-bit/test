def f(x):
    
    def g(y):
        
        print(f"x value{x} y value{y}")
        return( y + x + 3) 
    return(g)




nf1 = f(2)
nf2 = f(3)


print(nf1(1))
print(nf2(2))