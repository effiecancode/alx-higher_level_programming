#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []

    for x in range(0, list_length):
        try:
            div = my_list_1[x] / my_list_2[x]
        except TypeError as err:
            print("wrong type")
            div = 0
        except ZeroDivisionError as err:
            print("division by 0")
            div = 0
        except IndexError as err:
            print("out of range")
            div = 0
        finally:
            newList.append(div)

    return (newList)
