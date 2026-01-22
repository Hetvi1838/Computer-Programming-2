def area_perimtr():
    l=int(input("Enter the length of the rectangle:"))
    b=int(input("Enter the breadth of the rectangle:"))
    area=l*b
    per=2(l+b)
    if(area>per):
        print("The area of the rectangle is greater than its perimeter")
    else:
        print("The perimeter of the rectangle is greater than its area")


area_perimtr()
