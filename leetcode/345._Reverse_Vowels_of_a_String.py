#Backend
class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s=list(s)
        vowele=("a","e","i","o","u","A","E","I","O","U")
        index=[]
        value=[]
        i=0
        for val in s:
            if val in vowele:
                index.append(i)
                value.append(val)
            i+=1   
        for index in index:
            list_s[index]=value.pop()
            
        return"".join(list_s)

#Frontend
print("\n###Greatest Common Divisor of Strings###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        s=input("Enter to Reverse Vowels of a String:")
        if len(s) >=1 and len(s) <= 3 * 105:
            Sol = Solution.reverseVowels(0,s)
            print(f"\nThe Reverse Vowels of a String: {Sol}")
        else:
            print("INVALID INPUT: No of String is not in Range")
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")

