# This is a program that is used to search and sort the given Albums.


"""Doc String
 The class Album should be created.
 Variable names for all the variables.
 Initialize the attributes of the class.
 Create the required methods and functions
 Sort all the albums by the number_of _songs.
 Print the albums"""


# This the the class Album.
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

# This is the __repr__  method, used to print the strings.
    def __repr__(self):
        return f"""Album name:{self.album_name},
          Songs: {self.number_of_songs},
            Artist: {self.album_artist}"""


# This the empty list for the albums.
albums1 = []


albums1.append(Album("AlbumA", 10, "ArtistA"))
albums1.append(Album("AlbumB", 12, "ArtistB"))
albums1.append(Album("AlbumC", 14, "ArtistC"))
albums1.append(Album("AlbumD", 16, "ArtistD"))
albums1.append(Album("AlbumE", 9, "ArtistE"))


# For loop to iterate through the album list.
for row in albums1:
    print(row, end=" ")
    print()


# The sorted function is used to sort the albums.
sorted(albums1, key=lambda Album: Album.number_of_songs)

print()
print(albums1)
print()


# This method is used to rearrange the order of the albums.
albums1[1], albums1[2] = albums1[2], albums1[1]

albums2 = []

albums2.append(Album("Album1", 9, "Artist1"))
albums2.append(Album("Album2", 16, "Artist2"))
albums2.append(Album("Album3", 16, "Artist3"))
albums2.append(Album("Album4", 16, "Artist4"))
albums2.append(Album("Album5", 16, "Artist5"))

for row in albums2:
    print(row, end=" ")
    print()

print(albums2)


# The extend function is used to extend the albums2 list.
albums2.extend(albums1)
print(albums2)

albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!..I Did it Again", 16, "Britney Spears"))

sorted(albums2, key=lambda Album: Album.album_name)

if 'Dark Side of the Moon' in albums2:
    index = albums2.index('Dark side of the Moon')
    print(f"The index is: {index}")
else:
    print("Invalid - album not found!")
