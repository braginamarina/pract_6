def magic(day, month, year):
    if day * month == year % 100:
        return True
    else:
        return False


date = input("введите дату (дд.мм.гггг): ")
parts = date.split(".")

day = int(parts[0])
month = int(parts[1])
year = int(parts[2])

print(magic(day, month, year))