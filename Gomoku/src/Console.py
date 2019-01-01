import random

from src.Piece import Piece
from src.Printer import Printer


class Console:
    def __init__(self, userPiecesService, aiPiecesService, gameService) -> None:
        self.userPiecesService = userPiecesService
        self.aiPiecesService = aiPiecesService
        self.gameService = gameService

    def run(self):
        playerToMove = random.randint(0, 1)
        print(str(playerToMove) + " starts")
        boardFull = False
        gameWon = False
        draw = False
        winner = -1
        printer = Printer()
        while not boardFull and not gameWon:
            print(str(playerToMove) + " moves")
            if playerToMove == 0:
                userInput = self.__userInput()
                while not self.__isValidUserInput(userInput):
                    userInput = self.__userInput()
                self.userPiecesService.addPiece(int(userInput[0]), int(userInput[1]))
            else:
                self.aiPiecesService.addPiece()
            if self.__isGameWon():
                gameWon = True
                winner = self.__winner()
            if self.__isBoardFull():
                boardFull = True
                draw = True
            playerToMove = 1 - playerToMove
            printer.printBoard(self.userPiecesService.getList(), self.aiPiecesService.getList())
            if gameWon:
                if winner == 0:
                    print("User won!")
                else:
                    print("AI won!")
                return
            if draw:
                print("draw")
                return

    def __isBoardFull(self):
        """
        Check whether all board is full, that is, there are 225 (15x15) pieces on it.
        :return:
        """
        if len(self.userPiecesService.getList()) + len(self.aiPiecesService.getList()) == 225:
            return True
        return False

    def __isGameWon(self):
        """
        Checks whether game is over.
        """
        return self.gameService.isGameOver()

    def __winner(self):
        """
        Return the winner.
        """
        return self.gameService.winner()

    def __userInput(self):
        """
        Take user input and format it.
        """
        userInput = input("add new piece:")
        userInput.strip()
        userInput = userInput.split()
        return userInput

    def __isValidUserInput(self, userInput):
        """
        Validate user input.
        """
        if not len(userInput) == 2:
            print("input should be 2 ints")
            return False
        if not userInput[0].isdigit() or not userInput[1].isdigit():
            print("wrong input. should be positive ints")
            return False
        if not self.userPiecesService.isValidMove(int(userInput[0]), int(userInput[1])):
            print("cannot add on that position")
            return False
        return True
