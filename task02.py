def check_doble(list_element, searh_str):
    count = 0
    for i in range(len(list_element)):
        if searh_str == list_element[i]:
            count += 1
        if count == 2:
            print(f"Есть такой элемент = {i}")
            break

check_doble(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe")
        

