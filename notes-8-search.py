# Intro to Search
# Author: Audrey
# 25 November

import csv
from random import normalvariate

# Introduction to search algorithms
# Search for all songs by "Kendrick"
# Display all the YouTube and TikTok views
# Sort by either Youtube or TikTok views

def main():
    track_col = 0
    track_col_2 = 0
    song_name_col = 0
    artist_col = 2
    artist_col_two = 2
    yt_views_col = 11
    yt_views_two = 11
    tiktok_views_col =  15
    tiktok_views_two = 15
    artist = "Kendrick Lamar"
    artist_two = "Taylor Swift"
    kendrick_songs = []
    taylor_songs = []

    # open the file
    with open("data/spotify2024.csv") as f:
    # get rid of the header row
        _ = f.readline()

    # create a reader object
        r = csv.reader(f)

        for info in r:  # go thorugh the reader line by line
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                kendrick_songs.append(info)
            #  do something with it
            elif info[artist_col_two] == artist_two:
                taylor_songs.append(info)

            print(f"Number of Kendrick Songs: {len(kendrick_songs)}")
            print(f"Number of Taylor Songs: {len(taylor_songs)}")


        #  for every song in kendrick_songs
        for song in kendrick_songs:
            current_trackname = song[track_col]
            current_ytviews = song[yt_views_col]
            current_ttviews = song[tiktok_views_col]

            print(f"{current_trackname}.strip\t\t{current_ytviews}\t\t{current_ttviews}")

        for song in taylor_songs:
            current_trackname_two = song[track_col]
            current_ytviews_two = song[yt_views_two]
            current_ttviews_two = song[tiktok_views_two]
            # display information in a clear way
            # track name        yt views        tt views
            # Squabble up       100,000,000     120,000,000
            print(f"{current_trackname_two}\t\t{current_ytviews_two}\t\t{current_ttviews_two}")

        exp_track = 0
        for song in kendrick_songs:
            info_track = song[-1]
            if info_track == "1":
                exp_track += 1

        print(f"The amount of explicit tracks is: {exp_track}")
        # print(f"The amount of non-explicit tracks is: {no_exp_track}")

        exp_track_2 = 0
        for song in taylor_songs:
           info_track_2 = song[-1]
           if info_track_2 == "1":
               exp_track_2 += 1

        print(f"The amount of explicit tracks for T is: {exp_track_2}")
       # print(f"The amount of non-explicit tracks is: {no_exp_track}")




if __name__ == "__main__":
    main()
