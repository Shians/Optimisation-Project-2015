#!/usr/bin/env python

import pandas as pd
import numpy as np

days = 15
cities = 15
maxDays = 4

travel = pd.read_csv("AirfareData15.csv", sep = ",", header = 0)
dailyMid = pd.Series(data = [92, 223, 298, 148, 169, 181, 126, 130, 145, 142, 165, 100, 85, 158, 134])
fromMelb = pd.Series(data = [1390, 1090, 1007, 1175, 1082, 1298, 1101, 1376, 1399, 1611, 1376, 1236, 1140, 1044, 1362])
toMelb = pd.Series(data = [803, 844, 875, 1061, 934, 922, 983, 921, 1033, 1186, 622, 1058, 748, 836, 1076])

names = ["Moscow", "Paris", "London", "Madrid", "Rome", "Crete", "Barcelona", "Berlin", "Budapest", "Florence", "Amsterdam", "Prague", "Istanbul", "Vienna", "Venice"]

options = pd.Series(data = [np.nan] * cities)

for i in range(cities):
	options[i] = fromMelb[i] + maxDays * dailyMid[i]

current = options.idxmin()

cost = options[current]
daysLeft = days - maxDays

location = list()

for i in range(maxDays):
	location.append(current)

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

cost += toMelb[current]

print("\nTotal Cost : ${0}\n".format(cost))

for i in range(days):
	print("Day {0} in {1}".format(i + 1, names[location[i]]))
