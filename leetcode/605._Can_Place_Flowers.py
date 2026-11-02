# Backend
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                        
        return n <= 0

# Frontend 
print("\n###canPlaceFlowers###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        raw_input = input("\nEnter all Flowerbed separated by spaces (e.g., 1 0 0 0 1): ")
        n = int(input("no of Flowerbed has to be free to place flowers:"))
        flowerbed = [int(x) for x in raw_input.split()]
        value = Solution.canPlaceFlowers(0, flowerbed, n)
        print(f"\ncan Place Flowers is: {value}")
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")
