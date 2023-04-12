from faker import Faker
import mysql.connector
import random
import string


def generate_songs(country_code_list, database):
    '''Generate songs'''
    fake = Faker()
    for i in range(8000):
        song_ID = i + 1
        title = fake.catch_phrase()
        artist = fake.name()
        genre = random.choice(['Rock', 'Pop', 'Hip Hop', 'Jazz',
                               'Classical', 'RNB', 'Country', 'EDM', 'Folk', 'Metal', 'Reggae', 'Soul', 'Blues', 'Punk'])
        release_date = fake.date_between(start_date='-50y', end_date='today')
        city_id = random.randint(1, 4079)
        country_code = country_code_list[city_id]
        ranking = random.randint(1, 10)
        # table layout ID, Title, Artist, Genre, ReleaseDate, CityID, CountryCode, Ranking
        song_data = (song_ID, title, artist, genre, release_date.strftime(
            '%Y-%m-%d'), city_id, country_code, ranking)
        add_song = ("INSERT INTO Music " "(ID, Title, Artist, Genre, ReleaseDate, CityID, CountryCode, Ranking) " "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor = database.cursor()
        cursor.execute(add_song, song_data)
        database.commit()
    cursor.close()


def main():
    '''Sql funniest joke ever'''
    # connect to mysql, change password to your own
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tempWord21!",
    )

    # create a cursor object
    cursor = mydb.cursor()
    # use world database
    cursor.execute("USE world;")
    city_id_country_code = {}
    # get all city ids and country codes from data.txt
    with open('data.txt', 'r') as f:
        for line in f:
            city_id, country_code = line.split()
            city_id_country_code[int(city_id)] = country_code

    # Generate songs
    generate_songs(city_id_country_code, mydb)


if __name__ == "__main__":
    main()
