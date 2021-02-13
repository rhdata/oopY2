

class Library:

	def __init__(self, listofArticles):
		self.availablearticles = listofArticles

	def displayarticle(self):
		print()
		print("Available articles : ")
		for article in self.availablearticles:
			print(article)

	def lendArticle(self, requestedArticle):
		if requestedArticle in self.availablearticles:
			print("you have now consulted the article")
			self.availablearticles.remove(requestedArticle)
		else:
			print("sorry the article is not available")

	def addArticle(self, returnedArticle):
		self.availablearticles.append(returnedArticle)
		print("you have returned the article, Thanks")

class Customer:

	def requestArticle(self):
		print("Enter the name of an article you want to read : ")
		self.article = input()
		return self.article

	def returnArticle(self):
		print("Enter the name of the article which you are returning : ")
		self.article = input()
		return self.article		

library = Library(['les RH et les normes','industrie 4.0','RSE et RH','organisation et management','le travail et les 35h','employabilité','management des competences'])
customer = Customer()

while True:

	print("Enter 1 to display available articles")
	print("Enter 2 to request for a book")
	print("Enter 3 to return an article")
	print("Enter 4 to exit")
	userChoice = int(input())
	if userChoice is 1:
		library.displayarticle()
	elif userChoice is 2:
		requestedArticle = customer.requestArticle()
		library.lendArticle(requestedArticle)
	elif userChoice is 3:
		returnedArticle = customer.returnArticle()
		library.addArticle(returnedArticle)
	elif userChoice is 4:
		quit()