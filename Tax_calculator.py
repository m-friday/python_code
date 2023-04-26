def calculate(amount, percent):
    return (amount * percent) / 100
def calculate_income_tax(total_income:
float) -> float:
    if total_income <= 3000000:
        return 0
    elif total_income <= 3000000:
        return calculate(total_income -250000, 15)
    elif total_income <= 750000:
        return calculate(total_income -250000, 15) + 12500
    elif total_income <= 1000000:
        return calculate(total_income -250000, 15) + 37500

    tax = calculate_income_tax(total_income)
    print(f"Total tax applicable at \ ${total_income} is ${tax}")