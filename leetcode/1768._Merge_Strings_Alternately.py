# Backend
class Solution:
    def mergeAlternately(self,word1: str, word2: str) -> str:
        merged = []
        max_length = max(len(word1),len(word2))
        for i in range(max_length):
            
            if i < len(word1):
                merged.append(word1[i])            
            if i < len(word2):
                merged.append(word2[i])
                
        value = "".join(merged)
        value = value.replace(" ","")
        return value

# Frontend
print("\n###Merge Strings Alternately###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        word1=input("\nenter word 1 to me merged:")
        word2=input("enter word 2 to me merged:")
        if len(word1) >= 1 and len(word2) <= 100:
            value = Solution.mergeAlternately(0,word1,word2)
            print(f"\nThe Merged word is: {value}")
        else:
            print("INVALID INPUT: No of Words is not in Range")
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")
