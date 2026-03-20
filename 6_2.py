def divide(x):
    return 100 / x


try:
    n = int(input("введите число: "))
    result = divide(n)
    print(result)

except ValueError:
    print("вы ввели не число")

except ZeroDivisionError:
    print("нельзя делить на нооль")

except:
    print("другая ошибка")