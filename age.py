from datetime import date

def calculateAge(born):
	try:
		today = date.today()
		try:
			birthday = born.replace(year = today.year)

		except ValueError:
			birthday = born.replace(
				year = today.year,
				month = born.month + 1,
				day = 1
				)

		if birthday > today:
			return today.year - born.year - 1
"""
		elif birthday <= 0:
			print("You can't be that young :D")
"""

		else:
			return today.year - born.year
	except:
		print("Something that did not expected went wrong, run the program again !")
while True:
	yıl = int(input("Year : "))
	ay = int(input("Month : "))
	gün = int(input("Day : "))


	print(calculateAge(date(yıl,ay,gün)),"years")