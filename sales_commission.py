# Customer data retrieved from the system
#customer_name = "Carlos Silva"
#product_name = "Data Science Bootcamp"
#amount_due = 150.00
#days_overdue = 5

# Creating a dynamic message using an f-string
#email_message = f"Hello, {customer_name}! We noticed that your payment for '{product_name}' (Amount: ${amount_due:.2f}) is {days_overdue} days overdue. Please update your payment status."

#print(email_message)

# Daily revenue from Monday to Friday
#daily_sales = [12000.00, 8500.00, 14000.00, 9100.00, 11000.00]
#weekly_goal = 50000.00

# Summing up all values in the list
#total_revenue = sum(daily_sales)

#print(f"Total Revenue: ${total_revenue:.2f}")

# Making a decision based on the performance
#if total_revenue >= weekly_goal:
    #print("Congratulations! The team achieved the weekly goal.")
#else:
    #print("Alert: Goal not reached. We need an action plan to recover sales.")

# 1. Employee data (Feel free to change values for testing)
employee_name = input("Enter employee name: ")
base_salary = 2500.00
closed_deals = [float(x) for x in input("Enter closed deals amounts separated by commas: ").split(',')]

# 2. Total sales calculation
total_sales = sum(closed_deals)

# 3. Commission calculation (10% of total sales)
commission_rate = 0.10

# Commission is only given if total sales exceed $20,000.00
if total_sales >= 20000.00:
    commission = total_sales * commission_rate
    print(f"Success! {employee_name} hit the sales target.")
else:
    commission = 0.00
    print(f"{employee_name} did not hit the sales target.")

# 4. Final payout calculation
final_payout = base_salary + commission

print(f"Final Payout for {employee_name}: ${final_payout:.2f}")