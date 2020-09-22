#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_div_list = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except (TypeError, ValueError):
            division = 0
            print("wrong type")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            final_div_list.append(division)
    return final_div_list
