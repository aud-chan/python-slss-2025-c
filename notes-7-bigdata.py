# Big Data
# Author : Audrey
# 17 November

# Process files
# Ingest large data
# Make sense of data



def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)

    # print the first line of the file
    header_row = file.readline()

    # uncle_fatihs = 0
    # club_ilia = 0
    # pizza_hut = 0

    # # Get info about the fav pizza place
    # for line in file:
    #     # fav pizza is in column 5 (4 index)
    #     # each line is a string
    #     # split the string wherever a , is
    #     # convert from string -> list
    #     info = line.split(",")
    #     fave_pizza = info[4]
    #     if fave_pizza == "Uncle Fatih's":
    #         uncle_fatihs += 1
    #     elif fave_pizza == "Club Ilia":
    #         club_ilia += 1
    #     elif fave_pizza == "Pizza Hut":
    #         pizza_hut += 1

    # # Display results
    # print("--------------")
    # print("Result:")
    # print(f"Uncle Faiths")
    # # Print the rest of the lines of data
    # for line in file:
    #     print(line)

    mbc = 0
    cornerstone = 0

    for line in file:
        info = line.split(",")
        fav_burrito = info[5]
        if fav_burrito == " Guadelupe (MBC)":
            mbc += 1
        elif fav_burrito == "Quesada (Cornerstone)":
            cornerstone += 1

    if cornerstone > mbc:
        print("The most popular burrito place is Quesada (Cornerstone).")
    elif mbc > cornerstone:
        print("The most popular burrito place is Guadelupe (MBC).")
    elif mbc == cornerstone:
        print("It's a tie!")





    file.close()


if __name__ == "__main__":
    main()
