import threading
import time
import random
from pymongo import MongoClient

def conectar_mongoDB():
    client = MongoClient('localhost', 27017)
    db = client.bancoiot
    return db.sensores

def gerar_temp():
    return round(random.uniform(30, 40), 2)

def sensor_temp(nome_sensor, intervalo, db_collection):
    while True:
        temperatura = gerar_temp()
        print(f'{nome_sensor} - Temperatura: {temperatura}')
        documeto = db_collection.find_one({'nome': nome_sensor})
        if documeto:
            db_collection.update_one({'nome': nome_sensor}, {'$set': {'temperatura': temperatura}})
            if temperatura >38:
                print(f'A temperatura do sensor {nome_sensor} está acima do limite!')
                db_collection.update_one({'nome': nome_sensor}, {'$set': {'sensorAlarmado': True}})
                break
        else:
            db_collection.insert_one({'nome': nome_sensor, 'temperatura': temperatura})
            if temperatura >38:
                print(f'A temperatura do sensor {nome_sensor} está acima do limite!')
                db_collection.update_one({'nome': nome_sensor}, {'$set': {'sensorAlarmado': True}})
                break
        time.sleep(intervalo)
        
        
def iniciar():
    db_collection = conectar_mongoDB()
    sensores = ['sensor0', 'sensor1', 'sensor2']
    intervalo = 5
    threads = []
    
    for sensor in sensores:
        t = threading.Thread(target=sensor_temp, args=(sensor, intervalo, db_collection))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        
if __name__ == '__main__':
    iniciar()
            
            