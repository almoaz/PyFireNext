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


class __parent__update__:
    def __parent__update__(self, child):
        try:
            database = open(self + ".ndb", "r").read()
            value = ""
            updateDB = ""
            child_update = "false"
            for x2 in range(database.__len__()):
                if database[x2] != start__tag and database[x2] != child__end__tag and database[
                    x2] != end__tag:
                    value = value + database[x2]
                if database[x2] == child__end__tag:
                    if child == value:
                        child_update = "true"
                        if updateDB == "":
                            updateDB = value + child__end__tag
                        else:
                            updateDB = updateDB + value + child__end__tag
                    else:
                        if updateDB == "":
                            updateDB = value + child__end__tag
                        else:
                            updateDB = updateDB + value + child__end__tag
                    value = ""
                if x2 == len(database) - 1:
                    if child != value:
                        if child_update == "false":
                            updateDB = updateDB + value + child__end__tag + child
                        else:
                            updateDB = updateDB + value
                    if child == value:
                        if updateDB == "":
                            updateDB = value
                        else:
                            updateDB = updateDB + value

            open(self + ".ndb", "w").write(start__tag + updateDB + end__tag)

        except:
            open(self + ".ndb", "w").write(start__tag + child + end__tag)