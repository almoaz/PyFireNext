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
from FireNext.developer.Doc.__self__child__ import __self__child__


class __self__query__:
    def __self__query__(self):
        value = ""
        databaseName = ""
        parentDatabaseName = ""
        for x in range(self.__len__()):
            if ">" != self[x]:
                value = value.__add__(self[x])
            if ">".__eq__(self[x]):
                if databaseName.__eq__(""):
                    try:
                        open(value.__add__(".ndb"), "r")
                        databaseName = value
                        value = ""
                    except:
                        return "'" + value + "' database not found"
                elif databaseName.__ne__(""):

                    childData = open(databaseName.__add__(".ndb"), "r").read()
                    if childData.__eq__(""):
                        return "'" + value + "' child not found"
                    elif childData.__ne__(""):
                        readChild = ""
                        updateNDB = ""
                        for x1 in range(childData.__len__()):
                            if childData[x1].__ne__(end__tag):
                                updateNDB = updateNDB + childData[x1]
                            if childData[x1].__ne__(start__tag) and childData[x1].__ne__(child__end__tag) and childData[
                                x1].__ne__(end__tag):
                                readChild = readChild + childData[x1]
                            if childData[x1].__eq__(child__end__tag):
                                if readChild.__eq__(value):
                                    try:
                                        open(value.__add__(".ndb"), "r")
                                        if parentDatabaseName == "":
                                            parentDatabaseName = databaseName
                                        else:
                                            parentDatabaseName = parentDatabaseName + ">" + databaseName
                                        databaseName = value
                                        value = ""
                                        break
                                    except:
                                        return "'" + value + "' database not found"
                                readChild = ""

                            if childData[x1].__eq__(end__tag) and x1.__eq__(len(childData) - 1):
                                if readChild.__eq__(value):
                                    try:
                                        open(value.__add__(".ndb"), "r")
                                        if parentDatabaseName == "":
                                            parentDatabaseName = databaseName
                                        else:
                                            parentDatabaseName = parentDatabaseName + ">" + databaseName
                                        databaseName = value
                                        value = ""
                                    except:
                                        return "'" + value + "' database not found"
                                else:
                                    return "'" + value + "' child not found"

                    value = ""

            if x.__eq__(len(self) - 1):
                try:
                    childData = open(databaseName.__add__(".ndb"), "r").read()
                except:
                    return print("'" + databaseName + "' child not found")

                if childData.__eq__(""):
                    return "'" + value + "' child not found"
                elif childData.__ne__(""):
                    readChild = ""
                    updateNDB = ""
                    childMatch = "true"
                    query_child_name = ""
                    childData = open(databaseName.__add__(".ndb"), "r").read()
                    for x2 in range(childData.__len__()):
                        if childData[x2].__ne__(start__tag) and childData[x2].__ne__(child__end__tag) and childData[
                            x2].__ne__(end__tag):
                            readChild = readChild + childData[x2]
                        if childData[x2].__eq__(child__end__tag):
                            if childMatch == "true":
                                check = __self__child__.__self__child__(databaseName + ">" + readChild + ">" + value)
                                if check == "true":
                                    if query_child_name == "":
                                        query_child_name = [readChild]
                                    else:
                                        query_child_name.append(readChild)

                            readChild = ""
                            childMatch = "true"
                        if childData[x2].__eq__(value__child__tag):
                            childMatch = "false"
                        elif childMatch == "true":
                            updateNDB = updateNDB + childData[x2]
                        if x2.__eq__(len(childData) - 1):
                            if childMatch == "true":

                                check = __self__child__.__self__child__(databaseName + ">" + readChild + ">" + value)
                                if check == "true":
                                    if query_child_name == "":
                                        query_child_name = [readChild]
                                    else:
                                        query_child_name.append(readChild)

                                return query_child_name
                            else:
                                if query_child_name == "":
                                    return "'" + value + "' query child not found"
                                else:
                                    return query_child_name

    def __len__(self):
        pass
