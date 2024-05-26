from query import Database

class TeacherCRUD:
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.database.query(query, {"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t
        """
        return self.database.query(query, {"name": name})

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        """
        self.database.query(query, {"name": name, "newCpf": newCpf})

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        self.database.query(query, {"name": name})
