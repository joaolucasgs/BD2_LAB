from pymongo import MongoClient
from bson.objectid import ObjectId
from schemaLivros import LivroSchema
def main():
    # Conecte-se ao banco de dados MongoDB
    try:
        client = MongoClient("localhost", 27017)
        database = client["Blibioteca"]
        collection = database["Livros"]
        livro_model = LivroSchema(collection)
        print("Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return

    while True:
        # Menu de opções
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Pesquisar Livro")
        print("3. Atualizar livro")
        print("4. Deletar livro")
        print("5. Sair")

        # Obter a escolha do usuário
        choice = input("Escolha uma opção: ")

        if choice == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano do livro: "))
            preco = float(input("Digite o preço do livro: "))
            livro_model.create(titulo, autor, ano, preco)
        elif choice == "2":
            livro_id = input("Digite o ID do livro: ")
            livro_model.readById(livro_id)
        elif choice == "3":
            livro_id = input("Digite o ID do livro: ")
            titulo = input("Digite o novo título do livro: ")
            autor = input("Digite o novo autor do livro: ")
            ano = int(input("Digite o novo ano do livro: "))
            preco = float(input("Digite o novo preço do livro: "))
            livro_model.update(livro_id, titulo, autor, ano, preco)
        elif choice == "4":
            livro_id = input("Digite o ID do livro que deseja excluir: ")
            livro_model.delete(livro_id)
        elif choice == "5":
            print("Saindo do Menu")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
