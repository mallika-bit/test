def announce(ch):
    def wrapping2(a,b):
        #print("begin")
        result = ch(a,b)
        print(result)
        print("done")
    return wrapping2
    


 
@announce 
def  hello(a,b):
    return a+b
    
     

hello(1,2)
       