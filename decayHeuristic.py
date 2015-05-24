#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import numpy as np
import collections as c

names = ["Moscow","Paris","London","Madrid","Rome","Crete","Barcelona","Berlin","Budapest","Florence","Amsterdam","Prague","Istanbul","Vienna","Venice"]

fromMelb = [1390,1090,1007,1175,1082,1298,1101,1376,1399,1611,1376,1236,1140,1044,1362]
returnMelb = [2311,1909,1908,1870,2135,2757,1900,1890,1831,2779,1839,1832,1760,2076,1837]

travel = np.matrix([[0,146,126,202,146,168,143,156,207,291,154,146,115,131,129]
,[227,0,60,143,93,123,139,110,162,85,52,165,150,140,68]
,[213,82,0,249,160,284,135,107,163,224,124,171,197,179,152]
,[188,86,136,0,144,188,69,70,96,138,103,124,180,143,119]
,[223,80,125,146,0,177,39,96,69,84,94,94,74,105,71]
,[233,81,223,188,58,0,131,123,58,241,200,114,120,164,169]
,[200,121,79,76,32,165,0,143,108,103,90,110,141,103,74]
,[130,53,81,97,83,153,110,0,83,214,92,123,99,176,104]
,[249,133,125,96,41,123,96,76,0,164,157,113,50,149,97]
,[309,246,162,172,86,301,90,186,204,0,227,155,279,229,150]
,[155,158,73,141,136,211,117,106,125,229,0,85,121,155,95]
,[112,122,100,112,48,193,116,108,138,144,97,0,85,152,65]
,[123,101,127,154,67,173,122,86,41,235,66,108,0,59,65]
,[145,162,122,202,90,75,145,117,175,171,90,181,121,0,194]
,[167,65,17,117,84,191,97,119,110,152,75,96,177,152,0]])

baseUtility = [71.017, 92.66, 100, 77.356, 85.238, 50.707, 78.964, 87.116, 67.093, 74.819, 73.17, 77.126, 77.067, 75.922, 77.436]

dailyMid = [92, 223, 298, 148, 169, 181, 126, 130, 145, 142, 165, 100, 85, 158, 134]

DecayRate = 0.92

Utility = np.matrix([[x * DecayRate ** (n+1) for n in range(15)] for x in baseUtility])

Trip = []*15

totalUtility = 0

ct = c.Counter()

i = 15
while i > 0:
	currentUtility = [Utility[n, ct[n]] for n in range(15)]
	bestCity = currentUtility.index(max(currentUtility))
	if i > 1
		if ct[bestCity] > 0
			totalUtility += currentUtility[bestCity]
			ct[bestCity] += 1
		elif ct[bestCity] == 0
			totalUtility += currentUtility[bestCity]
			ct[bestCity] += 1

			currentUtility = [Utility[n, ct[n]] for n in range(15)]
			totalUtility += currentUtility[bestCity]
			ct[bestCity] += 1
	elif i == 1:
		currentUtility = [Utility[n, ct[n]] for n in ct.values()]

citiesList = [x[0] for x in  ct.items()]
totalCost = 0
travelPlan = []

costList = [fromMelb[c] for c in citiesList]
cheapest = costList.index(min(costList))
travelPlan.append(citiesList[cheapest])
del citiesList[cheapest]

while len(citiesList) > 0:
	currentCity = travelPlan[0]
	costList = [travel[currentCity, c] for c in citiesList]
	cheapest = costList.index(min(costList))
	travelPlan.append(citiesList[cheapest])
	del citiesList[cheapest]

totalCost += fromMelb[travelPlan[0]]
totalCost += returnMelb[travelPlan[-1]]
for c in travelPlan:
	totalCost += ct[c] * dailyMid[c]

for i in travelPlan:
	print "Go to %s for %d days." % (names[i], ct[i])

print "Total Cost: $%d" % totalCost
print "Total Utility: %.3f" % totalUtility