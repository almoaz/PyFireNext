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

from FireNext.developer.Table.__tag__ import *


class __delete__col__name__:
    def __delete__col__name__(self, Column_Name):
        try:
            queryPosition = 0
            queryPermit = "false"
            table = open(self.__add__(".nt")).read()
            value = ""
            updateDB = ""
            for x in range(table.__len__()):
                if queryPermit == "false" and table[x] == col__start__tag or queryPermit == "null" and table[
                    x] == col__start__tag:
                    updateDB = updateDB + table[x]
                if queryPermit == "null" and table[x] != col__end__tag:
                    updateDB = updateDB + table[x]
                if table[x] != col__start__tag and table[x] != cel__end__tag and table[
                    x] != col__end__tag and queryPermit == "false":
                    value = value + table[x]
                elif table[x] == cel__end__tag and queryPermit == "false":
                    if value == Column_Name:
                        queryPosition = queryPosition + 1
                        queryPermit = "null"
                        value = ""

                    else:
                        queryPosition = queryPosition + 1
                        updateDB = updateDB + value + cel__end__tag
                        value = ""
                elif table[x] == col__end__tag and queryPermit == "false":
                    if value == Column_Name:
                        queryPosition = queryPosition + 1
                        updateDB = updateDB[:-1]
                        queryPermit = "null"

                        value = ""

                    else:
                        return "'error' " + "[" + Column_Name + "]" + " Column name not found"
                if table[x] == col__end__tag and queryPermit == "null":
                    updateDB = updateDB + value + col__end__tag
                    queryPermit = "true"
                elif queryPermit == "true":

                    updateDB = updateDB + table[x]
                if x == len(table) - 1:
                    table = open(self + ".nt", "w")
                    table.write(updateDB)
                    return "true"
        except:
            return "'error' " + '[' + self + ']' + " table not found"

    def __add__(self, param):
        pass