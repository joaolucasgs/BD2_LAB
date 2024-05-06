class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (:Player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id, result):
        query = "CREATE (:Match {id: $match_id, result: $result})"
        parameters = {"match_id": match_id, "result": result}
        self.db.execute_query(query, parameters)

    def add_player_to_match(self, player_id, match_id):
        query = """
        MATCH (p:Player {id: $player_id})
        MATCH (m:Match {id: $match_id})
        MERGE (p)-[:PARTICIPATED_IN]->(m)
        """
        parameters = {"player_id": player_id, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def update_player_name(self, player_id, new_name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_match_result(self, match_id, new_result):
        query = "MATCH (m:Match {id: $match_id}) SET m.result = $new_result"
        parameters = {"match_id": match_id, "new_result": new_result}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.id AS id, m.result AS result"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "result": result["result"]} for result in results]

    def get_player_matches(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m.id AS id, m.result AS result
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"id": result["id"], "result": result["result"]} for result in results]

    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)