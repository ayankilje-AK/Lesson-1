def total_calc(bill_amount, tip_percentage):
    total_calc = bill_amount*(1+0.01*tip_percentage)
    total_calc = round(total_calc, 2)
    print(f"You have to pay ${total_calc}")    
total_calc(150,20)

