# CREATE A FUNCTION CALLED MAKE_ALBUM
def make_album(artist, album_title, number_songs=None):
    """THIS FUNCTION BUILDS A DICTIONARY OF AN ALBUM"""
    album = {
        'artist': artist,
        'album title': album_title
    }

    if number_songs:
        album['number of songs'] = number_songs
    return album

album = make_album('twenty one pilots', 'scaled and icy')
print(album)

album = make_album('lil dicky', 'professional rapper', 20)
print(album)

album = make_album('red hot chili peppers', 'californication')
print(album)

while True:
    print("\nTell me the name of an artist and an album of theirs. number of songs on the album is optional" )
    print("(Enter 'q' to quit.) ")

    a_name = input("Artist: ")
    if a_name == 'q':
        break

    al_name = input("Album: ")
    if al_name == 'q':
        break

    songs = input("Number of songs: (enter 'None' if you are not providing this info)")
    if songs == 'None':
        songs = None
    elif songs == 'q':
        break

    album_info = make_album(a_name, al_name, songs)
    print(album_info)