from lib.album import *

'''
Test album class initialization 
'''

def test_album_class_initialize_title_release_year_artist_id():
    album = Album(1, 'Doolittle', 1989, 1)
    assert album.title == 'Doolittle'
    assert album.release_year == 1989
    assert album.artist_id == 1

'''
We can compare to identical albums
and  have them equal
'''
def test_equal_albums():
    album1 = Album(1, 'Doolittle', 1989, 1)
    album2 = Album(1, 'Doolittle', 1989, 1)
    assert album1 == album2

'''
We format album to string
'''

def test_format_album_str():
    album = Album(1, 'Doolittle', 1989, 1)
    assert str(album) == 'Album(1, Doolittle, 1989, 1)' 

