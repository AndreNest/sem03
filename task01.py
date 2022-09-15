def have_number(list_number:list, number) -> bool:
    have_number = False
    for str in list_number:
        for elem in str:
            if(elem == number):
                have_number = True
                print("Такой элемент есть!")
                break
    if have_number == False:
        print('Такого элемента нет!')
have_number(['fdg5', 'dfgrd7', '8', 'fdgdf', 'trr'], '5')
have_number(['fdg5', 'dfgrd7', '8', 'fdgdf', 'trr'], '1')