def run():
    cuadrados_div_ = []
    for i in range(1,101):
        if i % 3 != 0:
            cuadrados_div_.append(i**2)
    


    list_comprehension =  [i**2 for i in range(1,101) if i % 3 !=0]

    print(list_comprehension)




if __name__== "__main__":
    run()
