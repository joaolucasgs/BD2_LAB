from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer


def main():
    db = Database(database="mercado", collection="compras")
    db.resetDatabase()

    analyzer = ProductAnalyzer(db.collection)

    analyzer.produtos_vendidos_acima_de_um()

    analyzer.total_vendas_por_dia()
    analyzer.produto_mais_vendido()
    analyzer.cliente_com_maior_gasto()


if __name__ == "__main__":
    main()