import chromadb

# Create an in-memory Chroma client (no persistence — good for demos/testing)
client = chromadb.Client()

# Create (or reuse) a collection to store our vehicle documents
collection = client.get_or_create_collection(name="vehicles")

# Add data — longer, more descriptive documents give the embedding model
# more context to work with, which usually improves match quality.
collection.add(
    documents=[
        "A car is a wheeled motor vehicle that runs on land, "
        "typically used for personal transportation on roads and highways.",

        "A plane, or airplane, is an aircraft that flies through the sky "
        "at high altitude, powered by jet engines or propellers, "
        "used for fast long-distance travel.",

        "A boat is a watercraft that travels on rivers, lakes, or the sea, "
        "used for fishing, transport, or leisure on water.",

        "A bus is a large public transport vehicle that runs on roads, "
        "carrying many passengers along fixed routes in cities and towns.",

        "A train runs on rails and is used for transporting passengers "
        "or freight over land, often between cities.",

        "A bicycle is a human-powered, two-wheeled vehicle used for "
        "short-distance travel and exercise on roads or trails.",

        "A submarine is a vehicle that travels underwater, used for "
        "naval operations, research, or exploration beneath the sea.",

        "A helicopter is an aircraft that can take off and land vertically, "
        "flying through the sky using rotating blades instead of fixed wings.",
    ],
    ids=[
        "car1", "plane1", "boat1", "bus1",
        "train1", "bicycle1", "submarine1", "helicopter1",
    ],
)

print("Vehicle Search System")
print("Type 'exit' to quit.\n")

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question.strip():
        print("Please enter a question.\n")
        continue

    # Query the collection for the top N semantically closest documents
    results = collection.query(
        query_texts=[question],
        n_results=3  # bumped up since we now have more documents
    )

    docs = results["documents"][0]
    ids = results["ids"][0]
    distances = results.get("distances", [[None] * len(docs)])[0]

    print("\nTop Matches:")
    for doc_id, doc, dist in zip(ids, docs, distances):
        dist_str = f" (distance: {dist:.4f})" if dist is not None else ""
        print(f"- {doc_id}{dist_str}: {doc}")
    print()