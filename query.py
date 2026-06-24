import chromadb
client = chromadb.Client()

# Create a collection
collection = client.get_or_create_collection(name="vehicles")

print("Collection created : ", collection.name)

#Add Data to collection
collection.add(
    documents=[
        "Car runs on land",
        "Plane runs in The sky",
        "Boat travels on water",
        "Bus is a public transport on road"
    ],
    ids=["car1", "plane1", "boat1", "bus1"],
)
#Query ther collection
results = collection.query(
    query_texts=["Which can carry more than 20 people?"],
    n_results=4
)

#Print the output
print (results)