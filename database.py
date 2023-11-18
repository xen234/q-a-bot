from pymongo import MongoClient
import json

class SimpleFileDB:
    def __init__(self, path="./", name="base.json"):
        self.base_path = path + name
        with open(self.base_path, "w") as base:
            json.dump({"questions": []}, base)

    def _read_from_db(self):
        with open(self.base_path, "r") as base:
            user_list = json.load(base)
        return user_list

    def _write_to_db(self, data):
        with open(self.base_path, "w") as base:
            json.dump(data, base)

    def save_question(self, user_id, question):
        record = {"user_id": user_id, "question": question}
        question_list = self._read_from_db()
        question_list["questions"].append(record)
        self._write_to_db(question_list)


class SimpleMongoDB:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.qa_database

    def save_question(self, user_id, question: str):
        self.db.questions.insert_one({"user_id": user_id, "question": question})
      
