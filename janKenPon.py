import random 

class Choices:
	def __init__(self):
		self.lists = ["Rock", "Paper", "Scissors"]

	def defWinner(self, num):
		try:
			return{
			1 : "Human",
			2 : "Bot",
			3 : "Draw",
			}[num]
		except Exception as e:
			return "Out of bound@"

	def choices(self,num):
		try:
			return{
			1 : "Rock", 
			2 : "Paper",
			3 : "Scissors",
			}[num]
		except Exception as e:
			return "Out of bound!"


class Bot:
	def randomizeBotChoice(self):
		return random.randint(1, 3)

class ScoreBoardAndRound:
	def __init__(self):
		self.scoreHuman = 0
		self.scoreBot = 0
		self.Round = 1
		self.roundByBot = 0
		self.roundByHuman = 0
		self.result = []
		self.winnerRound = []

	def addWinnerRound(self, who):
		self.winnerRound.append(who)

	def addResultRound(self, who):
		self.result.append(who)

	def addHumanScore(self):
		self.scoreHuman += 1

	def addBotScore(self):
		self.scoreBot += 1

	def resetAllInStart(self):
		self.__init__()

	def addRound(self):
		self.Round += 1

	def resetScoreToNextRound(self):
		self.scoreHuman = 0
		self.scoreBot = 0
		self.addRound()

	def compareToWin(self, one, two):
		if(one == 1):
			if(two == 1):
				return 3
			elif(two == 3):
				return 1
			elif(two == 2):
				return 1
		elif(one == 2):
			if(two == 2):
				return 3
			elif(two == 3):
				return 2
			elif(two == 1):
				return 2
		elif(one == 3):
			if(two == 3):
				return 3
			elif(two == 2):
				return 1
			elif(two == 1):
				return 2

	def checkIfRoundEnd(self):
		if(len(self.winnerRound) == 3):
			for i in self.winnerRound:
				if(self.winnerRound.index(i) == "Bot"):
					self.roundByBot += 1
				elif(self.winnerRound.index(i) == "Human"):
					self.roundByHuman += 1
			if(self.roundByHuman > self.roundByBot):
				return 1
			else:
				return 2

	def checkScoreToNextStage(self):
		if(self.scoreHuman == 3 and self.scoreBot == 3):
			self.scoreHuman = 0
			self.scoreBot = 0
			return
		if(self.scoreHuman == 3):
			self.addWinnerRound("Human")
			self.resetScoreToNextRound()
		elif(self.scoreBot == 3):
			self.addWinnerRound("Bot")
			self.resetScoreToNextRound()


##Defining classes

A = Choices()
B = Bot()
C = ScoreBoardAndRound()


##Start

print("Welcome to JanKenPon (Rock, Paper, Scissors, SUIT!)\n\nChoices : \n1. Rock,\n2. Paper, \n3.Scissors, \n\nQ = Quit")


while(True):
	print("Round :"+str(C.Round))

	botPick = B.randomizeBotChoice()

	humanInput = input("Pick your choice : ")

	if(humanInput == "Q" or humanInput == "q" or humanInput == ""):
		break

	winnerSession = A.defWinner(C.compareToWin(int(humanInput), botPick))
	print("The winner is : "+winnerSession)
	if(winnerSession == "Human"):
		C.addHumanScore()
	elif(winnerSession == "Bot"):
		C.addBotScore()
	else:
		C.addHumanScore()
		C.addBotScore()
	C.checkScoreToNextStage()

	if(C.checkIfRoundEnd() != None):
		print("\n\n\nThe winner of this game is : "+str(A.defWinner(C.checkIfRoundEnd())))
		break
