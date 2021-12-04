import math

def floatInput(prompt, min = -math.inf, max = math.inf):
    while True:
        try:
            res = float(input(prompt))
            break
        except:
            print("Invalid Number!")

    if(res < min or res > max):
        return False

    return res

def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    while True:
        try:
            h = floatInput("Humidity (%)? ", 0, 100)
            if(h == False):
                raise Exception(f"Invalid Interval!")
            print("h:", h)
            break
        except Exception as e:
            print("ERROR: ", e)

    print("c) Try entering invalid values such as 23C or -274.")
    while True:
        try:
            t = floatInput("Temperature (Celsius)? ", min=-273.15)
            if (t == False):
                raise Exception(f"Invalid Interval!")
            print("t:", t)
            break
        except Exception as e:
            print("ERROR: ", e)

    # d) What happens if you uncomment this?
    # impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    main()
