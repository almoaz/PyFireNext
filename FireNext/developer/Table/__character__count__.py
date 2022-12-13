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

class __character__count__:
    def __character__count__(self):
        finalValue = ""

        for x in range(self.__len__()):

            value = self[x]
            if value != "0" and value != "1" and value != "2" and value != "3" and value != "4" and value != "5" and value \
                    != "6" and value != "7" and value != "8" and value != "9":
                count = finalValue.count(value, 0)
                if finalValue == "":
                    count = self.count(value, 0)
                    finalValue = value + " = " + str(count)
                elif count == 0:
                    count = self.count(value, 0)
                    finalValue = finalValue + "\n" + value + " = " + str(count)
            if x == len(self) - 1:
                for x1 in range(10):
                    count = self.count(str(x1), 0)
                    if count >= 1:
                        finalValue = finalValue + "\n" + str(x1) + " = " + str(count)

        return finalValue

    def __len__(self):
        pass