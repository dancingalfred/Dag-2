

def loop_up_and_down(range_to_loop):
    my_list = list(range(range_to_loop + 1))
    for number in my_list:
        print(number)
    my_list.reverse()
    for number in my_list:
        print(number)



loop_up_and_down(5)