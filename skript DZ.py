# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 13:58:44 2022

@author: sklad_2
"""

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:admin@locaihost:5432/схема ДЗ №3.drawio')
engine

connection = engine.connect()

connection.execute("""import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:admin@locaihost:5432/схема ДЗ №3.drawio')
engine

# количество исполнителей в каждом жанре
connection.execute("""SELECT genre_id, COUNT(executors_id) FROM genres_executors
                   GROUP BY genre_id;
        """).fetchall()

# количество треков, вошедших в альбомы 2019-2020 годов        
connection.execute("""SELECT album_id, COUNT(track_id) FROM tracks_in_albums
                   WHERE year_of_release ('2018', '2019', '2020')
                   GROUP BY album_id;
        """).fetchall()
        
# средняя продолжительность треков по каждому альбому       
connection.execute("""SELECT album_id,track_id FROM tracks_in_albums
                   FROM tracks_in_albums FULL OUTER JOIN List_tracks
                   ON A.track_id = B.track_id 
                   WHERE track_id = (SELECT AVG(time) FROM List_tracks ); 
                   GROUP BY album_id;
        """).fetchall()

# все исполнители, которые не выпустили альбомы в 2020 году        
connection.execute("""SELECT executors_id, album_id FROM List_albums 
                   WHERE executors_id not in = (
                   SELECT executors_id, year_of_release = 2000 
                   FROM List_albums)
                   GROUP BY executors_id;
        """).fetchall()
# названия сборников, в которых присутствует конкретный исполнитель        
connection.execute("""SELECT nickname FROM cataloge_executors
                  JOIN tracks_in_collection ON List_tracks.track_id = tracks_in_collection.track_id
                  JOIN tracks_in_collection ON List_albums.album_id = tracks_in_collection.album_id
                  JOIN tracks_in_collection.album_id ON albums_executors.executors_id = tracks_in_collection.executors_id
                  JOIN tracks_in_collection ON cataloge_executors.nickname = tracks_in_collection.nickname
                  WHERE nickname = 'Гербер'
                  """).fetchall()


#6 название альбомов, в которых присутствуют исполнители более 1 жанра;
connection.execute("""SELECT album_name FROM List_albums
        JOIN List_albums ON albums_executors.executors_id = List_albums.executors_id 
        JOIN List_albums ON cataloge_executors.executors_id = List_albums.id.executors_id
        JOIN List_albums ON genres_executors.genres_id = List_albums.genres_id
        GROUP BY album_name, genres_id
        HAVING count(genres_id) > 1;
        """).fetchall()


#7 наименование треков, которые не входят в сборники;
connection.execute("""SELECT track_name FROM List_tracks 
        LEFT JOIN List_tracks ON tracks_in_collection = cd.track_id
        WHERE track_id IS NULL;
        """).fetchall()


#8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
connection.execute("""SELECT executors_id FROM cataloge_executors
        JOIN cataloge_executors ON albums_executors.album_id = cataloge_executors.album_id
        JOIN cataloge_executors.album_id ON List_albums.album_id = cataloge_executors
        JOIN cataloge_executors ON List_tracks.time = cataloge_executors.time
        WHERE cataloge_executors.time IN (SELECT MIN(time) FROM List_tracks)
        """).fetchall()


#9 название альбомов, содержащих наименьшее количество треков.
connection.execute("""SELECT album_name, FROM List_albums 
    JOIN album_name ON List_tracks.track_id = album_name.track_id
    GROUP BY album_name 
    HAVING count(album_name.track_id) in (
        SELECT COUNT (album_name.track_id)
        FROM List_albums
        ORDER BY count(t.id)\
        LIMIT 1)
    ''').fetchall()

