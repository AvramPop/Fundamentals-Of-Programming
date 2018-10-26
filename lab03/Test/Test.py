import Test.CommandsTest
import Test.ExpenseTest
import Test.ExpenseValidationTest
import Test.ExpensesListHistoryStackTest


def test():
    Test.ExpensesListHistoryStackTest.test()
    Test.CommandsTest.test()
    Test.ExpenseTest.test()
    Test.ExpenseValidationTest.test()
    print("testing done successfully")
