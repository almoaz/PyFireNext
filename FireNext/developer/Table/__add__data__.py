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


class __add__data__:
    def __add__data__(self, Data):
        try:
            table = open(self.__add__(".nt"))
            if len(table.read()) < 4:
                return "'error' column name not found\nbefore add data we need to add column name"
            else:
                value = ""
                for x in range(Data.__len__()):
                    if Data[x] == "|":
                        value = value + cel__end__tag
                    else:
                        value = value + Data[x]
                open(self + ".nt", "a").write(row__start__tag + value + row__end__tag)
                return "true"
        except:
            return "'error' " + '[' + self + ']' + " table not found"

    def __add__(self, param):
        pass