from lib.album_repository import *
from lib.album import *

'''
When we call album_repo #ALL
we get a list with all albums
'''

def test_all_return_a_list_of_albums(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository
    album = repository.all()
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]

'''
When we call find method 
we get a specific result set based on the condition we set
'''

def test_find_a_specific_album_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    album = repository.find(3)
    assert album == [
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
    ]
def test_create_a_new_album_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    repository.create(Album(13, 'Sufer Rosa', 1988, 1))
    album = repository.all()
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Sufer Rosa', 1988, 1)
    ]

def test_delete_album_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    repository.delete(2020)
    album = repository.all()
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]