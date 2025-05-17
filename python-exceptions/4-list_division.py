#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    n_list = []
    while i != list_length:
        try:
            n_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            n_list.append(0)
            print("division by 0")
        except TypeError:
            n_list.append(0)
            print("wrong type")
        except IndexError:
            n_list.append(0)
            print("out of range")
        finally:
            i += 1
    return n_list
