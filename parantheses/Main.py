class Main:
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        numberOfParentheses = input("n = ")
        self.generateParenthesesRecursive(int(numberOfParentheses) / 2, int(numberOfParentheses) / 2, "")
        print("-------------------")
        self.generateParenthesesIterative(int(numberOfParentheses), 0, [0] * 100, 0)

    def generateParenthesesIterative(self, numberOfParentheses, index, solution, sum):
        pool = [1, -1]
        for parenthese in pool:
            solution[index] = parenthese
            if self.isValidSolution(index, sum + parenthese, numberOfParentheses):
                if index == numberOfParentheses - 1:
                    self.printParentheses(solution, numberOfParentheses)
                else:
                    self.generateParenthesesIterative(numberOfParentheses, index + 1, solution, sum + parenthese)

    def isValidSolution(self, index, sum, numberOfParentheses):
        if index == numberOfParentheses - 1 and sum != 0:
            return False
        if sum < 0:
            return False
        return True

    def printParentheses(self, stack, numberOfParentheses):
        printed = 0
        for element in stack:
            if element == 1:
                print("(", end="")
                printed += 1
            else:
                print(")", end="")
                printed += 1
            if printed == numberOfParentheses:
                print()
                return

    def generateParenthesesRecursive(self, left, right, resultString):
        if left == 0 and right == 0:
            print(resultString)
        if left > right:
            return
        if left > 0:
            self.generateParenthesesRecursive(left - 1, right, resultString + "(")
        if right > 0:
            self.generateParenthesesRecursive(left, right - 1, resultString + ")")


main = Main()
main.run()

