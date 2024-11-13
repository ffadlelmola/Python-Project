"""A pizza simulation that outputs a summary of that days's profits, inventory,
most popular toppings, revenue, and a line graph showing, if given 7 class
instances, 7 days' worth of profits. 
"""
from argparse import ArgumentParser
import sys
import re
import matplotlib.pyplot as plt

TOPPINGS_INVENTORY= {
  'olives': 10,
  'sausages':2,
  'mushrooms':10,  
  'ham': 10,
  'spinach':10,
  'cheese':10,
  'chicken':10,
  'onions': 10,
}
pizzaSizeCosts= {
"S": 5.99,
"M": 7.99, 
"L":9.99,
}

pizzaSizeRetail = {
"S": 2.00,
"M": 3.50,
"L": 4.00,   
}
    
class Shop:
    """Creates the Pizza Shop.
    
    Attributes:
        filepath (str): a path to a text file containg customer orders that
        includes the size of the pizza and a list of toppings
        inventory (dict): a dictionary containing the name of the toppings
        available and the number of each topping as a serving size available 
        orders (dict): an order number 
        order_num (int): the current order number 
        total (float): the total profit
        revenue (float): the total revenue
    """    
    def __init__(self, filepath):
        """Reads a text file containing all of the customer orders for a 
        particular day and adds them to a dictionary cont

        Args:
            filepath (str): a text file that contains customer information 
            including the size of pizza and the toppings on the pizza

        Raises:
            TypeError: When the line of the text file does not match the regular
            expression, the order can't be processed. 
        """        
        self.filepath = filepath
        self.inventory = TOPPINGS_INVENTORY 
        self.orders = {}
        self.order_num = 1
        self.total = 0
        self.revenue = 0
        pattern = r"""(?x)^(?P<Pizza_Size>[MLS]),\s*(?P<Toppings>(?:\w+,)*\w+)
        (?:,\s*)?$"""
           
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f: 
                match = re.match(pattern,line)
                if match:
                    size = match.group('Pizza_Size')
                    Toppings = tuple(match.group('Toppings').split(','))
                    self.orders[self.order_num] = (size, Toppings) 
                    self.order_num +=1  
                else:
                    raise TypeError
          

    def getProfit(self):
        """Iterates through orders to determine the daily profit.
        
        Returns:
            total (float): total profit from the day.
        """
        for order in self.orders.values():
            p = pizzaSizeRetail[order[0]] + (0.25 * len(order[1])) if \
                (len(order[1]) > 0) else (p == pizzaSizeRetail[order[0]])
            self.total += p
        return self.total 
    
    
    def updateInventory(self):
        """Updates invetory for the shop.

        Returns:
            inventory(dict): the inventory of the store. 
        """        
        for order in self.orders.values():
            topping_list = order[1] 
            for j in topping_list:
                if j in self.inventory and self.inventory[j] > 1:
                    self.inventory[j]-=1        
        return self.inventory
         
         
    def get_popular_topping(self):
        """Returns the most popular topping from the list of orders
            
        Returns:
            sorted_toppings (list of tuples): a list of toppings in a tuple 
            with the number of times they were ordered. 
        """    
        topping_counts = {}
        for order in self.orders.values():
            topping_list = order[1]
            for topping in topping_list:
                if topping in topping_counts:
                    topping_counts[topping] += 1
                else:
                    topping_counts[topping]=1
                    
        self.sorted_toppings = sorted(topping_counts.items(), key=lambda x: 
            x[1], reverse=True)
        return self.sorted_toppings[0][0] 
    
           
    def getGross(self):
        """Calculates the gross revenue of the Pizza Shop for a particular day.

        Returns:
            revenue (float): the total revenue of the day
        """
        for order in self.orders.values():
            topping_list = order[1]
            pizza_size= order[0]
            for item in topping_list:
                self.revenue += 1
            if pizza_size == "S":
                self.revenue += 5.99
            elif pizza_size == "M":
                self.revenue += 7.99
            else:
                self.revenue += 9.99
        self.revenue += self.order_num  
        self.revenue = round(self.revenue, 2)
        return self.revenue
    
    
    def __str__(self):
        """string magic method

        Returns:
            f-string: an f-string that shows a daily summary of all statistics 
            calculated within the Pizza Shop
        """        
        return f"""Summary:
    Daily Revenue: ${self.revenue}
    Daily Profit: ${self.total}
    New Inventory: {self.inventory}
    Most Popular Toppings: {self.sorted_toppings}
    """


def main(filepath, path1=None, path2=None, path3=None, path4=None, path5=None,
         path6=None): 
    """Instantiates the Shop class for up to 7 different days of operation and
    runs all methods within the class. If there is 7 instances of the class
    given in the command line, then it displays a pyplot line graph of the 
    profit over the 7 day period. 

    Args:
        filepath (str): a text file containing customer's order info that
        includes the size of the pizza and the toppings.
        path1 (str, optional): a text file containing customer's order info that
        includes the size of the pizza and the toppings. Defaults to None.
        path2 (str, optional): a text file containing customer's order info that
        includes the size of the pizza and the toppings. Defaults to None.
        path3 (str, optional): a text file containing customer's order info that
        includes the size of the pizza and the toppings. Defaults to None.
        path4 (str, optional): a text file containing customer's order info that
        includes the size of the pizza and the toppings.Defaults to None.
        path5 (str, optional): a text file containing customer's order info that
        includes the size of the pizza and the toppings. Defaults to None.
        path6 (str, optional): a text file containing customer's order info that
        includes the size of the pizza and the toppings. Defaults to None.
    
    Side Effects:
        Writes to stdout a summary of statistics and a pyplot of profit of 7
        instances of the class. 
    """    
    newPizzaShop = Shop(filepath)
    dailyprofit = newPizzaShop.getProfit()
    newPizzaShop.get_popular_topping()
    newPizzaShop.getGross()
    newPizzaShop.updateInventory()
    print(str(newPizzaShop))
    if path1 is not None:
        newPizzaShop1 = Shop(path1)
        dailyprofit1 = newPizzaShop1.getProfit()
        newPizzaShop1.get_popular_topping()
        newPizzaShop1.getGross()
        newPizzaShop1.updateInventory()
        print(str(newPizzaShop1))
    if path2 is not None:
        newPizzaShop2 = Shop(path2)
        dailyprofit2 = newPizzaShop2.getProfit()
        newPizzaShop2.get_popular_topping()
        newPizzaShop2.getGross()
        newPizzaShop2.updateInventory()
        print(str(newPizzaShop2))
    if path3 is not None:
        newPizzaShop3 = Shop(path3)
        dailyprofit3 = newPizzaShop3.getProfit()
        newPizzaShop3.get_popular_topping()
        newPizzaShop3.getGross()
        newPizzaShop3.updateInventory()
        print(str(newPizzaShop3))
    if path4 is not None:
        newPizzaShop4 = Shop(path4)
        dailyprofit4 = newPizzaShop4.getProfit()
        newPizzaShop4.get_popular_topping()
        newPizzaShop4.getGross()
        newPizzaShop4.updateInventory()
        print(str(newPizzaShop4))
    if path5 is not None:
        newPizzaShop5 = Shop(path5)
        dailyprofit5 = newPizzaShop5.getProfit()
        newPizzaShop5.get_popular_topping()
        newPizzaShop5.getGross()
        newPizzaShop5.updateInventory()
        print(str(newPizzaShop5))
    if path6 is not None:
        newPizzaShop6 = Shop(path6)
        dailyprofit6 = newPizzaShop6.getProfit()
        newPizzaShop6.get_popular_topping()
        newPizzaShop6.getGross()
        newPizzaShop6.updateInventory()
        print(str(newPizzaShop6))
    if (path1 is not None and path2 is not None and path3 is not None and
        path4 is not None and path5 is not None and path6 is not None):
        profitlist= [dailyprofit, dailyprofit1, dailyprofit2, dailyprofit3, 
                 dailyprofit4, dailyprofit5, dailyprofit6]
        plt.plot([1,2,3,4,5,6,7], profitlist)
        plt.xlabel('Days')
        plt.ylabel('Profit in Dollars')
        plt.title("Pizza Shop Profit over 7 days")
        plt.show()   


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file that
    contains all orders for a Pizza Shop on a given day 
    Six optional command line arguments: 
        -d2, --day2: if specificed, a path to a text file that contains all
        orders for a Pizza Shop on a given day
        -d3, --day3: if specificed, a path to a text file that contains all
        orders for a Pizza Shop on a given day
        -d4, --day4: if specificed, a path to a text file that contains all
        orders for a Pizza Shop on a given day
        -d5, --day5: if specificed, a path to a text file that contains all
        orders for a Pizza Shop on a given day
        -d6, --day6: if specificed, a path to a text file that contains all
        orders for a Pizza Shop on a given day
        -d7, --day7: if specificed, a path to a text file that contains all
        orders for a Pizza Shop on a given day

    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """    
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to text file")
    parser.add_argument("-d2", "--day2", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-d3", "--day3", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-d4", "--day4", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-d5", "--day5", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-d6", "--day6", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-d7", "--day7", type=str, default=None,
                        help="path for a new text file of a new day")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.filepath, args.day2, args.day3, args.day4, args.day5, 
         args.day6, args.day7)