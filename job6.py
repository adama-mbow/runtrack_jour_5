def note(n):
    if n < 40:
        print ("ajourné")
    else:
        multiple_5 = (n // 5+1)*5
        if multiple_5 - n < 3:
            print (multiple_5)
        else:
            print (n)

        print("reussit")

note(39)