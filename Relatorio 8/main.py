from database import Database
from game_database import GameDatabase

db = Database("neo4j+s://0a5d70af.databases.neo4j.io", "neo4j", "jQ6UBFGAXzhiAk91lvEHhoPmMYXT_fn5gP-_lHY9A1c")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("player1", "Joao")
game_db.create_player("player2", "Lucas")
game_db.create_match("match1", "Joao Ganhou")
game_db.create_match("match2", "Lucas Ganhou")

game_db.add_player_to_match("player1", "match1")
game_db.add_player_to_match("player2", "match1")
game_db.add_player_to_match("player2", "match2")

game_db.update_player_name("player1", "Hulk")
game_db.update_match_result("match2", "Hulk ganhou")