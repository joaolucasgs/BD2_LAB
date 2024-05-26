# main.py
from teacher_crud import TeacherCRUD
from query import Database

def main():
    db = Database("neo4j+s://0a5d70af.databases.neo4j.io", "neo4j", "jQ6UBFGAXzhiAk91lvEHhoPmMYXT_fn5gP-_lHY9A1c")
    teacher_crud = TeacherCRUD(db)

   
    teacher_crud.create("Chris Lima", 1956, "189.052.396-66")
    
    
    teacher = teacher_crud.read("Chris Lima")
    print(f"Teacher: {teacher}")

    
    teacher_crud.update("Chris Lima", "162.052.777-77")
    
   
    teacher = teacher_crud.read("Chris Lima")
    print(f"Updated Teacher: {teacher}")

    
    teacher_crud.delete("Chris Lima")
    
    db.close()

if __name__ == "__main__":
    main()
