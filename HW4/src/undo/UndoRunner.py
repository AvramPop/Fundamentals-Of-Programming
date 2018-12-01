from src.Constants import Constants
from src.Date import Date
from src.dao.ClientDAO import ClientDAO
from src.dao.MovieDAO import MovieDAO
from src.undo.OppositeCommandGenerator import OppositeCommandGenerator
from src.undo.RedoActionRunner import RedoActionRunner
from src.undo.UndoActionRunner import UndoActionRunner


class UndoRunner:

    def addCommandToUndo(self, command, controller, undoStack, typeWorkingWith, commandsStack):
        # for every command add to stack the command + id of element + type
        oppositeCommandGenerator = OppositeCommandGenerator()
        if typeWorkingWith == "client":
            if command[0] == "add":
                undoStack.push(oppositeCommandGenerator.addClientOppositeCommand(controller))
                commandsStack.push(command)
            elif command[0] == "remove":
                undoStack.push(oppositeCommandGenerator.removeClientOppositeCommand(command, controller))
                commandsStack.push(command)
            elif command[0] == "update":
                undoStack.push(oppositeCommandGenerator.updateClientOppositeCommand(command, controller))
                commandsStack.push(command)
            else:
                return
        elif typeWorkingWith == "movie":
            if command[0] == "add":
                commandsStack.push(command)
                undoStack.push(oppositeCommandGenerator.addMovieOppositeCommand(controller))
            elif command[0] == "remove":
                commandsStack.push(command)
                undoStack.push(oppositeCommandGenerator.removeMovieOppositeCommand(command, controller))
            elif command[0] == "update":
                commandsStack.push(command)
                undoStack.push(oppositeCommandGenerator.updateMovieOppositeCommand(command, controller))
            else:
                return
        elif typeWorkingWith == "rental":
            if command[0] == "rent":
                commandsStack.push(command)
                undoStack.push(oppositeCommandGenerator.rentOppositeCommand(controller))
            elif command[0] == "return":
                commandsStack.push(command)
                undoStack.push(oppositeCommandGenerator.returnOppositeCommand(command, controller))
            else:
                return
        else:
            raise TypeError

    def undo(self, clientController, movieController, rentalController, stack):
        self.__runUndoCommand(stack.pop(), clientController, movieController, rentalController)

    def redo(self, commandToRedo, clientController, movieController, rentalController):
        redoActionRunner = RedoActionRunner()
        if commandToRedo[0] == "rent":
            dueDate = Date(int(commandToRedo[3]),
                           int(commandToRedo[4]),
                           int(commandToRedo[5]))
            redoActionRunner.rent(dueDate, commandToRedo, rentalController, clientController, movieController)
        elif commandToRedo[0] == "return":
            redoActionRunner.doReturn(commandToRedo, rentalController)
        elif commandToRedo[0] == "add" and len(commandToRedo) == 2:
            redoActionRunner.addClient(commandToRedo, clientController)
        elif commandToRedo[0] == "remove" and commandToRedo[2] == "client":
            redoActionRunner.removeClient(commandToRedo, clientController, rentalController)
        elif commandToRedo[0] == "update" and len(commandToRedo) == 3:
            redoActionRunner.updateClient(commandToRedo, clientController)
        elif commandToRedo[0] == "add" and len(commandToRedo) == 4:
            redoActionRunner.addMovie(commandToRedo, movieController)
        elif commandToRedo[0] == "remove" and commandToRedo[2] == "movie":
            redoActionRunner.removeMovie(commandToRedo, movieController, rentalController)
        elif commandToRedo[0] == "update" and len(commandToRedo) == 5:
            redoActionRunner.updateMovie(commandToRedo, movieController)

    def __runUndoCommand(self, command, clientController, movieController, rentalController):
        typeOfOperation = command[0]
        operation = command[1]
        undoActionRunner = UndoActionRunner()
        if typeOfOperation == "client":
            if operation == "add":
                undoActionRunner.addClient(command, clientController)
            elif operation == "remove":
                undoActionRunner.removeClient(command, clientController, rentalController)
            elif operation == "update":
                undoActionRunner.updateClient(command, clientController)
        elif typeOfOperation == "movie":
            if operation == "add":
                undoActionRunner.addMovie(command, movieController)
            elif operation == "remove":
                undoActionRunner.removeMovie(command, movieController, rentalController)
            elif operation == "update":
                undoActionRunner.updateMovie(command, movieController)
        elif typeOfOperation == "rental":
            if operation == "returnedDateToNone":
                undoActionRunner.returnedDateToNone(command, rentalController)
            elif operation == "remove":
                undoActionRunner.removeRental(command, rentalController)
