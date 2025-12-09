# Intro to Sort
# Author: Audrey
# 4 December

import csv
import helper_spotify
# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order

# def selection_sort(l: list[int], ascending=True) -> list[int]:
#     """Sorts a given list using selection sort
#     Params:
#         l - list of numbers to sort
#         ascending - True if sorting in ascending order
#     Returns:
#         a sorted list
#     """
    # # Starting at the beginning of the list
    # candidate_num = 0
    # candidate_index = 0

    # num_items = len(l)
    # for i in range(num_items):
    #     # set the lowest_num to the current number
    #     candidate_num = l[i]
    #     # set the lowest_index to the current index
    #     candidate_index = i

    #     # check the rest of the list
    #     for j in range(i+1, num_items):
    #         if ascending:
    #             # if this number is smaller than the lowest
    #             if l[j] < candidate_num:
    #                 # set the lowest_num to this number
    #                 candidate_num= l[j]
    #                 # set the lowest_index to this index
    #                 candidate_index = j
    #             # go to the next number until we get to the end - happens automatically
    #         # if this number is smaller than the lowest
    #            else:
                     # if l[j] > candidate_num:
    #                 candidate_num = l[j]
    #                 candidate_index = j
    #             # set the lowest_num to this number
    #             candidate_num = l[j]
    #             # set the lowest_index to this index
    #             candidate_index = j
    #         # go to the next number until we get to the end - happens automatically


    #     # swap the current number with the number at the lowest index
    #     l[i], l[candidate_index] = l[candidate_index], l[i]

def selection_sort(l: list[int], ascending=True) -> list[int]:
        """Sorts a given list using selection sort
        Params:
            l - list of numbers to sort
            ascending - True if sorting in ascending order
        Returns:
            a sorted list
        """
        num_items = len(l)

        # starting at the beginning of the list
        for i in range(num_items):
            lowest_num = l[i]
            lowest_index = i

            # check the rest of the list
            for j in range(i+1, num_items):
                if l[j] < lowest_num:
                    lowest_num = l[j]
                    lowest_index = j

            # swap the current number with the number at the
            # lowest index
            l[i], l[lowest_index] = l[lowest_index], l[i]


        return l

def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
    songs - list of songs
    col - column to sort
    ascending - will sort ascending by default

    Returns: sorted list"""
    # Get songs from an artist

    # Use Selection Sort to sort songs


    num_songs = len(songs)
    # Starting at the beginning of the list (songs)
    for i in range(num_songs):  # i represents where we currently are with the index
        # This value is the candidate
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        # This index is the candidate
        candidate_index = i
         # Check the rest of the list
        for j in range(i+1, num_songs):
            this_songs_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                # Is this value lower than the candidate
                if this_songs_val < candidate_val:
                    # Mark this number as the candidate
                    candidate_val = this_songs_val
                    # Mark this index as the candidate location
                    candidate_index = j
            # If descending
            else:
                # Is this value higher than the candidate
                if this_songs_val > candidate_val:
                    # Mark this number as the candidate
                    candidate_val = this_songs_val
                    # Mark this index as the candidate
                    candidate_index = j
            # Swap the candidate with the current index
        songs[i], songs[candidate_index] = songs[candidate_index], songs[i]
    return songs


if __name__ == "__main__":
    # sorted_list = selection_sort([1, 43, 55, -11, 100, 34])
    # Get a list of all songs from "Ed Sheeran"
    ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    # artist -> col 11
    sorted_ytview_songs = sort_songs(ed_songs, 11, ascending=True)


    print("Ed Songs")
    print("-------------")
    for song in sorted_ytview_songs:
        print(song[0], "\t", song[11])




if __name__ == "__main__":
    # sorted_list = selection_sort([1, 43, 55, -11, 100, 34])
    # Get a list of all songs from "Ed Sheeran"
    ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    # artist -> col 11
    sorted_ttview_songs = sort_songs(ed_songs, 15, ascending=False)
    print("------------")

    print("Tiktok Views ")
    print("-------------")
    for song in sorted_ttview_songs:
        print(song[0], "\t", song[15])
