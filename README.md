# INST326 Final Project
## Pizza Shop Simulation 

A simulation that represents a pizza shop and different aspects, calculations, and analysis of the shop. The simulation would be based on the perspective of the shop owner. The simulation will go over the different aspects of owning a pizza shop like customers every day, profit calculation, stock calculation, common toppings, prices, and the cost of stock. The user can input up to 7 text files within the command line arguments to be able to see how the shop is doing over 7 days. This will result in a daily summary of the information above and prompt the user to change these items if they want to. The daily summary will display the profit made on that day, the total number of customers, and the leftover inventory based on servings. Also, if 7 days are inputed, a pyplot will display and show the profit trend over the last 7 days. 
#  

## Purpose of Files

__customers1.txt to customers7.txt__ - these text files list the information about the customers so that the program can have data to use that is inputted by the user

__finalproject.py__ - this runs the analysis of the Pizza Shop including the creation of the pyplot, the total revenue of the shop on a specific day, the profit of the shop on a specific day, the popular topping of the day, and the amount of stock of toppings at the end of the day (in terms of serving).
#   

## Table of Attribution

| Method/Function    |Primary Author  | Techniques Demonstrated|
| -------------------| -------------- | ----------------------:|
| main               |Claire Knorr    |   optional parameters  |
| ```__init__ ```    |Fatma Fadlelmoda|   Regular Expressions  |
| parse_args         |Andy Yang       |  ArgumentParser class  |
|``` __str__ ```     |Claire Knorr    |    magic methods       |
| get_popular_topping|Fatma Fadlelmoda| use of a key function  |
| getProfit          |Andy Yang       | conditional expression |
#  

## Command Line Arguments

To get a single day summary:

```
python finalproject.py customers1.txt
```

To get multiple days of the simulation:

```
python finalproject.py customers1.txt -d2 customers2.txt -d3 customers3.txt -d4 customers4.txt -d5 customers5.txt -d6 customers6.txt -d7 customers7.txt
```
#  
## How to Interpret Results

This program outputs a string representation of the major statisitcs that a Pizza Shop would need to know in order to operate a successful business for the number of days that you input into the program. However, if you input 7 days, a line graph of the profit is shown to highlight which days were better than others so that more analysis can be done with the printed information like looking into topping population and inventory. 