#!/usr/bin/env python
import sys


data = open("restaurants.csv", "r")
lines = data.readlines()
restaurant_name = []
restaurant_time = []
restaurant_food = []
restaurant_waittime = []


for line in lines:
    info = line.rstrip().split(",")
    restaurant_name.append(info[1])
    restaurant_time.append(info[2])
    restaurant_food.append(info[3])
    restaurant_waittime.append(info[4])


def close_restaurants():
    for i in range(1, len(restaurant_name)):
        if restaurant_waittime[i] == "Three" or "Four":
            print restaurant_name[i], "is only ", restaurant_time[i], " minutes away"


def fast_restaurant():
    for i in range(1, len(restaurant_waittime)):
        if restaurant_waittime[i] == "Low":
            print restaurant_name[i], "has a low estimated wait time"


def choose_food():
    n = raw_input("Enter a food category: ")
    for i in range (1, len(restaurant_food)):
        if restaurant_food[i] == n:
            print "These restaurants: ", restaurant_name[i], "have ", restaurant_food[i]

def choose_restaurant():
    n = raw_input("Enter a restaurant name: ")
    for i in range (1, len(restaurant_name)):
        if restaurant_name[i] == n:
            print "There is a ", restaurant_name[i], restaurant_time[i], " minutes away from you "


def most_common_food(restaurant_food):
    restaurant_food = []
    for row in range(0, restaurant_food):
        if restaurant_food[i] not in restaurant_food:
            food_list.append(restaurant_food[i])

    food_counts = []
    for food in food_list:
        total = 0
        for restaurant_food in restaurant_food:
            if restaurant_food == food:
                total += 1

        food_counts.append(total)

    return max(food_counts)

print " "
print "My Final Project"
print " "
print close_restaurants
print " "
print fast_restaurant
print " "
print choose_food
print " "
print choose_restaurant
print " "
print most_common_food
print " " 