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


class __read__table__:
    def __read__table__(self):

        try:
            table = open(self.__add__(".nt")).read()
            value = ""
            value2 = ""
            table_data = ""
            # table_data = "Table name : " + str(Table_Name) + "    Total Character : " + str(len(table))
            if table.__len__() > 0:
                Cell_Size = 0
                for x in range(table.__len__()):
                    if table[x] != cel__end__tag and table[x] != col__start__tag and table[x] != col__end__tag \
                            and table[x] != row__start__tag and table[x] != row__end__tag:
                        value = value + table[x]
                    elif table[x] == cel__end__tag:
                        if value.__len__() > Cell_Size:
                            Cell_Size = value.__len__()
                        value = ""
                    elif table[x] == col__end__tag or table[x] == row__end__tag:
                        if value.__len__() > Cell_Size:
                            Cell_Size = value.__len__()
                        value = ""

                for x1 in range(table.__len__()):
                    if table[x1] != cel__end__tag and table[x1] != col__start__tag and table[x1] != col__end__tag \
                            and table[x1] != row__start__tag and table[x1] != row__end__tag:
                        value = value + table[x1]
                    elif table[x1] == col__start__tag and value2 != "" or table[x1] == row__start__tag and value2 != "":
                        table_data = table_data + value2 + "\n"
                        table_data = table_data + value.ljust(value2.__len__(), "-") + "\n"
                        value2 = ""

                    elif table[x1] == cel__end__tag:
                        value = value.ljust(Cell_Size + 3, " ")
                        value2 = value2 + value
                        value = ""
                    elif table[x1] == col__end__tag or table[x1] == row__end__tag:
                        value = value.ljust(Cell_Size + 3, " ")
                        value2 = value2 + value
                        value = ""
                    if x1 == table.__len__() - 1:
                        # print(value2)
                        table_data = table_data + value2 + "\n"
                        return table_data
        except:
            return "'error' " + '[' + self + ']' + " table not found"

    def __add__(self, param):
        pass