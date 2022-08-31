l = int(input ("Please, Enter the Lowest Range Value: "))  
u= int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for e in range (l,u+1):  
    if e > 1:  
        for i in range (2, e):  
            if (e % i) == 0:  
                break  
        else:  
            print (e,end=" ")  