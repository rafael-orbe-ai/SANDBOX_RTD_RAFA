COMPREENSÃO DOS DADOS
*******

01.O QUE É PANDAS.
=========

01.a.DESCRIÇÃO SOBRE PANDAS.
------

•	Pandas é uma biblioteca em Python para trabalhar com dados, como por exemplo nas seguintes etapas do roteiro de um projeto de dados:

.. figure::  projeto_de_dados.png
   :align:   center
 
COMPREENDER OS DADOS
+++++++++

•	Explorar
•	Analisar

PREPARAR OS DADOS PARA ALGORITMOS DE APRENDIZAGEM
+++++++++

•	Limpar
•	Adequar


01.b.IMPORTANDO O PANDAS.
-------

Para importarmos o Pandas para o Jupyter Notebook usamos o comando import. Como iremos escrever a palavra Pandas muitas vezes ao longo do código, é muito comum apelidarmos a biblioteca para um nome menor pd com o uso do comando as.
Como importar o Pandas para o Jupyter Notebook e apelidar de pd.

.. code-block:: python
   :linenos:
   
   import pandas as pd
   

02.CRIANDO UM DATAFRAME A PARTIR DE UM DATASET.
------

Para criar um (objeto) DataFrame a partir de um dataset (conjunto de dados) precisamos seguir os seguintes passos:

PRIMEIRO: COLOCAR O DATASET NO PROJETO.
++++++++++++

•	Ir em arquivos na aba lateral do Google Colaboratory.

.. figure::  arquivos_colaboratory.png
   :align:   center

 
•	Arrastar o dataset para a parte de arquivos.

.. figure::  arrastar_planilha.png
   :align:   center
 
•	Clicar com o botão direito em cima da planilha e depois em “copiar caminho” ou “copy path”.

.. figure::  copiar_caminho.png
   :align:   center
 
•	Substituir o “endereço do arquivo” pelo caminho copiado.

.. figure::  copiar_caminho_resultado.png
   :align:   center
 
SEGUNDO: USAR OS MÉTODOS DO PANDAS PARA LER O ARQUIVO.
++++++++++++

•	``read_excel(“endereço do arquivo”)`` -> para ler arquivos do tipo planilha Excel.

•	``read_csv(“endereço do arquivo”)`` -> para ler arquivos do tipo csv.

•	Criar o objeto a partir do operador de atribuição -> ``=``

Exemplo:

.. code-block:: python
   :linenos:
   
   df = pd.read_excel(“endereço do arquivo”)
   
.. code-block:: python
   :linenos:

   print(df)
   
**Este é o resultado:**

.. figure::  print_df.png
   :align:   center
 
03.COMANDOS BÁSICOS COM O DATAFRAME.
========

03.a.VISUALIZANDO O DATAFRAME.
-----------

A forma mais comum de visualizar o DataFrame é usar o comando head() que nos mostra as primeiras linhas do DataFrame.
Por padrão, o método ``head()`` mostra as primeiras cinco linhas, mas caso desejamos mais, basta informar a quantidade dentro dos parênteses do método.
Exemplo:

.. code-block:: python
   :linenos:

   df.head()
   
**Este é o resultado:**

.. figure::  df_head.png
   :align:   center
 
 
03.b.FORMATO DO DATAFRAME.
--------

Para entendermos o formato do DataFrame, ou seja, a quantidade de linhas e colunas, usamos a propriedade ``shape``.
Exemplo:

.. code-block:: python
   :linenos:

   df.shape
   
**Este é o resultado:**


.. code-block:: python
   
   >>> (23759, 9)

03.c.TIPOS DE DADOS.
-----------
A nomenclatura do tipo de dado do Pandas é diferente do tipo de dado do Python:

.. figure::  nomenclatura_dados.png
   :align:   center
   
Para visualizarmos quais são os tipos de dados por coluna usamos a propriedade ``dtypes`` desta forma:

.. code-block:: python
   :linenos:

   df.dtypes
   
**Este é o resultado:**

.. figure::  df_dtypes.png
   :align:   center
   
   
04.ATRIBUTOS
=======

Como vimos anteriormente, o DataFrame é organizado em linhas e colunas; as linhas para armazenar as entradas de dados e as colunas representam os atributos que descrevem as características dos dados de cada linha.

04.a.TIPOS DE ATRIBUTOS.
-------

Os atributos podem ser divididos da seguinte forma:

.. figure::  tipos_atributos.png
   :align:   center
 
04.a.i.NUMÉRICO
++++++

•	Pode-se executar operações matemáticas, como subtração, soma, e aplicar conceitos estatísticos como média, moda, mediana.

**DISCRETO:**

•	``dtype: int64``
•	Número inteiro.
•	Geralmente resultado de uma contagem.
•	Exemplo: quantidade de pessoas, número de produtos em um estoque, etc.
•	Exemplo: quantidade de pessoas em uma sala: 18


**CONTÍNUO:**

•	``dtype: float64``
•	Número com casa decimal.
•	Geralmente é uma medida realizada com algum instrumento.
•	Exemplo: altura, peso, etc.
•	Exemplo: peso de um animal: 12,5 Kg.


04.a.ii. CATEGÓRICO
+++++++

•	``dtype: string``
•	Pode-se apenas trabalhar com a medida estatística moda.
•	Representa uma classificação de categorias.

**ORDINAIS:**
•	Há ordenação.
•	Ex: escolaridade (primeiro, segundo, terceiro grau), estágio da doença (inicial, intermediária, avançada), etc.

**NOMINAIS:**
•	Não há ordenação.
•	Ex: sexo, cor do olho, aprovado/reprovado, etc.


05. PRODUZINDO TABULAÇÕES.
=====

Tabular dados é uma forma de organizarmos os dados em linhas e colunas. Para isso costuma-se utilizar dois métodos para organizar os dados: ``unique() e value_counts()``.

05.a.MÉTODO ``unique( )``
-----

Mostra o domínio de uma coluna do DataFrame, ou seja, todas as categorias distintas que ele assume.
Exemplo:

•	Abaixo usamos o método ``df.SEXO.unique()`` para ver quais categorias diferentes ele assume:

.. code-block:: python
   :linenos:

   df.SEXO.unique()
   
**Este é o resultado:**


.. code-block:: python
   
   >>> array([1, 0])
 
 
05.b.MÉTODO ``value_counts()``
------

Gera uma tabela de frequências simples para um atributo (coluna) , ou seja, conta a quantidade de vezes que um valor aparece em um atributo (coluna).
Exemplo:

•	Abaixo usamos o método ``df.SEXO.value_counts()`` para ver quantas vezes ele assumiu as categorias 0 ou 1:

.. code-block:: python
   :linenos:

   df.SEXO.value_counts()
   
**Este é o resultado:**

.. code-block:: python
   
   >>> 1      17385
   >>> 0       6374


06. AGREGAÇÕES.
======

Agregação é uma operação que agrega (junta) um grupo de dados para realizar contas com estatística para um grupo de linhas e colunas.
Por exemplo, suponha que você tenha o seguinte DataFrame:

.. figure::  df_vendas_head.png
   :align:   center
 
Para você saber qual o valor total foi vendido por bairro, você precisa fazer uma agregação, para isso usamos o método ``groupby( )``, dessa forma:

.. code-block:: python
   :linenos:

   grupo_valor_bairro = df_vendas['VALOR'].groupby(df_vendas['BAIRRO'])
   
.. code-block:: python
   :linenos:

   print(grupo_valor_bairro.sum())
   

**Este é o resultado:**

.. figure::  groupby.png
   :align:   center
 
Dessa forma os valores:

1.Na **coluna VALOR são agrupados** por valores da **coluna BAIRRO** 

2.Com o método ``sum()`` exibimos qual a somatória desses valores agregados.


07.IDENTIFICANDO OS DADOS AUSENTES.
====

É muito importante entender quantos dados ausentes há em cada coluna.

Para identificar quantos dados ausentes há em cada coluna usamos os métodos:

•	``isnull()`` para identificar dados ausentes.

•	``sum( )`` para somar todos os dados ausentes.

Vejo o exemplo de como usar os comandos ``df.isnull( ).sum( )``:

.. code-block:: python
   :linenos:

   df.isnull().sum()

**Este é o resultado:**

.. figure::  isnull_sum.png
   :align:   center 

 
 
