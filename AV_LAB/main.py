from database import Database
from motoristaCLI import MotoristaCLI
from motoristaDAO import MotoristaDAO

def main():
    #NO ARQUIVO SCHEMA.JSON ESTA O SCHEMA QUE COPIEI DIRETAMENTE DO COMPASS
    db = Database(database="AV01", collection="Motoristas")

   
    motorista_dao = MotoristaDAO("AV01", "Motoristas")

    
    motorista_cli = MotoristaCLI(motorista_dao)

    
    motorista_cli.run()

if __name__ == "__main__":
    main()
