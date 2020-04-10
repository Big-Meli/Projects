import time, random

console = input("STEW >> File you would like to load >> ")

file = open((console+".stew"), "r")
stew = file.read()
file.close()

stewLines = stew.split("\n")


class variable:
    def __init__(variable, name, value, type):
        variable.name = name
        variable.type = type
        try:
            if type == "boolean":
                variable.value = bool(value)

            elif type == "int":
                variable.value = int(value)

            elif type == "float":
                variable.value = float(value)

            elif type == "string":
                variable.value = str(value)

            else:
                print("STEW >> $AssignmentError >> Variable: {} could not parse {}. Variable {} NEEDS a type!".format(name, value, name))

        except ValueError:
            print("STEW >> $ValueError >> Variable: {} tried to parse: {} as: {}. Variable: {} is not type: {}!".format(name, value, type, name, type))
            quit()


class array:
    def __init__(array, value, type):
        pass


class step:
    def __init__(step, value, type):
        pass


variables = []
currLine = 1

handledCode = []
for eachLine in stewLines:
    if not eachLine.startswith("//"):
        stewKeyWords = eachLine.split(" ")

        if eachLine.lower().startswith("message"):
            placeFixedMessage = []

            messageValue = eachLine.split('"')[1]

            for word in messageValue.split(" "):
                if word.startswith("$"):
                    variableHandled = False
                    for eachVariable in variables:
                        if eachVariable.name == word[1:]:
                            variableHandled = True
                            placeFixedMessage.append(eachVariable.value)
                    if not variableHandled:
                        print("STEW >> $ReferenceError >> The Variable: {} could not be referenced because it does not exist!".format(word))
                        quit()
                else:
                    placeFixedMessage.append(word)

            print(" ".join(placeFixedMessage))

        elif eachLine.lower().startswith("set"):
            variableEachLine = eachLine.split(" ")
            variableValue = " ".join(eachLine.split("to")[1:])
            variableType = variableEachLine[1]
            if variableValue[1:] == "log":
                try:
                    if variableType == "boolean":
                        variableValue = bool(input(""))
                    elif variableType == "int":
                        variableValue = int(input(""))
                    elif variableType == "float":
                        variableValue = float(input(""))
                    elif variableType == "string":
                        variableValue = str(input(""))
                except ValueError:
                    print("STEW >> $ValueError >> Input: {} tried to parse: {} as: {}. Input: {} is not type: {}!".format(variableEachLine[2], variableValue, variableType, variableValue, variableType))
                    quit()

                variables.append(variable(variableEachLine[2], variableValue, variableEachLine[1]))
            else:
                variables.append(variable(variableEachLine[2], variableValue[1:], variableEachLine[1]))

    currLine += 1
