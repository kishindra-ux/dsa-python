# Backend
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)

# Frontend
print("\n###is Subsequence###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        t=input("\nenter word:")
        s=input("enter sbusequence:")
        print(Solution.isSubsequence(0,s,t))
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")

