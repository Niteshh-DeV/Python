def calculate_tip():
    print("Welcome to the Tip Calculator!")
    
    while True:
        try:
            total_bill = float(input("\nEnter the total bill amount: $"))
            tip_percentage = int(input("Enter the tip percentage you'd like to give (e.g., 10, 15, 20): "))
            num_people = int(input("How many people are splitting the bill? "))
            
            # Calculate the total amount and per-person cost
            tip_amount = (tip_percentage / 100) * total_bill
            total_amount = total_bill + tip_amount
            per_person = total_amount / num_people
            
            print(f"\nTip amount: ${tip_amount:.2f}")
            print(f"Total bill (with tip): ${total_amount:.2f}")
            print(f"Each person pays: ${per_person:.2f}")
            
            if input("\nWould you like to calculate another bill? (yes/no): ").lower() != "yes":
                print("Thank you for using the Tip Calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_tip()