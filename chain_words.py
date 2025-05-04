def chain_words(text):


    arry = list()
    arr = list()
    check = False


    for index,value in enumerate(text.split()):
        if index+1 >= len(text.split()):
            break
        if len(text.split()[index]) == len(text.split()[index+1]):
            check = True
            arr.append(value)
        else:
            if check:
                arr.append(value)
                check = False
            if arr:
                arry.append(arr)
                arr = list()
    return arry



