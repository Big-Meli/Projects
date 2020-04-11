import time, random

console = input("STEW >> File you would like to load >> ")

file = open((console+".stew"), "r")
stew = file.read()
file.close()

stewLines = stew.split("\n")
stewLinesRaw = stew

class variable:
    def __init__(variable, name, value, type):
        variable.name = name
        variable.type = type
        try:
            if type == "boolean":
                variable.value = bool(value)

            elif type == "whole":
                variable.value = int(value)

            elif type == "decimal":
                variable.value = float(value)

            elif type == "text":
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

class locationClass:
    def __init__(location, name, lines):
        location.name = name
        location.lines = lines

class lineClass:
    def __init__(line, value, type):
        line.value = value
        line.type = type
        line.handled = False

        if line.location() or line.loop():
            line.ignore = True
        else:
            line.ignore = False

    def location(line):
        if line.type == "location":
            return True

    def loop(line):
        if line.type == "loop":
            return True

    def message(line):
        if line.type == "message":
            return True

    def set(line):
        if line.type == "set":
            return True

locations = []

lines = []
for x in stewLines:
    lines.append(lineClass(x, ""))

for x in lines:
    if x.value.startswith("@location"):
        x.value = x.value.replace("{", "LOCATIONBREAK")
    if x.value.startswith("}"):
        x.value = x.value.replace("}","LOCATIONBREAK")

linesx = []
for x in lines:
    if x.value.startswith(" "):
        linesx.append(x.value[1:])
    else:
        linesx.append(x.value)

linesy = "".join(linesx).split("LOCATIONBREAK")
linesy.pop(-1)
print(linesy)
while len(linesy) > 0:
    locations.append(locationClass(linesy[0].split(" ")[1], linesy[1]))
    linesy.pop(0)
    linesy.pop(0)

for z in locations:
    print("Location name: '{}', location lines: '{}'".format(z.name, z.lines))

linesx = []
for x in lines:
    linesx.append(x.value)

print("".join(linesx))
"""
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
                    elif variableType == "whole":
                        variableValue = int(input(""))
                    elif variableType == "decimal":
                        variableValue = float(input(""))
                    elif variableType == "text":
                        variableValue = str(input(""))
                except ValueError:
                    print("STEW >> $ValueError >> Input: {} tried to parse: {} as: {}. Input: {} is not type: {}!".format(variableEachLine[2], variableValue, variableType, variableValue, variableType))
                    quit()

                variables.append(variable(variableEachLine[2], variableValue, variableEachLine[1]))
            else:
                variables.append(variable(variableEachLine[2], variableValue[1:], variableEachLine[1]))

    currLine += 1
"""
