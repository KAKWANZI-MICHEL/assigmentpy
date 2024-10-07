#QN1 the volume of the sphere with radius r is (4/3)*pie* r**2.
# what is the volume of a sphere with radius 5
# make sure that the program enters the radius from the keyboard and provide the answer in 2 decimal places
# radius= float(input("Enter the radius"))
# pie = 22/7
# volume= (4/3)*pie*(radius**2)
# print(f"the volume of the sphere is {volume:.2f}")

radius = float(input("Enter the radius: "))
pie = 22/7
volume = (4/3) * pie * (radius ** 3)
print(f"The volume of the sphere is {volume:.2f}")


# #QN2 create a programm to calculate the area of a triangle (1/2*base*height).
# # base and height should be entered using the keyboard
# base= float(input("Enter the base of the triangle: "))
# height= float(input("Enter the height of the triangle: "))
# area= (1/2)*base*height
# print(f"The area of the triangle is {area} ")

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (1/2) * base * height
print(f"The area of the triangle is {area:.2f}")

#QN3 
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail  
mark = int(input("Enter the mark: "))
if 90 <= mark <= 100:
    print("grade is A")
elif 80 <= mark < 90:
    print("grade is B")
elif 70 <= mark < 80:
    print("grade is C")
elif 60 <= mark < 70:
    print("grade is D")
elif 50 <= mark < 60:
    print("grade is E ")
else:
    print("fail")
        

# QN4. WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.
class WITIAcademySacco:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 1000:
            print("Minimum deposit is 1000.")
            return
        self.balance += amount
        print(f"Successfully deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 500:
            print("Minimum withdrawal is 500.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Successfully withdrew {amount}. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


def main():
    sacco = WITIAcademySacco()
    print("Welcome to WITI Academy Sacco.")

    while True:
        print("\nPlease choose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            sacco.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            sacco.withdraw(amount)
        elif choice == '3':
            sacco.check_balance()
        elif choice == '4':
            print("Thank you for using WITI Academy Sacco. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()