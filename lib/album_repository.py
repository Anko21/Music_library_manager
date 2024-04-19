from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def find(self,artist_id):
        rows = self.connection.execute(
            'SELECT * from albums WHERE artist_id = %s', [artist_id]
        )
        albums = []
        for row in rows:
            item = Album(row['id'], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)

        return albums
    
    def create(self, album):
        self.connection.execute(
            'INSERT INTO albums (id, title, release_year, artist_id) VALUES(%s,%s,%s,%s)',[
                album.id, album.title, album.release_year, album.artist_id
            ]
        )
    def delete(self, release_year):
        self.connection.execute(
            'DELETE FROM albums WHERE release_year = %s', [release_year]
        )
        