from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

class ProductAnalyzer:
    def __init__(self, dados):
        self.dados = dados

    def total_vendas_por_dia(self):
        resultado = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        writeAJson(resultado, "Total de Vendas por dia")

    def produto_mais_vendido(self):
        resultado = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(resultado, "Produto mais vendido")

    def cliente_com_maior_gasto(self):
        resultado = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        writeAJson(resultado, "Cliente que mais gastou")

    def produtos_vendidos_acima_de_um(self):
        resultado = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 1}}},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade_vendida": {"$sum": "$produtos.quantidade"}}}
        ])
        writeAJson(resultado, "Produtos vendidos mais que 1")
