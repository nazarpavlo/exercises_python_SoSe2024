def teilbar (x,y):
    if y==0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif x==y:
        print("x und y sind gleich")
    elif x%y==0:
        print("x ist durch y teilbar")
    else:
        print("x ist nicht durch y teilbar")
        
    teilbar(10,0)