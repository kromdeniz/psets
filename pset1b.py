# -*- coding: utf-8 -*-







total_cost = float(input('enter the price of the house:'))
down_payment = total_cost /4
annual_salary = float(input('enter your annual salary:'))
monthly_salary = annual_salary/12
portion_percent = float(input('enter the monthly portion of your salary to be saved:'))
current_savings = 0
monthly_investment = 0
months = 1
demi_raise = float(input('enter your raise:'))

while current_savings < down_payment:
    if months%6==0:
        annual_salary+= annual_salary*demi_raise
    portion_salary = annual_salary*portion_percent/12
    current_savings += portion_salary    
    monthly_investment = current_savings *0.04/12    
    current_savings += monthly_investment   
    months +=1
    
        
        
print(f'you need to save money for {months} months')    
    