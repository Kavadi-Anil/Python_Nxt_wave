mutable
-----------
a+=1 is compuding 
a=a+1 is not compunding

def increment(list_z):
    list_z=list_z+[1] 
    print(list_z) 
list_z=[1,2]    
increment(list_z)  
print(list_z) 
#ouput   
[1, 2, 1]
[1, 2]




