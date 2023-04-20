import unittest
import json
import pathlib
from fastapi.testclient import TestClient
from main import app
# from mongodb import Mongo
# from config import Settings

# settings = Settings()
# mongo = Mongo(settings)

# app.config = settings
# app.mongodb_client = mongo

client = TestClient(app)

# f = open(f'{pathlib.Path(__file__).parent}/json/all_movies.json')
# all_movies_data = json.load(f)
# f.close()

class TestAPI(unittest.TestCase):

    def test_get_all(self):
        response = client.get("/api/v1/movies")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['description'], "Response all movies")
        self.assertLessEqual(data['count'], 100)
        self.assertLessEqual(len(data['result']), 100)
        # self.assertEqual(data, all_movies_data)

    def test_get_by_id(self):
        response = client.get("/api/v1/movies/643efea592bd889b46754918")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['description'], "Reponse movies by id")
        self.assertEqual(data['result']['id'], 315162)
        self.assertEqual(data['result']['title'], "Puss in Boots: The Last Wish")


# if __name__ == '__main__':
#     unittest.main()
# python -m unittest discover -v -s tests -p "*.test.py"