from pymongo import MongoClient
from database import Database

class MotoristaDAO:
    def __init__(self, database: str, collection: str):
        self.db = Database(database, collection)

    def create(self, motorista):
        try:
            res = self.db.collection.insert_one(motorista)
            print (res)
            print("Motorista criado!")
        except Exception as e:
            print("Houve um erro ao criar o motorista:", e)

    def get(self, filtro=None):
        try:
            if filtro:
                return self.db.collection.find_one(filtro)
            else:
                return list(self.db.collection.find())
        except Exception as e:
            print("Houve eu erro ao consultar mototorista:", e)
            return None

    def update(self, filtro, novos_valores):
        try:
            self.db.collection.update_one(filtro, {"$set": novos_valores})
            print("Motorista atualizado com sucesso!")
        except Exception as e:
            print("Houve um erro ao atualizar motorista:", e)

    def delete(self, filtro):
        try:
            self.db.collection.delete_one(filtro)
            print("Motorista deletado com sucesso")
        except Exception as e:
            print("Houve um erro ao deletar o motorista", e)