def search(arr,a_size,to_find):
    for i in range(0,a_size):
        if(arr[i]==to_find):
            return i
    return 1

print("\nWelcome to the code of linear search on array\n")
exit=False
arr=[]
while exit==False:
    try:
        x=int(input("Enter an int value in array:\t"))
        arr.append(x)
        exist=(input("Press 'e' to exit and 'c' to continue:\t"))
        if exist.lower()=='e':
            exit=True
        else:
            print("\n")
    except:
        print("\nYou have entered a non-integer value.")
print(f"Array data that you have entered: {arr}")
to_find=int(input("\nEnter integer value to find in array that you have provided:\t "))        
a_size=len(arr)
index=search(arr,a_size,to_find)
if index!=1:
    print(f"The element is present at index {index} in the array i.e {arr}")
else:
    print(f"Element not found in the array {arr}")