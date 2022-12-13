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


class __read__col__name__:
    def __read__col__name__(self):
        try:
            table = open(self.__add__(".nt"), "r").read()
            value = ""
            value2 = ""

            for x1 in range(table.__len__()):
                if table[x1] != cel__end__tag and table[x1] != col__start__tag and table[x1] != col__end__tag:
                    value = value + table[x1]

                elif table[x1] == cel__end__tag:
                    if value2 == "":
                        value2 = [value]
                    else:
                        value2.append(value)
                    value = ""
                elif table[x1] == col__end__tag:
                    if value2 == "":
                        value2 = [value]
                    else:
                        value2.append(value)
                    return value2
        except:
            return "'error' " + '[' + self + ']' + " table not found"

    def __add__(self, param):
        pass