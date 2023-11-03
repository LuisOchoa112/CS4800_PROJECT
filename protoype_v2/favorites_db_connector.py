#this file will connect the favorites page to the database to retrieve the user's favorites meals
#Author: Luis O.


import sqlite3

# Function to list favorite meals for a user
def list_favorite_meals(user_id):
    conn = sqlite3.connect("favorite_meals.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM favorite_meals WHERE user_id=?", (user_id,))
    favorite_meals = cursor.fetchall()

    conn.close()
    return(favorite_meals)
