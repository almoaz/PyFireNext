"""
MIT License

Copyright (c) 2022 Mahfuz Salehin Moaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from FireNext.developer.Doc.__tag__ import *


class __self__:
    def __self__read__(self):
        return open(self.__add__(".ndb"), "r").read()

    def __self__(self):
        database = __self__.__self__read__(self)
        childValue = ""
        spaceLength = len(self)
        childName = ""
        returnValue = ""
        for x in range(database.__len__()):
            if database[x] != start__tag and database[x] != child__end__tag and database[x] != end__tag:
                childValue = childValue + database[x]
            if database[x] == value__child__tag:
                childName = childValue
                childValue = ""
            if database[x] == child__end__tag:
                if childName != "":
                    if returnValue == "":
                        returnValue = self + "\n".ljust(spaceLength, " ") + devided__tag + line__tag + childName + childValue
                    else:
                        returnValue = returnValue + "\n".ljust(spaceLength,
                                                               " ") + devided__tag + line__tag + childName + childValue
                    childName = ""
                    childValue = ""
                else:
                    space = "".ljust(spaceLength - 1, " ") + devided__tag + "".ljust(len(childValue) + 2) + devided__tag
                    value = __self__.__self__1(childValue, space)
                    if returnValue == "":
                        returnValue = self + "\n".ljust(spaceLength, " ") + devided__tag + line__tag + value
                    else:
                        returnValue = returnValue + "\n".ljust(spaceLength, " ") + devided__tag + line__tag + value

                    childValue = ""
            if x == len(database) - 1:
                if childName != "":
                    if returnValue == "":
                        returnValue = self + "\n".ljust(spaceLength, " ") + devided__tag + line__tag + childName + childValue
                    else:
                        returnValue = returnValue + "\n".ljust(spaceLength,
                                                               " ") + devided__tag + line__tag + childName + childValue
                else:
                    space = "".ljust(spaceLength - 1, " ") + devided__tag + "".ljust(len(childValue) + 2) + devided__tag
                    value = __self__.__self__1(childValue, space)
                    if returnValue == "":
                        returnValue = self + "\n".ljust(spaceLength, " ") + devided__tag + line__tag + value
                    else:
                        returnValue = returnValue + "\n".ljust(spaceLength, " ") + devided__tag + line__tag + value
        return returnValue

    def __self__1(self, parentSpace):
        database = __self__.__self__read__(self)
        childValue = ""
        spaceLength = parentSpace
        childName = ""
        returnValue = ""
        for x in range(database.__len__()):
            if database[x] != start__tag and database[x] != child__end__tag and database[x] != end__tag:
                childValue = childValue + database[x]
            if database[x] == value__child__tag:
                childName = childValue
                childValue = ""
            if database[x] == child__end__tag:
                if childName != "":
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + childName + childValue
                    elif returnValue != "":
                        returnValue = returnValue + "\n" + spaceLength + line__tag + childName + childValue

                    childName = ""
                    childValue = ""
                else:
                    space = spaceLength + "".ljust(len(childValue) + 2) + devided__tag
                    value = __self__.__self__2(childValue, space)
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + value
                    else:
                        returnValue = returnValue + "\n" + spaceLength + line__tag + value

                    childValue = ""

            if x == len(database) - 1:
                if childName != "":
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + childName + childValue
                    elif returnValue != "":
                        returnValue = returnValue + "\n" + spaceLength + line__tag + childName + childValue

                else:
                    space = spaceLength + "".ljust(len(childValue) + 2) + devided__tag
                    value = __self__.__self__2(childValue, space)
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + value
                    else:
                        returnValue = returnValue + "\n" + spaceLength + line__tag + value

        return returnValue

    def __self__2(self, parentSpace):
        database = __self__.__self__read__(self)
        childValue = ""
        spaceLength = parentSpace
        childName = ""
        returnValue = ""
        for x in range(database.__len__()):
            if database[x] != start__tag and database[x] != child__end__tag and database[x] != end__tag:
                childValue = childValue + database[x]
            if database[x] == value__child__tag:
                childName = childValue
                childValue = ""
            if database[x] == child__end__tag:
                if childName != "":
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + childName + childValue
                    elif returnValue != "":
                        returnValue = returnValue + "\n" + spaceLength + line__tag + childName + childValue

                    childName = ""
                    childValue = ""
                else:
                    space = spaceLength + "".ljust(len(childValue) + 2) + devided__tag
                    value = __self__.__self__1(childValue, space)
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + value
                    else:
                        returnValue = returnValue + "\n" + spaceLength + line__tag + value

                    childValue = ""

            if x == len(database) - 1:
                if childName != "":
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + childName + childValue
                    elif returnValue != "":
                        returnValue = returnValue + "\n" + spaceLength + line__tag + childName + childValue

                else:
                    space = spaceLength + "".ljust(len(childValue) + 2) + devided__tag
                    value = __self__.__self__1(childValue, space)
                    if returnValue == "":
                        returnValue = self + "\n" + spaceLength + line__tag + value
                    else:
                        returnValue = returnValue + "\n" + spaceLength + line__tag + value

        return returnValue

    def __add__(self, param):
        pass