from vector_space import VectorSpace

vector_space = VectorSpace(["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."])
print("start")
print(vector_space.search(["cat"]))
print(vector_space.ralated(0))