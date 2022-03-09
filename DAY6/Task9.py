#TASK9

#Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
li =['a', 'b', 'c']
di ={}
for ele in li:
    # Increase the value of key
    # if exists
    if ele in di:
        di[ele]= di[ele]+1
    else:
          
        # Insert the new key:value
        # pair
        di[ele]= 1
print(di)