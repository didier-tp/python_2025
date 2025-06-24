#pip install 

from pymongo import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)

try:
    database = client.get_database("news") # database name
    news_col = database.get_collection("news") # collection name (with s)

    query = { "title": "myNews" }
    my_news = news_col.find_one(query)

    print(my_news)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
