
import csv
import helper_spotify





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
    sorted_ytview_songs = sort_songs(ed_songs, 0, ascending=True)


    print("Ed Songs")
    print("-------------")
    for song in sorted_ytview_songs:
        print(song[0], "\t", song[0])
