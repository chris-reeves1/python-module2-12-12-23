def getIncomeTax(salery):
    if salery < 11850:
        return 0
    elif 11850 <= salery <= 34500:
        return (salery - 11850) * 0.2
    elif 34501 <= salery <= 150000:
        return 4530 + ((salery - 34500) * 0.4)
    else:
        return 50370 + ((salery - 150000) * 0.45)
    
salery = 100000
tax_amount = getIncomeTax(salery)

print("tax amount for salery £{} is £{}".format(salery, tax_amount))