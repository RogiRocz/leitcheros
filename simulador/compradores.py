from faker import Faker
import random
import string

fake = Faker('pt_BR')

string_alfabeto = string.ascii_uppercase
alfabeto = list(string_alfabeto)

def calcular_peso_mercado(regiao = '', tipo = ''):
    valor = 0
    if tipo == 'Grande':
        inicio, fim = 0.25, 0.45
        valor = random.uniform(inicio, fim)
        if regiao in ['Geraldo', 'Atacarejo']:
            valor += random.uniform(0.08, 0.10)

    elif tipo == 'Filial':
        inicio, fim = 0.03, 0.07
        valor = random.uniform(inicio, fim)
        if 'Centro' in regiao:
             valor += random.uniform(0.01, 0.02)

    elif tipo == 'Pequeno':
        inicio, fim = 0.005, 0.03
        valor = random.uniform(inicio, fim)
        if 'Centro' in regiao:
            valor += random.uniform(0.005, 0.015)

    return round(valor, 4)

def gerar_pequenos_comercios(quantidade=10):
    comercios = []
    for _ in range(quantidade):
        nome_comercio = alfabeto[random.randrange(0, len(alfabeto))]
        bairro = random.choice(BAIRROS_QUIXADA)
        comercios.append({
            "nome": f"Mercadinho {nome_comercio} - {bairro}",
            "tipo": "Pequeno Porte (Informal)",
            "peso_mercado": calcular_peso_mercado(bairro, tipo='Pequeno')
        })
    
    return comercios

PLAYERS_PRINCIPAIS = [
    {"nome": "Supermercado Pinheiro", "tipo": "Grande Porte", "peso_mercado": calcular_peso_mercado(tipo='Grande')},
    {"nome": "Atacarejo Quixadá", "tipo": "Grande Porte", "peso_mercado": calcular_peso_mercado('Atacarejo' ,tipo='Grande')},
    {"nome": "Supermercado São Geraldo (Matriz)", "tipo": "Grande Porte", "peso_mercado": calcular_peso_mercado('Geraldo', tipo='Grande')},
]

BAIRROS_QUIXADA = ["Planalto Universitário", "Campo Novo", "Centro", "Putiú", "Herval", "Irajá"]
BAIRROS_FILIAIS_SAO_GERALDO = ["Campo Novo", "Centro 1", "Centro 2", "Herval", "Irajá"]
FILIAIS_SAO_GERALDO = [
    {"nome": f"São Geraldo - Filial {bairro}", "tipo": "Filial", "peso_mercado": calcular_peso_mercado(bairro ,tipo='Filial')} 
    for bairro in BAIRROS_FILIAIS_SAO_GERALDO
]

pequenos_comercios_gerados = gerar_pequenos_comercios()

TODOS_COMPRADORES = PLAYERS_PRINCIPAIS + FILIAIS_SAO_GERALDO + pequenos_comercios_gerados
