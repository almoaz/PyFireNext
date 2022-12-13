from FireNext.Table.__tag__ import *


class __search__row__data__:
    def __search__row__data__(self, Search_Id):
        try:
            queryPermit = "false"
            table = open(self.__add__(".nt")).read()
            value = ""
            col_name = ""
            for x in range(table.__len__()):
                if queryPermit == "false":
                    col_name = col_name + table[x]

                if table[x] == col__end__tag and queryPermit == "false":
                    queryPermit = "true"
                elif queryPermit == "true":

                    value = value + table[x]

                    if table[x] == row__end__tag:
                        data = ""
                        for x1 in range(value.__len__()):
                            if value[x1] != row__start__tag and value[x1] != cel__end__tag and value[
                                x1] != row__end__tag:
                                data = data + value[x1]

                            elif value[x1] == cel__end__tag:
                                if data == Search_Id:
                                    Cell_Size = 0
                                    value2 = ""
                                    for x2 in range(value.__len__()):
                                        if value[x2] != cel__end__tag and value[x2] != row__start__tag and value[
                                            x2] != row__end__tag:
                                            value2 = value2 + value[x2]
                                        elif value[x2] == cel__end__tag:
                                            if value2.__len__() > Cell_Size:
                                                Cell_Size = value2.__len__()
                                            value2 = ""
                                        elif value[x2] == row__end__tag:
                                            if value2.__len__() > Cell_Size:
                                                Cell_Size = value2.__len__()
                                            value2 = ""
                                    col_name = col_name + value
                                    value = ""
                                    value2 = ""
                                    for x2 in range(col_name.__len__()):
                                        if col_name[x2] != cel__end__tag and col_name[x2] != col__start__tag and \
                                                col_name[
                                                    x2] != col__end__tag \
                                                and col_name[x2] != row__start__tag and col_name[x2] != row__end__tag:
                                            value = value + col_name[x2]
                                        elif col_name[x2] == row__start__tag and value2 != "":
                                            print(value2)
                                            print(value.ljust(value2.__len__(), "-"))
                                            value2 = ""

                                        elif col_name[x2] == cel__end__tag:
                                            value = value.ljust(Cell_Size + 3, " ")
                                            value2 = value2 + value
                                            value = ""
                                        elif col_name[x2] == col__end__tag or col_name[x2] == row__end__tag:
                                            value = value.ljust(Cell_Size + 3, " ")
                                            value2 = value2 + value
                                            value = ""
                                        if x2 == col_name.__len__() - 1:
                                            return value2
                                    break

                                else:
                                    data = ""
                            elif value[x1] == row__end__tag:
                                if data == Search_Id:
                                    Cell_Size = 0
                                    value2 = ""
                                    for x2 in range(value.__len__()):
                                        if value[x2] != cel__end__tag and value[x2] != row__start__tag and value[
                                            x2] != row__end__tag:
                                            value2 = value2 + value[x2]
                                        elif value[x2] == cel__end__tag:
                                            if value2.__len__() > Cell_Size:
                                                Cell_Size = value2.__len__()
                                            value2 = ""
                                        elif value[x2] == row__end__tag:
                                            if value2.__len__() > Cell_Size:
                                                Cell_Size = value2.__len__()
                                            value2 = ""
                                    col_name = col_name + value
                                    value = ""
                                    value2 = ""
                                    for x2 in range(col_name.__len__()):
                                        if col_name[x2] != cel__end__tag and col_name[x2] != col__start__tag and \
                                                col_name[
                                                    x2] != col__end__tag \
                                                and col_name[x2] != row__start__tag and col_name[x2] != row__end__tag:
                                            value = value + col_name[x2]
                                        elif col_name[x2] == row__start__tag and value2 != "":
                                            print(value2)
                                            print(value.ljust(value2.__len__(), "-"))
                                            value2 = ""

                                        elif col_name[x2] == cel__end__tag:
                                            value = value.ljust(Cell_Size + 3, " ")
                                            value2 = value2 + value
                                            value = ""
                                        elif col_name[x2] == col__end__tag or col_name[x2] == row__end__tag:
                                            value = value.ljust(Cell_Size + 3, " ")
                                            value2 = value2 + value
                                            value = ""
                                        if x2 == col_name.__len__() - 1:
                                            return value2
                                    break
                        if x == table.__len__() - 1:
                            return "'error' [Search id : " + Search_Id + "] not found"
                        value = ""

        except:
            return "'error' " + '[' + self + ']' + " table not found"

    def __add__(self, param):
        pass