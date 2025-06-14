# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPounds) tuples
    fruitShops: List of FruitShops
    Returns the FruitShop where the order costs the least amount.
    """
    bestShop = None
    lowestCost = float('inf') 

    for shop in fruitShops:
        cost = shop.getPriceOfOrder(orderList)
        if cost < lowestCost:
            lowestCost = cost
            bestShop = shop
            
    return bestShop

