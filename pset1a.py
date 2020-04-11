# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:55:25 2020

@author: mnm
"""


total_cost = float(input('enter the price of the house...'))
down_payment = total_cost /4
annual_salary = float(input('enter your annual salary...'))
monthly_salary = annual_salary/12
portion_salary = monthly_salary*float(input('enter the monthly portion of your salary to be saved...'))
current_savings = 0
monthly_investment = 0
months = 1

while current_savings < down_payment:
    current_savings += portion_salary    
    monthly_investment = current_savings *0.04/12    
    current_savings += monthly_investment   
    months +=1
    
print(f'you need to save money for {months} months')    
    