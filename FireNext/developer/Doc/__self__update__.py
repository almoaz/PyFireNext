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


class __self__update__:

    def __self__update__(self, child):
        parentValue = ""
        parent1 = ""
        for x in range(self.__len__()):
            if self[x] != ">":
                parentValue = parentValue + self[x]

            if self[x] == ">":
                parentValue = parentValue + self[x]
                parent1 = parent1 + parentValue
                parentValue = ""
            if x == len(self) - 1:
                dataBase = open(parentValue + ".ndb", "r").read()
                value = ""
                updateNDB = ""
                for x1 in range(dataBase.__len__()):
                    if dataBase[x1] == start__tag:
                        updateNDB = dataBase[x1]
                    if dataBase[x1] != child__end__tag and dataBase[x1] != start__tag and dataBase[x1] != end__tag:
                        value = value + dataBase[x1]
                    if dataBase[x1] == child__end__tag:
                        if value == child:
                            updateNDB = updateNDB
                        else:
                            value = value + dataBase[x1]
                            updateNDB = updateNDB + value
                        value = ""
                    if x1 == len(dataBase) - 1:
                        if value == child:
                            if updateNDB == start__tag:
                                updateNDB = updateNDB + end__tag
                                open(parentValue.__add__(".ndb"), "w").write(updateNDB)
                            else:
                                updateNDB = updateNDB[:-1] + end__tag
                                open(parentValue.__add__(".ndb"), "w").write(updateNDB)

                            if updateNDB == "[]":
                                os.remove(parentValue + ".ndb")
                                __self__update__.__self__update__1(parent1[:-1], parentValue)
                        else:
                            updateNDB = updateNDB + value + end__tag
                            open(parentValue.__add__(".ndb"), "w").write(updateNDB)

    def __self__update__1(self, child):
        parentValue = ""
        parent1 = ""
        for x in range(self.__len__()):
            if self[x] != ">":
                parentValue = parentValue + self[x]

            if self[x] == ">":
                parentValue = parentValue + self[x]
                parent1 = parent1 + parentValue
                parentValue = ""
            if x == len(self) - 1:

                dataBase = open(parentValue + ".ndb", "r").read()
                value = ""
                updateNDB = ""
                for x1 in range(dataBase.__len__()):
                    if dataBase[x1] == start__tag:
                        updateNDB = dataBase[x1]
                    if dataBase[x1] != child__end__tag and dataBase[x1] != start__tag and dataBase[x1] != end__tag:
                        value = value + dataBase[x1]
                    if dataBase[x1] == child__end__tag:
                        if value != child:
                            value = value + dataBase[x1]
                            updateNDB = updateNDB + value

                        value = ""
                    if x1 == len(dataBase) - 1:
                        if value == child:
                            if updateNDB == start__tag:
                                updateNDB = updateNDB + end__tag
                                open(parentValue.__add__(".ndb"), "w").write(updateNDB)
                            else:
                                updateNDB = updateNDB[:-1] + end__tag
                                open(parentValue.__add__(".ndb"), "w").write(updateNDB)

                            if updateNDB == "[]":
                                os.remove(parentValue + ".ndb")
                                __self__update__.__self__update__(parent1[:-1], parentValue)
                        else:
                            updateNDB = updateNDB + value + end__tag
                            updateNDB = open(parentValue.__add__(".ndb"), "w").write(updateNDB)

    def __len__(self):
        pass