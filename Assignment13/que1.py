# Write a program which accepts length and width of rectangle and prints area
def areaOFrect(l, w):
    return l * w

def main():
    length = int(input("Enter lenght number : "))
    width = int(input("Enter width number : "))
    result = areaOFrect(length,width)
    print("area of rectangle ",result)

if __name__ == "__main__":
    main()