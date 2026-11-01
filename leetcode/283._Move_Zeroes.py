# Backend
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        return nums

# Frontend 
print("\n###moveZeroes###")

while True:
    print()
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "1":
        nums=[]
        n=int(input("\nenter no of value in list to enter:"))
        for i in range(1,n+1):
            num=int(input(f"enter value {i}:"))
            nums.append(num)
        value = Solution.moveZeroes(0, nums)
        print(f"\n The move Zeroes is: {value}")
    elif program_run == "2":
        print("\nThank you for using the program, Have a great day!")
        break
    else:
        print("Invalid input. Please type 1 or 2.")
