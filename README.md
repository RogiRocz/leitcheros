#Projeto para análise de dados e criação de dados mockados do comércio de leite em Quixadá
# Leitcheros: Ecossistema de Laticínios em Quixadá 
## Resumo do projeto

> Este projeto nasceu da observação de uma lacuna no mercado varejista de Quixadá, Ceará: a escassez de leite fresco (líquido/in natura) nos grandes supermercados, que são dominados quase exclusivamente pelo leite de caixa (UHT). O Leitcheros é uma iniciativa que une Ciência de Dados e Desenvolvimento de Software para emular a dinâmica de compra e venda entre produtores locais e mercados, servindo como um estudo de viabilidade e um simulador de economia regional.

## Motivação e Intenção

A intenção principal é criar um sistema que emule o fluxo diário de leite não-industrializado, permitindo que produtores (formais e informais) e estabelecimentos comerciais interajam em um mercado digital.  O projeto visa: 

**1. Identificar Oportunidades**: Provar, através de dados, a viabilidade do comércio de leite fresco na região. \
**2. Simular Operações**: Emular a compra e venda diária para gerar dados de "mercado mockado" (fictícios). \
**3. Visualizar Resultados**: Transformar essas interações em um *Dashboard* de *Business Intelligence* (BI) para análise de tendências e faturamento. 

## A Jornada dos Dados: Da Curiosidade à Projeção

Antes de escrever a primeira linha de código do sistema, mergulhei nos dados históricos para garantir que o simulador fosse realista.

**Fase 1: Exploração e Erro (Censo vs. PPM):** Iniciei testando projeções baseadas no Censo Agropecuário 2017 e na PPM (Pesquisa da Pecuária Municipal).  No entanto, percebi que projetar a partir de 2017 trazia distorções, pois o mercado de leite no Ceará passou por mudanças significativas nos últimos anos.

**Fase 2: A Busca pelo "Melhor Ano":** Para refinar o modelo, desenvolvi um algoritmo para encontrar o Ano Base Ideal. Através do cálculo do CAGR (*Compound Annual Growth Rate* ou  Taxa de Crescimento Anual Composta, em português), identifiquei que o ano de 2021 era o ponto de partida mais fiel para prever o comportamento de 2025 e 2026.

Validação: O modelo foi testado contra dados reais de 2024, apresentando um erro (MAPE) extremamente baixo, validando a assertividade da projeção.

**Fase 3: Refinamento Sazonal:** Não bastava saber quanto Quixadá produz por ano; era preciso entender quando. Utilizei os dados da Tabela 1086 (Leite Adquirido) para aplicar índices de sazonalidade trimestral.  Isso permitiu que o sistema emulasse picos de preço na entressafra e picos de produção durante o período de chuvas no Sertão Central.

## Próximos Passos

Atualmente, o projeto concluiu a fase de Data Intelligence. Os próximos marcos são:

**1. Backend Development:** Construir a lógica de negócios para as transações diárias entre produtores e mercados.

**2. API Integration:** Disponibilizar os dados projetados e emulados para o frontend.

**3. BI Dashboard:** Criação da camada de visualização para análise de KPIs (Key Performance Indicators) de faturamento e volume.