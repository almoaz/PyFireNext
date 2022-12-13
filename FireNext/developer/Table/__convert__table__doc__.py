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
from FireNext.developer.Table.__read__col__name__ import __read__col__name__
from FireNext.developer.Table.__search__col__data__ import __search__col__data__
from FireNext.developer.Table.__search__data__ import __search__data__
from FireNext.developer.Table.__parent__update__ import __parent__update__
from FireNext.developer.Doc.__self__add__ import __self__add__


class __convert__table__doc__:

    def __convert__table__doc__(self, child):
        value_child = __read__col__name__.__read__col__name__(self)
        child_id = __search__col__data__.__search__col__data__(self, child)
        child = ""
        for x in child_id:
            for x1 in value_child:
                value = __search__data__.__search__data__(self, x, x1)
                value = x1 + value__child__tag + value
                if child == "":
                    child = value
                else:
                    child = child + devided__tag + value

            if child != "":
                __self__add__.__self__add__(x + ">" + child)
                __parent__update__.__parent__update__(self, x)

            child = ""
        return "true"
