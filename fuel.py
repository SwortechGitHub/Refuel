def main():
    x,y = convert(fraction = input('Fraction: '))
    gauge(round(x*100/y))
    
def convert(fraction):
    while True:
        try: #int?
            x,y = fraction.split('/')
            x,y = int(x),int(y)
            if y != 0:
                if x<y and not y < 0:
                    return (x,y)
                else:
                    raise ValueError('y too big or too small')
            else:
                raise ZeroDivisionError('Division with 0')
        except ValueError:
            raise ValueError('Not a number')


def gauge(percentage):
    if 1 < percentage and 99 > percentage:
        return f"{percentage}%"
    elif 1 >= percentage:
        return("E")
    elif 99 <= percentage:
        return("F")
    else:
        return("Error")

if __name__ == "__main__":
    main()