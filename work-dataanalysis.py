# Data Analysis
# Author: Alicia
# Analyse the data provided in class


def main():
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)
    file.readline()
    year = int(1869)
    for line in file:
        info = line.split(",")
        date = info[0].split("-")

        if int(date[0]) == year and date[1] == "06":
            total_temp = 0
            if info[5].strip():
                average = float(info[5])
                total_temp += average
            print(f"{year} {total_temp} deg")
            year += 1


if __name__ == "__main__":
    main()
