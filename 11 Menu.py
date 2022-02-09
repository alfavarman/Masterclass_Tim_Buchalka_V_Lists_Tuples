from nested_data import albums
SONGS_LIST = 3

while True:
    print("Select Album From List Below: WRONG INPUT WILL TERMINATE APP::")
    for index,(album, author, year, songs_list) in enumerate(albums):
            print("{}: {}".format(index + 1, album))

    selected_album = int(input())
    if 1 <= selected_album <= len(albums[0]):
        print('Selected Album >{}< Please Select Song:'.format(albums[selected_album - 1][0]))

    for selected_album, (song_index, song_title) in enumerate(albums[selected_album-1][SONGS_LIST]):
        print('{}: {}'.format(song_index, song_title))
    selected_song = int(input())

    if 1 <= selected_song <= len(albums[selected_album][SONGS_LIST]):
        print('=' * 60)
        print('Playing Song:: {}'.format(albums[selected_album][SONGS_LIST][selected_song-1][1]))
        print('=' * 60)
        input()

    else:
        print()

