# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:23:51 2019

@author: degte
"""
#=================Homework 1====================

class Portfolio():
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.stocks = []

#        self.funds = funds
    
    def __add__(self, cash):
        self.cash + cash
        print ("The total ammount of your cash after adding is")
        return self.cash + cash
    
    
    def __sub__(self, cash):
        print ("The total ammount of your cash after substracting is")
        return self.cash - cash

#    def history_show (self):
#        if stock.buy_stock():
#            print (stock.buy_stock())
#        elif stock.sell_stock():
#            print (stock.sell_stock())
#        elif fund.buy_fund():
#            print(fund.buy_fund())
#        else fund.sell_fund()
#            print(fund.sell_fund())
#    
  
class Stock():
    def __init__(self, name, price, ammount):
        self.name = name 
        self.price = price
        self.ammount = ammount
    
    def buy_stock (self, name, portfolio, price, ammount):
        self.portfolio = Portfolio
        self.name = name
        if type(ammount) != int:
            raise TypeError("Use the a price that in range 0.5X-1.5X.")
        else: 
            print ("You bought %s stock.The ammount of stocks is %d. You spend %d of cash. Your balance is %d."
                       % (self.name, ammount, (ammount*price), (self.cash - ammount*price)))
    
    def sell_stock (self, name, portfolio, price, ammount):
        self.name = name
        self.portfolio = Portfolio
        if type(ammount) != int:
            raise TypeError("Use the whole numbers of stocks to buy.")
        elif price != [0.5*self.price, 1.5*self.price]:
            raise TypeError("Use the a price that in range 0.5X-1.5X.")
        else: 
            print ("You sold %s stock. The ammount of stocks is %d. You received %d of cash. Your balance is %d."
                       % (self.name, ammount, (ammount*price), (self.cash + ammount*price)))

class Fund():
    def __init__(self, name, price, ammount):
        self.name = name 
        self.price = price
        self.ammount = ammount
    
    def buy_fund (self, name, portfolio, price, ammount):
        self.portfolio = Portfolio
        self.name = name
        print ("You bought %s fund.The ammount of funds is %d. You spend %d of cash. Your balance is %d."
                       % (self.name, ammount, (ammount*price), (self.cash - ammount*price)))
    
    def sell_fund (self, name, portfolio, price, ammount):
        self.name = name
        self.portfolio = Portfolio
        if price != [0.9*self.price, 1.2*self.price]:
            raise TypeError("Use the a price that in range 0.9X-1.2X.")
        else: 
            print ("You sold %s fund. The ammount of funds is %d. You received %d of cash. Your balance is %d."
                       % (self.name, ammount, (ammount*price), (self.cash + ammount*price)))  

