import Test.CommandsTest
import Test.ExpenseTest
import Test.ExpenseValidationTest


def test():
    Test.CommandsTest.test()
    Test.ExpenseTest.test()
    Test.ExpenseValidationTest.test()
    print("testing done successfully")
