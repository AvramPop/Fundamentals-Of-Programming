import datetime


expenseTypeEnum = ("housekeeping", "food", "transport", "clothing", "internet", "others")
commandsEnum = ("add", "insert", "remove", "remove", "list", "sum", "max", "sort", "filter", "undo", "exit")
now = datetime.datetime.now()
today = now.day if now.day <= 30 else 1
