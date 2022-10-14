# imports json and random functions for use throughout the program
import json
import random


def findBy(IDToFind, JSONObject, fieldToFind):
    songs = []
    for item in JSONObject:
        if item[fieldToFind].lower() == IDToFind.lower():
            songs.append(item)
    return songs

#function which creates a new account for the user if they don't have one and saves the account info in account.json
def newAccount():
    name = input("Please enter your name: ")
    if name == "":
      return False
    dob = input("Please enter your date of birth: ")
    if dob == "":
      return False
    artist = input("Please enter your favourite artist: ")
    if artist == "":
      return False
    genre = input("Please enter your favourite genre: ")
    if genre == "":
      return False
    x = {
        "name": (name),
        "dob": (dob),
        "favourite-artist": (artist),
        "favourite-genre": (genre)
    }
    with open("account.json", "w") as openfile:
        json.dump(x, openfile, ensure_ascii=False, indent=4)
    print(
        "Thank you for creating a new account. You are now able to use the music system."
    )
    return True

# if user already has an account, this function will validate the account details they enter against the details already stored in the account.json file
def validateAccount():
    wrong = True
    print("Please enter your name")
    name = input()
    print("")
    if name == "":
      return False
    while wrong == True:
      print("Please enter your date of birth in the format DD/MM/YYYY")
      DoB = input()
      print("")
      wrong = False
      for character in DoB:
        ASCIIDoB = ord(character)
        if ASCIIDoB <47 or ASCIIDoB >58:
          wrong = True
      if wrong == True:
        print("Date of birth isn't valid.")
        print("")     
    with open("account.json") as openfile:
        userAccount = json.load(openfile)
    if (name.lower() == userAccount["name"].lower() or name.upper() == userAccount["name"].upper()) and DoB == userAccount["dob"]:
        print("Hi " + name + ". Welcome to the music system. Your favourite genre is " +userAccount["favourite-genre"] +" and your favourite artist is " +userAccount["favourite-artist"])
        return True
    else:
        print("Sorry those details are incorrect")
    return False

#function which loads and prints the song library
def viewSongLibrary():
    with open("songLibrary.json", "r") as x:
        loadSongLibrary = json.load(x)
    displayPlaylist(loadSongLibrary)


def generateGenrePlaylist(genre):
    with open("songLibrary.json", "r") as y:
        loadSongLibrary = json.load(y)
    playlist = findBy(genre, loadSongLibrary, "genre")
    return playlist

#function takes the variable playlist and displays the songs in it
def displayPlaylist(playlist):
    for song in playlist:
      print(song["ID"], ".", song["song-name"], ",", song["artist"], ",",song["genre"])


def findPlaylist(playlistName):
    with open("playlistLibrary.json", "r") as x:
        loadPlaylistLibrary = json.load(x)
        playlist = findBy(playlistName, loadPlaylistLibrary, "playlist-name")
    return playlist[0]["playlist"]


def savePlaylist(playlist):
    with open("playlistLibrary.json", "r") as x:
        loadPlaylistLibrary = json.load(x)
    PlaylistName = input("Please enter the name of the playlist:   ")
    k = {
        "playlist-name": (PlaylistName),
        "playlist": (playlist),
    }
    loadPlaylistLibrary.append(k)
    with open("playlistLibrary.json", "w") as x:
        json.dump(loadPlaylistLibrary, x, ensure_ascii=False, indent=4)


def displayPlaylistLibrary():
    with open("playlistLibrary.json", "r") as x:
        loadPlaylistLibrary = json.load(x)
        for playlist in loadPlaylistLibrary:
            print(playlist["playlist-name"])


def generateDurationPlaylist(seconds):
    newPlaylist = []
    with open("songLibrary.json", "r") as y:
      loadSongLibrary = json.load(y)
    length = 0
    while True:
      songNumber = random.randint(0, len(loadSongLibrary) - 1)
      randomSong = loadSongLibrary[songNumber]
      length = length + int(randomSong["song-length"])
      if length <= seconds:
        newPlaylist.append(randomSong)
      else:
        break
    displayPlaylist(newPlaylist)
    savePlaylist(newPlaylist)
    return


def addSongToPlaylist(songID, playlist):
    with open("songLibrary.json", "r") as y:
        loadSongLibrary = json.load(y)
    song = findBy(songID, loadSongLibrary, "ID")
    playlist.append(song[0])
    return playlist


def createYourOwnPlaylist():
    print(
        "How many songs would you like to add to your playlist? Please type a number between 1 and 20"
    )
    numberOfSongs = input()
    playlist = []
    for i in range(0, int(numberOfSongs)):
        print("Enter song " + str(i + 1) + " of " + numberOfSongs)
        viewSongLibrary()
        print(
            "What song would you like to add to your playlist? Please type the number of your song:   "
        )
        songID = input()
        playlist = addSongToPlaylist(songID, playlist)
    savePlaylist(playlist)


def createArtistFile():
    viewSongLibrary()
    print(
        "What artist would you like to choose to export their songs to a separate file?"
    )
    artist = input()
    with open("songLibrary.json", "r") as y:
        loadSongLibrary = json.load(y)
    playlist = findBy(artist, loadSongLibrary, "artist")
    artist = artist.replace(" ", "_")
    with open(artist + ".json", "w") as f:
        json.dump(playlist, f, ensure_ascii=False, indent=4)
    print("All the songs by " + artist + " have been exported to the file " +
          artist + ".json.")

# function displays the list of playlists and asks the user for an input of whether they would like to view the songs in any of the given playlists
def viewPlaylistLibrary():
    displayPlaylistLibrary()
    print("Would you like to view the songs in any of the playlists? Type yes or no")
    viewSongs = input()
    if viewSongs.lower() == "yes":
      print("Which playlist would you like to view songs for?")
      playlistName = input()
      playlist = findPlaylist(playlistName)
      displayPlaylist(playlist)


def addSongToLibrary():
    with open("songLibrary.json", "r") as openfile:
        loadSongLibrary = json.load(openfile)
    newID = len(loadSongLibrary) + 1
    x = {
        "ID": str(newID),
        "song-name": input("Please enter the song name: "),
        "artist": input("Please enter the artist: "),
        "genre": input("Please enter the genre: "),
        "song-length": input("Please enter the song length in seconds: ")
    }
    loadSongLibrary.append(x)
    with open("songLibrary.json", "w") as x:
        json.dump(loadSongLibrary, x, ensure_ascii=False, indent=4)
    return


def alphabetiseSongLibrary():
    with open("songLibrary.json", "r") as openfile:
        loadSongLibrary = json.load(openfile)
        sortedList = sorted(loadSongLibrary, key=lambda k: k["song-name"])
        displayPlaylist(sortedList)


print("Hello. Welcome to the music system where you can create, edit, and view playlists. To begin, do you already have an account with us? Type yes or no")
account = input()
print("")

accountValidated = False
if account.lower() == "yes":
    for i in range(0, 3):
        if validateAccount() == True:
            accountValidated = True
            break
          
if accountValidated == False or account.lower() == "no":
  print("Would you like to create a new account? Type yes or no")
  newAccount1 = input()
  if newAccount1.lower() == "yes":
    while newAccount() == False:
      print("The new account cannot be created. Please try again.")      
  else:
      print("Thank you for viewing the music system. Have a good day!")
      quit()
      
print("")
print("Here is the song library: \n")
viewSongLibrary()

while 1 == 1:
    print("\nWhat would you like to do?\nPress 1 for viewing the playlist library \nPress 2 for creating your own genre playlist \nPress 3 for creating your own duration playlist \nPress 4 for adding your own songs to the song library \nPress 5 for alphabetise the song library \nPress 6 for creating your own playlist \nPress 7 for exporting an artists songs to a separate file \nPress 8 if you would like to quit the program")
    choice = input()
    if choice == "1":
        viewPlaylistLibrary()
    elif choice == "2":
        print(
            "What genre would you like to generate a playlist on - pop, rock, indie or disco?"
        )
        genre = input().lower()
        playlist = generateGenrePlaylist(genre)
        displayPlaylist(playlist)
        savePlaylist(playlist)
    elif choice == "3":
        print(
            "Please enter a duration you would like to generate a playlist for in minutes:   "
        )
        minutes = int(input())
        seconds = minutes * 60
        generateDurationPlaylist(seconds)
    elif choice == "4":
        addSongToLibrary()
    elif choice == "5":
        alphabetiseSongLibrary()
    elif choice == "6":
        createYourOwnPlaylist()
    elif choice == "7":
        createArtistFile()
    elif choice == "8":
        break
    else:
        for i in range(0, 3):
            print(
                "Sorry, the system doesn't understand what you've inputed. Please try again"
            )

print(
    "Thank you for choosing to use the music system today. See you again later!"
)
