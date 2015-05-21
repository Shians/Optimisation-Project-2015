#!/usr/bin/env python

import pandas as pd
import numpy as np

days = 15
cities = 15

#minDays = 2
maxDays = 4
decayFactor = 0.9

baseUtility = pd.Series(data = [71.017, 92.66, 100, 77.356, 85.238, 50.707, 78.964, 87.116, 67.093, 74.819, 73.17, 77.126, 77.067, 75.922, 77.436])
travel = pd.read_csv("AirfareData15.csv", sep = ",", header = 0)
dailyMid = pd.Series(data = [92, 223, 298, 148, 169, 181, 126, 130, 145, 142, 165, 100, 85, 158, 134])
fromMelb = pd.Series(data = [1390, 1090, 1007, 1175, 1082, 1298, 1101, 1376, 1399, 1611, 1376, 1236, 1140, 1044, 1362])
toMelb = pd.Series(data = [803, 844, 875, 1061, 934, 922, 983, 921, 1033, 1186, 622, 1058, 748, 836, 1076])

names = ["Moscow", "Paris", "London", "Madrid", "Rome", "Crete", "Barcelona", "Berlin", "Budapest", "Florence", "Amsterdam", "Prague", "Istanbul", "Vienna", "Venice"]

utility = pd.Series(data = [np.nan] * cities)

for i in range(cities):
	utility[i] = baseUtility[i]

current = utility.idxmax()

cost = fromMelb[current] + dailyMid[current]
totalUtility = utility[current]
runningDays = 1

utility[current] *= decayFactor

location = list()
location.append(current)

for i in range(days - 1):
	next = utility.idxmax()

	#if (current == next or runningDays < minDays):
	if (current == next):
		cost += dailyMid[current]
		totalUtility += utility[current]
		runningDays += 1

		if (runningDays < maxDays):
			utility[current] *= decayFactor
		else:
			utility[current] = np.nan

	else:
		cost += travel.iat[current, next] + dailyMid[next]
		totalUtility += utility[next]
		runningDays = 0

		utility[current] = np.nan
		current = next

	location.append(current)

cost += toMelb[current]

print("\nTotal Cost : ${0}".format(cost))

print("Total Utility : {0}\n".format(totalUtility))

for i in range(days):
	print("Day {0} in {1}".format(i + 1, names[location[i]]))
