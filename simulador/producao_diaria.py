import pandas as pd
import random
import json
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')

taxa_escoamento = 0
projecoes = []

with open('simulador/metricas.json', 'r') as json_file:
    dados = json.load(json_file)
    
    for metrica in dados:
        if 'taxa de escoamento' in metrica['Metrica'].lower():
            taxa_escoamento = metrica['Valor']

with open('simulador/projecao_trimestral.json', 'r') as json_file:
    dados = json.load(json_file)

    projecoes = dados
    
def gera_calendario_trimestre(ano, trimestre):
    mes_inicio = 3 * (trimestre - 1) + 1
    data_inicio = datetime(ano, mes_inicio, 1)

    if mes_inicio + 3 > 12:
        data_fim = datetime(ano + 1, 1, 1) - timedelta(days=1)
    else:
        data_fim = datetime(ano, mes_inicio + 3, 1) - timedelta(days=1)
    
    return pd.date_range(data_inicio, data_fim)

def distribuicao_producao_diaria(producao_leite_trimestral, ano, trimestre):
    datas = gera_calendario_trimestre(ano, trimestre)

    pesos = {data: random.uniform(0.8, 1.2) for data in datas}
            
    soma_pesos = sum(pesos.values())
    producao_diaria = []
    
    for data, peso in pesos.items():
        volume_dia = (peso / soma_pesos) * producao_leite_trimestral
        producao_diaria.append({
            "data": data.strftime("%d/%m/%Y"),
            "volume": volume_dia * taxa_escoamento
        })
        
    return producao_diaria

def calcular_producao_anual():
    producao = []
    for dado in projecoes:
        ano = dado['Ano']
        trimestre = dado['Trimestre']
        producao_leite_trimestral = dado['Produção_Estimada']
        
        producao_diaria_trimestral = distribuicao_producao_diaria(producao_leite_trimestral, ano, int(trimestre))
        producao.append(producao_diaria_trimestral)
    
    return producao

PRODUCAO_DIARIA_ANUAL = calcular_producao_anual()