#purpose: this programmes calculate savings amd return savings with interest

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly income: "))

#the calculations of savings

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#projected savings in one yewr with interset included

print("Your monthly savings are: ", monthly_savings)
print("Projected savings after one year, with interest, is: ",projected_savings)