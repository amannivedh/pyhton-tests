def paint_calc(height,width,cover):
    paint=round((height*width)/cover)
    print(f"You'll need {paint} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
# assuming one can could cover 5 sqmtr
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)