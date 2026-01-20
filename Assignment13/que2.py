# Write a program which accepts radius of circle and prints area of circle
def areaOFcircle(r):
    return 3.14*(r*r)

def main():
    redius = int(input("Enter radius number : "))
    result = areaOFcircle(redius)
    print("Area of circle",result)

if __name__ == "__main__":
    main()