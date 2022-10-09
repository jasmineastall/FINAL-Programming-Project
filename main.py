import json
import random

def findBy(IDToFind, JSONObject, fieldToFind):
  songs = []
  for item in JSONObject:
    if item[fieldToFind].lower() == IDToFind.lower():
      songs.append(item)
  return songs

def newAccount():
  x = {
        "name": input("Please enter your name: "),
        "dob": input("Please enter your date of birth: "),
        "favourite-artist": input("Please enter your favourite artist: "),
        "favourite-genre": input("Please enter your favourite genre: ")
  }
  with open("account.json", "w") as openfile:
    json.dump(x, openfile, ensure_ascii=False, indent=4)
  print("Thank you for creating a new account. You are now able to use the music system.")
  return

def validateAccount():
    print("Please enter your name")
    name = input()
    print("")
    print("Please enter your date of birth")
    DoB = input()
    print("")
    with open("account.json") as openfile:
        userAccount = json.load(openfile)
    if name == userAccount["name"] and DoB == userAccount["dob"]:
        print("Hi " + name +
              ". Welcome to the music system. Your favourite genre is " +
              userAccount["favourite-genre"] +
              " and your favourite artist is " +
              userAccount["favourite-artist"])
        return True
    else:
        print("Sorry those details are incorrect")
    return False

def viewSongLibrary():
  with open("songLibrary.json", "r") as x:
    loadSongLibrary = json.load(x)
  displayPlaylist(loadSongLibrary)

def generateGenrePlaylist(genre):
  with open("songLibrary.json", "r") as y:
    loadSongLibrary = json.load(y)
  playlist = findBy(genre,loadSongLibrary,"genre")
  return playlist

def displayPlaylist(playlist):
  for song in playlist:
    print(song["ID"], "." , song["song-name"], ",", song["artist"], ",", song["genre"])

def findPlaylist(playlistName):
  with open("playlistLibrary.json", "r") as x:
    loadPlaylistLibrary = json.load(x)
    playlist = findBy(playlistName,loadPlaylistLibrary,"playlist-name")
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

#THIS DOESN'T WORK
def generateDurationPlaylist(seconds):
  viewSongLibrary()
  length = 0
	#while 1 == 1:
    #randomSong = songLibrary[random(1, songLibrary.length())]
	  #length = length + randomSong[“duration”]
	  #if length <= seconds then:
		  #newPlaylist = newPlaylist + randomSong["ID"]
	  #else:
		  #break
  #displayPlaylist(playlist)
  #savePlaylist(playlist)

def addSongToPlaylist(songID, playlist):
  with open("songLibrary.json", "r") as y:
    loadSongLibrary = json.load(y)
  song = findBy(songID,loadSongLibrary,"ID")
  playlist.append(song[0])
  return playlist

def createYourOwnPlaylist():
  print("How many songs would you like to add to your playlist? Please type a number between 1 and 20")
  numberOfSongs = input()
  playlist = []
  for i in range(0,int(numberOfSongs)):
    print("Enter song " + str(i+1) + " of " +numberOfSongs)
    viewSongLibrary()
    print("What song would you like to add to your playlist? Please type the number of your song:   ")
    songID = input()
    playlist = addSongToPlaylist(songID, playlist)
  savePlaylist(playlist)

def createArtistFile():
  viewSongLibrary()
  print("What artist would you like to choose to export their songs to a separate file?")
  artist = input()
  with open("songLibrary.json", "r") as y:
    loadSongLibrary = json.load(y)
  playlist = findBy(artist,loadSongLibrary,"artist")
  artist = artist.replace(" ", "_")
  with open(artist+".json", "w") as f:
    json.dump(playlist, f, ensure_ascii=False, indent=4)
  print("All the songs by " +artist+ " have been exported to the file " +artist+".json.")

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
   x = {
        "name": input("Please enter your name: "),
        "dob": input("Please enter your date of birth: "),
        "favourite-artist": input("Please enter your favourite artist: "),
        "favourite-genre": input("Please enter your favourite genre: ")
  }
  with open("account.json", "w") as openfile:
    json.dump(x, openfile, ensure_ascii=False, indent=4)
  print("Thank you for creating a new account. You are now able to use the music system.")
  return

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
        newAccount()
    else:
        print("Thank you for viewing the music system. Have a good day!")
        quit()

print("Here is the song library: \n")
viewSongLibrary()

while 1==1:
  print("\nWhat would you like to do?\nPress 1 for viewing the playlist library \nPress 2 for creating your own genre playlist \nPress 3 for creating your own duration playlist \nPress 4 for adding your own songs to the song library \nPress 5 for alphabetise the song library \nPress 6 for creating your own playlist \nPress 7 for exporting an artists songs to a separate file \nPress 8 if you would like to quit the program")
  choice = input()
  if choice == "1":
    viewPlaylistLibrary()
    else:
      1 == 1
  elif choice == "2":
    print("What genre would you like to generate a playlist on - pop, rock, indie or disco?")
    genre = input().lower()
    playlist = generateGenrePlaylist(genre)
    displayPlaylist(playlist)
    savePlaylist(playlist)
  elif choice == "3":
    print("Please enter a duration you would like to generate a playlist for in minutes:   ")
    minutes = input()
    seconds = minutes * 60
  elif choice == "4":
    d
  elif choice == "5":
    d
  elif choice == "6":
    createYouOwnPlaylist()
  elif choice == "7":
    createArtistFile()
  elif choice == "8":
    break
  else:
    for i in range(0,3):
      print("Sorry, the system doesn't understand what you've inputed. Please try again")

print("Thank you for choosing to use the music system today. See you again later!")