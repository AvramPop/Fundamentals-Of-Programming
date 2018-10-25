from Validation.CommandsValidation import *


def isCommandTest():
    assert isCommand("add") is True
    assert isCommand(55) is False
    assert isCommand("addd") is False
    assert isCommand("insert") is True
    assert isCommand("") is False


def isValidAddCommandTest():
    assert isValidAddCommand(['add']) is False
    assert isValidAddCommand(['asfd']) is False
    assert isValidAddCommand(['add', '-5']) is False
    assert isValidAddCommand(['add', 'sadsd', 'food']) is False
    assert isValidAddCommand(['add', '-5', 'food']) is False
    assert isValidAddCommand(['add', '5.5', 'food']) is False
    assert isValidAddCommand(['add', '5', 'adsda']) is False
    assert isValidAddCommand(['add', '5', '5']) is False
    assert isValidAddCommand(['add', '-5', 'sdadsa']) is False
    assert isValidAddCommand(['add', '-5', 'das', 'das']) is False
    assert isValidAddCommand(['dsa', '5', 'food']) is False
    assert isValidAddCommand(['add', '5', 'food']) is True


def isValidInsertCommandTest():
    assert isValidInsertCommand(['insert']) is False
    assert isValidInsertCommand(['asfd']) is False
    assert isValidInsertCommand(['insert', '-5']) is False
    assert isValidInsertCommand(['insert', 'sadsd', 'food']) is False
    assert isValidInsertCommand(['insert', 'sadsd', 'food', 'sadsd', 'food']) is False
    assert isValidInsertCommand(['insert', '-5', '100', 'food']) is False
    assert isValidInsertCommand(['insert', '5.5', '100', 'food']) is False
    assert isValidInsertCommand(['insert', 'sad', '100', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '-100', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '100.1', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '-saddsa', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '100', 'asd']) is False
    assert isValidInsertCommand(['insert', '5', '100', '55']) is False
    assert isValidInsertCommand(['sda', '5', '100', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '100', 'food']) is True


def isValidRemoveCommandTest():
    assert isValidRemoveCommand(['remove']) is False
    assert isValidRemoveCommand(['asd']) is False
    assert isValidRemoveCommand(['remove', 'sadasasd']) is False
    assert isValidRemoveCommand(['remove', '4.5']) is False
    assert isValidRemoveCommand(['remove', '-4']) is False
    assert isValidRemoveCommand(['remove', '4', 'ds']) is False
    assert isValidRemoveCommand(['remove', '4', 'to', '-5']) is False
    assert isValidRemoveCommand(['remove', '4', 'to', 'food']) is False
    assert isValidRemoveCommand(['remove', '-4', 'to', '5']) is False
    assert isValidRemoveCommand(['remove', '4', 'to', '5.5']) is False
    assert isValidRemoveCommand(['remove', '4.5', 'to', '5']) is False
    assert isValidRemoveCommand(['remove', '4', 'ton', '5']) is False
    assert isValidRemoveCommand(['remove', '4', '5', '-5']) is False
    assert isValidRemoveCommand(['remove', 'food', '55']) is False
    assert isValidRemoveCommand(['remove', 'foode']) is False
    assert isValidRemoveCommand(['remove', '6']) is True
    assert isValidRemoveCommand(['remove', '6', 'to', '9']) is True
    assert isValidRemoveCommand(['remove', 'food']) is True


def isValidListCommandTest():
    assert isValidListCommand(['fads', 'food', '>', '5']) is False
    assert isValidListCommand(['fads']) is False
    assert isValidListCommand(['list', 'foodss', '>', '5']) is False
    assert isValidListCommand(['list', '6', '>', '5']) is False
    assert isValidListCommand(['list', 'food', '!', '5']) is False
    assert isValidListCommand(['list', 'food', '55', '5']) is False
    assert isValidListCommand(['list', 'food', '>', 'sad']) is False
    assert isValidListCommand(['list', 'food', '>', '5.5']) is False
    assert isValidListCommand(['list', 'food', '>', '-55']) is False
    assert isValidListCommand(['list', 'internet', '>', 'sad']) is False
    assert isValidListCommand(['list']) is True
    assert isValidListCommand(['list', 'food']) is True
    assert isValidListCommand(['list', 'food', '>', '5']) is True
