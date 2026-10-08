class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        gcd=gcd(len(str1),len(str2))
        if len(str1) >= 1 and len(str2) <=100:
            if str1.upper() + str2.upper() != str2.upper() + str1.upper():
                return ""
            else:
                return str1[:gcd]
     
# Frontend
print("\n###Greatest Common Divisor of Strings###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        str1=input("\nenter repeated string 1:")
        str2=input("enter repeated string 2:")
        if len(str1) >= 1 and len(str2) <= 100:
            value = Solution.gcdOfStrings(0,str1,str2)
            print(f"\nThe Greatest Common Divisor of Strings: {value}")
        else:
            print("INVALID INPUT: No of String is not in Range")
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")
