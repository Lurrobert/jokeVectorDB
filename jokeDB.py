import mlx

class VectorDB:
    def __init__(self):
        self.vector_db = []

    def add_vector(self, vector):
        self.vector_db.append(vector)

    def get_vector(self, index):
        return self.vector_db[index]
