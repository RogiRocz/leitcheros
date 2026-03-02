from producao_diaria import PRODUCAO_DIARIA_ANUAL
from compradores import TODOS_COMPRADORES
from datetime import datetime, timedelta
import random
import json

VARIABILIDADE_PORTE = {
    "Grande Porte": 0.05,
    "Filial": 0.10,
    "Pequeno Porte (Informal)": 0.20
}

TAXA_VENDA = 0.9

def calcular_distribuicao_individual():
    producao_individual = []
    for mes in PRODUCAO_DIARIA_ANUAL:
        for dia in mes:
            data = dia.get('data')
            volume_diario_total = dia.get('volume')
            dict_comercio = {}
            list_comercio = []

            dict_comercio.setdefault('data', data)


            for comercio in TODOS_COMPRADORES:
                list_comercio.append({
                    'nome': comercio['nome'],
                    'volume': volume_diario_total * comercio['peso_mercado']
                })

            dict_comercio.setdefault('comercios', list_comercio)
            producao_individual.append(dict_comercio)
    return producao_individual


def calcular_vendas_com_validade(distribuicao_producao):
    historico_vendas = []
    
    for dia_producao in distribuicao_producao:
        data_atual_str = dia_producao['data']
        data_atual = datetime.strptime(data_atual_str, '%d/%m/%Y')
        validade = (data_atual + timedelta(days=3)).strftime('%d/%m/%Y')
        
        vendas_do_dia = {
            'data': data_atual_str,
            'registros_comercio': []
        }

        for comercio in dia_producao['comercios']:
            tipo = comercio.get('tipo', 'Pequeno Porte (Informal)')
            vol_recebido = comercio['volume']
            
            dispersao = VARIABILIDADE_PORTE.get(tipo, 0.10)
            fator_ruido = random.uniform(1 - dispersao, 1 + dispersao)
            
            vol_vendido = min(vol_recebido, (vol_recebido * TAXA_VENDA) * fator_ruido)
            vol_perdido = max(0, vol_recebido - vol_vendido)

            vendas_do_dia['registros_comercio'].append({
                'nome': comercio['nome'],
                'volume_recebido': round(vol_recebido, 2),
                'volume_vendido': round(vol_vendido, 2),
                'volume_sobra_dia': round(vol_perdido, 2),
                'data_validade_lote': validade,
                'performance_venda': round((vol_vendido / vol_recebido) * 100, 2) if vol_recebido > 0 else 0
            })

        historico_vendas.append(vendas_do_dia)
    
    return historico_vendas


DISTRUICAO_PRODUCAO_COMERCIOS = calcular_distribuicao_individual()
VENDAS_DETALHADAS = calcular_vendas_com_validade(DISTRUICAO_PRODUCAO_COMERCIOS)

with open ('simulador/vendas_detalhadas.json', 'w') as json_file:
    json.dump(VENDAS_DETALHADAS, json_file, indent=4)
