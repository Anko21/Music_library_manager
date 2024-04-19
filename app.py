from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album import *
from lib.album_repository import *

class Application():
    # Connect to the database
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/music_library.sql")

    def run(self):
        print('Welcome to the music library manager!')
        print(
            '''What would you like to do? 
                1 - List all artists
                2 - List all albums'''
        )
        user_choice = int(input("Enter your choice(1 or 2):"))
        print(f'You choosed {user_choice}')

        if user_choice == 1:
            artist_repository = ArtistRepository(self.connection)
            artists = artist_repository.all()
            for artist in artists:
                print(artist)
        elif user_choice == 2 :
            albums_repository = AlbumRepository(self.connection)
            albums = albums_repository.all()
            for album in albums:
                print(album)

if __name__ == '__main__':
    app = Application()
    app.run()