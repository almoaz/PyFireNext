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


class __update__data__:
    def __update__data__(self, Search_Id, Column_Name, Update_Data):
        try:
            queryPosition = 0
            queryPermit = "false"
            updateData = "false"
            table = open(self.__add__(".nt")).read()
            value = ""
            updateDB = ""
            for x in range(table.__len__()):
                if queryPermit == "false" or queryPermit == "null":
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
                        value = ""
                elif table[x] == col__end__tag and queryPermit == "false":
                    if value == Column_Name:
                        queryPosition = queryPosition + 1
                        queryPermit = "null"
                        value = ""

                    else:
                        return "'error' [" + Column_Name + "] column name not found"
                if table[x] == col__end__tag and queryPermit == "null":
                    queryPermit = "true"
                elif queryPermit == "true":
                    value = value + table[x]

                    if table[x] == row__end__tag:
                        data = ""
                        dataPosition = 0
                        for x1 in range(value.__len__()):
                            if value[x1] != row__start__tag and value[x1] != cel__end__tag and value[
                                x1] != row__end__tag:
                                data = data + value[x1]

                            elif value[x1] == cel__end__tag:
                                if data == Search_Id:
                                    updateData = "true"
                                    data = ""
                                    for x2 in range(value.__len__()):
                                        if value[x2] != row__start__tag and value[x2] != cel__end__tag and value[
                                            x2] != row__end__tag:
                                            data = data + value[x2]
                                        if value[x2] == row__start__tag:
                                            updateDB = updateDB + value[x2]
                                        elif value[x2] == cel__end__tag:
                                            dataPosition = dataPosition + 1
                                            if dataPosition == queryPosition:
                                                updateDB = updateDB + str(Update_Data) + cel__end__tag
                                                data = ""
                                            else:
                                                updateDB = updateDB + data + cel__end__tag
                                                data = ""
                                        if x2 == value.__len__() - 1:
                                            dataPosition = dataPosition + 1
                                            if dataPosition == queryPosition:
                                                updateDB = updateDB + str(Update_Data) + row__end__tag
                                                data = ""
                                            else:
                                                updateDB = updateDB + data + row__end__tag
                                                data = ""

                                    break

                                else:
                                    data = ""
                            elif value[x1] == row__end__tag:
                                if data == Search_Id:
                                    updateData = "true"

                                    data = ""
                                    for x2 in range(value.__len__()):
                                        if value[x2] != row__start__tag and value[x2] != cel__end__tag and value[
                                            x2] != row__end__tag:
                                            data = data + value[x2]
                                        if value[x2] == row__start__tag:
                                            updateDB = updateDB + value[x2]
                                        elif value[x2] == cel__end__tag:
                                            dataPosition = dataPosition + 1
                                            if dataPosition == queryPosition:
                                                updateDB = updateDB + str(Update_Data) + cel__end__tag
                                                data = ""
                                            else:
                                                updateDB = updateDB + data + cel__end__tag
                                                data = ""
                                        if x2 == value.__len__() - 1:
                                            dataPosition = dataPosition + 1
                                            if dataPosition == queryPosition:
                                                updateDB = updateDB + str(Update_Data) + row__end__tag
                                                data = ""
                                            else:
                                                updateDB = updateDB + data + row__end__tag
                                                data = ""

                                    break

                                else:
                                    data = ""
                            if x1 == value.__len__() - 1:
                                updateDB = updateDB + value

                        value = ""
                if x == table.__len__() - 1 and updateData == "false":
                    return "'error' [Search Id : " + Search_Id + "] not found"
                elif x == table.__len__() - 1:
                    table = open(self + ".nt", "w")
                    table.write(updateDB)
                    return "true"

        except:
            return "'error' " + '[' + self + ']' + " table not found"

    def __add__(self, param):
        pass