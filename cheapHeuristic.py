#!/usr/bin/env python

import pandas as pd
import numpy as np

days = 15
cities = 15
maxDays = 4
decayFactor = 0.98

baseUtility = pd.Series(data = [71.017, 92.66, 100, 77.356, 85.238, 50.707, 78.964, 87.116, 67.093, 74.819, 73.17, 77.126, 77.067, 75.922, 77.436])
travel = pd.read_csv("AirfareData15.csv", sep = ",", header = 0)
dailyMid = pd.Series(data = [92, 223, 298, 148, 169, 181, 126, 130, 145, 142, 165, 100, 85, 158, 134])
fromMelb = pd.Series(data = [1390, 1090, 1007, 1175, 1082, 1298, 1101, 1376, 1399, 1611, 1376, 1236, 1140, 1044, 1362])
toMelb = pd.Series(data = [803, 844, 875, 1061, 934, 922, 983, 921, 1033, 1186, 622, 1058, 748, 836, 1076])

names = ["Moscow", "Paris", "London", "Madrid", "Rome", "Crete", "Barcelona", "Berlin", "Budapest", "Florence", "Amsterdam", "Prague", "Istanbul", "Vienna", "Venice"]

utility = baseUtility
totalUtility = 0

options = pd.Series(data = [np.nan] * cities)

for i in range(cities):
	options[i] = fromMelb[i] + maxDays * dailyMid[i]

current = options.idxmin()

cost = options[current]
daysLeft = days - maxDays

location = list()

for i in range(maxDays):
	location.append(current)

	totalUtility += utility[current]
	utility[current] *= decayFactor

while (daysLeft > 0):
	step = min(maxDays, daysLeft)

	for i in range(cities):
		if (i not in location):
			options[i] = travel.iat[current, i] + step * dailyMid[i]
		else:
			options[i] = np.nan

	current = options.idxmin()

	cost += options[current]
	daysLeft -= step

	for i in range(step):
		location.append(current)

		totalUtility += utility[current]
		utility[current] *= decayFactor

cost += toMelb[current]

print("\nTotal Cost : ${0}".format(cost))

print("Total Utility : {0}\n".format(totalUtility))

for i in range(days):
	print("Day {0:2d} in {1}".format(i + 1, names[location[i]]))
