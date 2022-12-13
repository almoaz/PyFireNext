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

import os
from FireNext.developer.Doc.__tag__ import *
from FireNext.developer.Doc.__self__update__ import __self__update__


class __self__child__delete__:
    def __self__child__delete__(self):
        value = ""
        parent = ""
        databaseName = ""
        for x in range(self.__len__()):
            if self[x] != ">":
                value = value + self[x]
            if self[x] == ">":
                value = value + self[x]
                parent = parent + value
                value = ""

            if x == self.__len__() - 1:

                if parent != "":
                    try:
                        dataBase = open(value + ".ndb", "r").read()
                    except:
                        return "'" + value + "' child not found"
                    if dataBase == "[]" or dataBase == "":
                        __self__update__.__self__update__(parent[:-1], value)
                        os.remove(value + ".ndb")
                        return "true"
                    else:
                        databaseName = value
                        value = ""
                        childFound = "true"
                        for x1 in range(dataBase.__len__()):
                            if dataBase[x1] != child__end__tag and dataBase[x1] != start__tag and dataBase[
                                x1] != end__tag:
                                value = value + dataBase[x1]
                            if dataBase[x1] == value__child__tag:
                                childFound = "false"
                            elif dataBase[x1] == child__end__tag:
                                if childFound == "true":
                                    __self__child__delete__.__self__child__delete__1(value)
                                    value = ""
                                else:
                                    value = ""
                                    childFound = "true"
                            if x1 == len(dataBase) - 1:
                                if childFound == "true":
                                    __self__child__delete__.__self__child__delete__1(value)
                                os.remove(databaseName + ".ndb")
                else:
                    try:
                        dataBase = open(value + ".ndb", "r").read()
                    except:
                        return "'" + value + "' child not found"
                    if dataBase == "[]" or dataBase == "":

                        os.remove(value + ".ndb")
                        return "true"
                    else:
                        databaseName = value
                        value = ""
                        childFound = "true"
                        for x1 in range(dataBase.__len__()):
                            if dataBase[x1] != child__end__tag and dataBase[x1] != start__tag and dataBase[
                                x1] != end__tag:
                                value = value + dataBase[x1]
                            if dataBase[x1] == value__child__tag:
                                childFound = "false"
                            elif dataBase[x1] == child__end__tag:
                                if childFound == "true":
                                    __self__child__delete__.__self__child__delete__1(value)
                                    value = ""
                                else:
                                    value = ""
                                    childFound = "true"
                            if x1 == len(dataBase) - 1:
                                if childFound == "true":
                                    __self__child__delete__.__self__child__delete__1(value)
                                os.remove(databaseName + ".ndb")



        if parent!= "":
            __self__update__.__self__update__(parent[:-1], databaseName)
        return "true"

    def __self__child__delete__1(self):
        value = ""
        parent = ""
        for x in range(self.__len__()):
            if self[x] != ">":
                value = value + self[x]
            if self[x] == ">":
                parent = value
                value = ""

            if x == self.__len__() - 1:
                try:
                    dataBase = open(value + ".ndb", "r").read()
                except:
                    return "'" + value + "' child not found"
                if dataBase == "[]" or dataBase == "":
                    os.remove(value + ".ndb")
                    return "true"
                else:
                    databaseName = value
                    value = ""
                    childFound = "true"
                    for x1 in range(dataBase.__len__()):
                        if dataBase[x1] != child__end__tag and dataBase[x1] != start__tag and dataBase[x1] != end__tag:
                            value = value + dataBase[x1]
                        if dataBase[x1] == value__child__tag:
                            childFound = "false"
                        elif dataBase[x1] == child__end__tag:
                            if childFound == "true":
                                __self__child__delete__.__self__child__delete__2(value)
                                value = ""
                            else:
                                value = ""
                                childFound = "true"
                        if x1 == len(dataBase) - 1:
                            if childFound == "true":
                                __self__child__delete__.__self__child__delete__2(value)
                            os.remove(databaseName + ".ndb")
                            return "true"

    def __self__child__delete__2(self):
        value = ""
        parent = ""
        for x in range(self.__len__()):
            if self[x] != ">":
                value = value + self[x]
            if self[x] == ">":
                parent = value
                value = ""

            if x == self.__len__() - 1:
                try:
                    dataBase = open(value + ".ndb", "r").read()
                except:
                    return "'" + value + "' child not found"
                if dataBase == "[]" or dataBase == "":
                    os.remove(value + ".ndb")
                    return "true"
                else:
                    databaseName = value
                    value = ""
                    childFound = "true"
                    for x1 in range(dataBase.__len__()):
                        if dataBase[x1] != child__end__tag and dataBase[x1] != start__tag and dataBase[x1] != end__tag:
                            value = value + dataBase[x1]
                        if dataBase[x1] == value__child__tag:
                            childFound = "false"
                        elif dataBase[x1] == child__end__tag:
                            if childFound == "true":
                                __self__child__delete__.__self__child__delete__1(value)
                                value = ""
                            else:
                                value = ""
                                childFound = "true"
                        if x1 == len(dataBase) - 1:
                            if childFound == "true":
                                __self__child__delete__.__self__child__delete__1(value)
                            os.remove(databaseName + ".ndb")
                            return "true"

    def __len__(self):
        pass