

from random import choice
from tempfile import tempdir

def main():
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)

    header_row = file.readline()
    data_points = 0

    total_temp = 0
    total_june_temp = 0

    # for line in file:
    #     data_points += 1
    # print(f"Number of points is: {data_points}")

    # average rainfall
    total = 0
    for line in file:
        # count how many data points we have
        data_points += 1
        info = line.split(",")
        rain = (float(info[1]))
        total += rain

        # get info
        if info[-2]:
            min_temp = (float(info[-2]))
            total_temp += min_temp

        if info[-2]:
            min_temp = (float(info[-2]))
            total_temp += min_temp
            # convert to celsius


            june = (float(info[0]))
            info = line.split("-")
            if june in file:
                if info[-1]:
                    max_temp = (float(info[-1]))
                    total_june_temp += max_temp






    average = total/data_points
    print(f"The average rainfall is {average}")

    average_temp = total_temp/data_points
    print(f"The average minimum temperature is {average_temp}")

    total_temp_celsius = (total_temp - 32) / 1.8
    print(f"The average minimum temperature in celsius is: {total_temp_celsius}")

    average_june = total_june_temp/data_points
    print(f"The average ")

    file.close()







if __name__ == "__main__":
    main()
