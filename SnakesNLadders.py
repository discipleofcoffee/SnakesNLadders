"""
A simple game of snakes and ladders.
Asks for number of players and their names.
Automated play.

Written to learn about python programming.

"""

import random
import sys

class Dice(object):
    """ Specifies the attributes required for the dice.

        Keyword args:
            customDice -- (default: 0) Determines if player can input the dice parameters. 0 -- No, 1 -- Yes.
            diceCount -- (default: 1) Sets number of dice used in the game. Range: int([1: )
            diceSides -- (default: 6) Sets the number of sides each dice has. Range: int([1: )

    """

    def __init__(self, customDice=0, diceCount=1, diceSides=6):
        """ Initializes the parameters of the dice- how many dice, how many sides.

        :return: none
        """

        if customDice != 0:
            diceCount = input('How many dice can the game use? (Default is 1): ')
            diceSides = input('How many sides does each dice have? (Default is 6): ')

        try:
            # abs(int(float(diceCount): ensures any value entered is converted to appropriate number.
            # Ex - float('-6.7') --> -6.7, int(-6.7) --> -6, abs(-6) --> 6.
            diceCount = abs(int(float(diceCount)))
        except ValueError:
            # raised if user input can not be converted into a numerical value. Ex- 'a' .
            print(
                'Invalid value. Number of dice can only be an integer with value 1 or more. Using default value of 1.')
            diceCount = 1
        except NameError:
            # raised if user input is a character which the program deals with as a variable. Ex- a .
            print(
                'Invalid value. Number of dice can only be an integer with value 1 or more. Using default value of 1.')
            diceCount = 1
        try:
            diceSides = abs(int(float(diceSides)))
        except ValueError:
            print(
                'Invalid value. Number of sides a dice has can only be an integer with value 1 or more. Using default value of 6.')
            diceSides = 6
        except NameError:
            print(
                'Invalid value. Number of sides a dice has can only be an integer with value 1 or more. Using default value of 6.')
            diceSides = 6
        self.diceCount = diceCount
        self.diceSides = diceSides

    def rollDice(self):
        """Rolls the dice for one turn. Returns the sum of the dice values.

        :return: int
        """
        rolledNumbers = []
        for idx in range(1,self.diceCount+1):
            rolledNumbers.append(random.randint(1, self.diceSides+1))

        return sum(rolledNumbers)


class GameMaster(object):
    """ Gets player count, checks if a player has won, moves the player along snakes and ladders on the board.
    """

    def __init__(self):

        self.Player = Player() # Plyaer class imported using composition.
        self.Dice = Dice()  # Dice class imported using comprehension.

    def getPlayerCount(self):
        """ Prompts the user to enter the number of players.

        :return: int
        """
        playerCount = input('Enter number of players: ')
        try:
            # abs(int(float(playerCount): ensures any value entered is converted to appropriate number.
            # Ex - float('-6.7') --> -6.7, int(-6.7) --> -6, abs(-6) --> 6.
            playerCount = abs(int(float(playerCount)))
        except ValueError:
            # raised if user input can not be converted into a numerical value. Ex- 'a' .
            print('Invalid value. Number of players can only be an integer with value 1 or more. Using default value of 1.')
            playerCount = 1
        except NameError:
            # raised if user input is a character which the program deals with as a variable. Ex- a .
            print('Invalid value. Number of players can only be an integer with value 1 or more. Using default value of 1.')
            playerCount = 1
        return playerCount

    def winCheck(self, currentPlayerOutcome, currentPlayerName):
        """ Checks if a player has reached the winning position.
        Prints the win message and terminates program.

        Keyword args:
            currentPlayerOutcome --  Accepts an int value specific to each player. 1 indicates player has won.
            currentPLayerName -- Accepts a str indicating the player's name

        :return : none
        """
        if currentPlayerOutcome == 1:
            print('Player', currentPlayerName, 'won!')
            print('Press any key to end program.')
            input()
            sys.exit()

    def snlReposition(self, currentPlayerPosition):
        """ Checks if a player is at a ladder or snake head and repositions them.
        
        :param currentPlayerPosition: Accepts an int value indicating a specific player's position
        :return: int
        """
        boardLayout = {1: 38,
                       4: 14,
                       9: 31,
                       17: 7,
                       21: 42,
                       28: 84,
                       51: 67,
                       54: 34,
                       62: 19,
                       64: 60,
                       71: 91,
                       80: 100,
                       87: 24,
                       93: 73,
                       95: 75,
                       98: 79}

        try:
            return boardLayout[currentPlayerPosition]
        except KeyError:
            return (currentPlayerPosition)


class Player(object):
    """ Specifies attributes for the player class.
    """

    def __init__(self, playerName='', playerPosition=0):
        """ Initializes parameters of the player.

       :param playerName: (default: '') Specifies plaeyr name.
        :param playerPosition:(default: 0) Specifies score of player. STarting score is 0.

        :return: none
        """
        self.playerName = playerName
        self.playerPosition = playerPosition
        self.playerWon = 0
        self.Dice = Dice()

    def rollDice(self): #Die.rollDie() imported into Player using composition.
        """ Rolls the dice for one turn. Returns the sum of the dice values.

        :return: int
        """
        return (self.Dice.rollDice())

    def getPlayer(self, playerQuery='position'):
        """ Returns player related data.

        :param playerQuery: 'name' | 'position' | 'outcome'
        :return: string | int | int
        """

        playerQuery = playerQuery.lower()
        if playerQuery == 'name':
            return self.playerName
        elif playerQuery == 'position':
            return self.playerPosition
        elif playerQuery == 'outcome':
            return (self.playerWon)

    def movePlayer(self, newPosition):
        """ Checks if player object is eligible to move and Changes the position of the player object.
        :param newPosition: int
        :return: none
        """
        if self.playerPosition == 0 and newPosition != 6:
            print('Player', self.playerName, 'cannot move until they roll a 6. They rolled a', newPosition,
                  '. Turn to next player.')
        elif self.playerPosition == 0 and newPosition == 6:
            newPosition = Player.rollDice(self)
            self.playerPosition = newPosition
            print('We have a 6! And', self.playerName, 'moves to', self.playerPosition, '.')
        else:
            self.playerPosition = newPosition
            if self.playerPosition > MAXPOSITION:
                self.playerWon = 1
            else:
                print('', self.playerName, 'moves to', self.playerPosition, '.')


if __name__ == '__main__':

    MAXPOSITION = (100)
    dice = Dice(customDice=0, diceCount=1, diceSides=6)
    game = GameMaster()
    playerCount = game.getPlayerCount()
    allPlayers = []

    # loop to get player names and initialize positions to 0.
    for playerCounter in range(0, playerCount):
        print('Enter player', playerCounter + 1, 'name:')
        playerNameTemp = input()
        allPlayers.append(Player(playerName=playerNameTemp, playerPosition=0))

    for turnCounter in range(0, MAXPOSITION):

        for playerCounter in range(0, playerCount):

            rolledValue = dice.rollDice()
            newPosition = rolledValue + allPlayers[playerCounter].getPlayer('position')
            allPlayers[playerCounter].movePlayer(newPosition)
            currentPlayerPosition = allPlayers[playerCounter].getPlayer('position')
            rePosition = game.snlReposition(currentPlayerPosition)

            if rePosition > currentPlayerPosition:
                print('', allPlayers[playerCounter].getPlayer('name'), 'found a ladder at',
                      currentPlayerPosition, '! Moving to', rePosition, '!')
                allPlayers[playerCounter].movePlayer(rePosition)

            elif rePosition < currentPlayerPosition:
                print('', allPlayers[playerCounter].getPlayer('name'), 'was bitten by a snake at',
                      currentPlayerPosition, '! Moving to', rePosition, '!')
                allPlayers[playerCounter].movePlayer(rePosition)

            game.winCheck(allPlayers[playerCounter].getPlayer('outcome'), allPlayers[playerCounter].getPlayer('name'))
