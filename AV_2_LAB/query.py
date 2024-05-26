from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

# Questão I

def get_teacher_by_name(database, name):
    query = """
    MATCH (t:Teacher {name: $name})
    RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
    """
    return database.query(query, {"name": name})

def get_teachers_starting_with(database, letter):
    query = """
    MATCH (t:Teacher)
    WHERE t.name STARTS WITH $letter
    RETURN t.name AS name, t.cpf AS cpf
    """
    return database.query(query, {"letter": letter})

def get_all_cities(database):
    query = """
    MATCH (c:City)
    RETURN c.name AS name
    """
    return database.query(query)

def get_schools_by_number(database, min_number, max_number):
    query = """
    MATCH (s:School)
    WHERE s.number >= $min_number AND s.number <= $max_number
    RETURN s.name AS name, s.address AS address, s.number AS number
    """
    return database.query(query, {"min_number": min_number, "max_number": max_number})

# Questão II

def get_youngest_and_oldest_teacher_birth_year(database):
    query = """
    MATCH (t:Teacher)
    RETURN max(t.ano_nasc) AS youngest_year, min(t.ano_nasc) AS oldest_year
    """
    return database.query(query)

def get_average_population(database):
    query = """
    MATCH (c:City)
    RETURN avg(c.population) AS average_population
    """
    return database.query(query)

def get_city_by_cep(database, cep):
    query = """
    MATCH (c:City {cep: $cep})
    RETURN replace(c.name, 'a', 'A') AS name
    """
    return database.query(query, {"cep": cep})

def get_teachers_name_character(database):
    query = """
    MATCH (t:Teacher)
    RETURN substring(t.name, 2, 1) AS character
    """
    return database.query(query)
