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
                userInput = self.userInput()
                while not self.isValidUserInput(userInput):
                    userInput = self.userInput()
                self.userPiecesService.addPiece(int(userInput[0]), int(userInput[1]))
            else:
                self.aiPiecesService.addPiece()
            if self.isGameWon():
                gameWon = True
                winner = self.winner()
            if self.isBoardFull():
                boardFull = True
                draw = True
            playerToMove = 1 - playerToMove
            printer.printBoard(self.userPiecesService.getList(), self.aiPiecesService.getList())
            if draw:
                print("draw")
                return
            if gameWon:
                if winner == 0:
                    print("User won!")
                else:
                    print("AI won!")
                return

    def isBoardFull(self):
        if len(self.userPiecesService.getList()) + len(self.aiPiecesService.getList()) == 225:
            return True
        return False

    def isGameWon(self):
        return self.gameService.isGameOver()

    def winner(self):
        return self.gameService.winner()

    def userInput(self):
        userInput = input("add new piece:")
        userInput.strip()
        userInput = userInput.split()
        return userInput

    def isValidUserInput(self, userInput):
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
