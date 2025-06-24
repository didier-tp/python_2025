#pip install 

import asyncio
from pymongo import AsyncMongoClient

async def fetch_new_in_mongo():

    uri = "mongodb://localhost:27017"
    client = AsyncMongoClient(uri)

    try:
        database = client.get_database("news") # database name
        news_col = database.get_collection("news") # collection name (with s)

        query = { "title": "myNews" }
        my_news = await news_col.find_one(query)

        print(my_news)

        await client.close()

    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

# Run the async function
asyncio.run(fetch_new_in_mongo())