# Backend
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_alt = 0
        max_alt = 0
        for i in gain:
            current_alt += i
            max_alt = max(max_alt, current_alt)       
        return max_alt

# Frontend 
print("\n###largestAltitude###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        raw_input = input("\nEnter all Altitude separated by spaces (e.g.,-5,1,5,0,-7): ")
        gain = [int(x) for x in raw_input.split()]
        value = Solution.largestAltitude(0, gain)
        print(f"\ncan Place Flowers is: {value}")
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")
