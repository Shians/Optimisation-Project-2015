#Takes user input for criteria rating and writes to userInput.txt file

A = []
criteria = ["Beaches", "History", "Art Galleries/Museums", "Architecture", "Nightlife", "Food", "Sport", "Theatre/Entertainment"]

budget = input('Enter your budget: ')
days = input('Enter the number of days you would like to travel: ')

print('Rate the following categories out of 10.')
for crit in criteria:
	x = (input('%s: ' %crit))
	while x not in range(11):
		print 'Please enter a number between 0 and 10.'
		x = (input('%s: ' %crit))
	A.append(x)


f = open('userInput.txt', 'w')
f.write('budget: %s\n\n' %budget)
f.write('days: %s\n\n' %days)
f.write('criteriaRating: [')
for item in A:
	f.write('%s, ' %item)
f.write(']\n\n')
f.close()

print ('Data written to userInput.txt')