Gráfico de linhas
********

 
01.Para que serve um gráfico de linhas
=====

•	Usamos um gráfico de linha **quando os dados possuem uma continuidade**. 
Geralmente tempo, que fica no eixo X (eixo horizontal).

.. image:: images/grafico/grafico_linha.png
   :align: center
   :width: 550
 
02.Preparando os dados
=======

02.a.Importando as bibliotecas necessárias
--------

.. code-block:: python
   :linenos:
   
   #Importando as bibliotecas necessárias
   import pandas as pd
   import matplotlib.pyplot as plt


02.b.Criando o DataFrame
-------

Criaremos o objeto DataFrame a partir de um dataset de os valores das ações na bolsa de valores e que pode ser encontrado no site do Yahoo! Finanças.

.. code-block:: python
   :linenos:
   
   #Criando o DataFrame
   df_vale = pd.read_csv("/content/VALE.csv")
   
.. code-block:: python
   :linenos:
   
   #Visualizandoo DataFrame
   df_vale.head()
   
   
**Este é o resultado:**
  
.. image:: images/grafico/head_vale.png
   :align: center
   :width: 550
 
2.c.Preparando o DataFrame para o gráfico de linhas
-------

.. image:: images/grafico/tipos_dados.png
   :align: center
   :width: 550
   
Entendendo que tipo de dado é a variável que indica tempo (neste caso a variável “Date”). Para isso usamos o comando ``dtypes`` desta forma:

.. code-block:: python
   :linenos:
   
   #Usando comando dtypes
   df_vale.dtypes
   
   
**Este é o resultado:**


.. image:: images/grafico/df_vale_dtypes.png
   :align: center
   :width: 550
 
02.c.i.Alterando o tipo de dado da variável de tempo para datetime
--------

É muito comum os valores da variável de tempo ('Date' no nosso caso) estar formatada como texto (``object``) e por isso temos que transformá-la em um tipo de dado de tempo (``datetime64``). 

Para isso usamos o comando ``.to_datetime()`` desta forma:

•	df.Nome_Variavel = pd.to_datetime(df.Nome_Variavel)

.. code-block:: python
   :linenos:
   
   #Tranformando a columa Date em um tipo de dado datetime64
   df_vale.Date = pd.to_datetime(df_vale.Date)


.. code-block:: python
   :linenos:
   
   #Usando comando dtypes para verificar a alteração
   df_vale.dtypes
    
**Este é o resultado:**

.. image:: images/grafico/df_vale_dtypes_datetime.png
   :align: center
   :width: 550
 
02.c.ii.Tornando a variável de tempo o índice do DataFrame
------

Antes vamos visualizar as cinco primeiras entradas do Data Frame com o método ``.head( )``:

.. code-block:: python
   :linenos:
   
   #Usando comando dtypes para verificar a alteração
   df_vale.head()
    
**Este é o resultado:**

.. image:: images/grafico/head_vale.png
   :align: center
   :width: 550
 
Transformar a variável de tempo no índice do Data Frame ajuda o Matplotlib a criar os gráficos de linha, já que os dados que estão no índex do DataFrame são os dados usados no eixo x (eixo horizontal) do gráfico. 

Para isso usamos o comando ``.set_index()`` desta forma:

.. code-block:: python
   :linenos:
   
   #Usando comando .set_index() para tranformar a coluna 'Date' no índex do DataFrame
   df_vale.set_index("Date", inplace=True)

.. code-block:: python
   :linenos:
   
   #Usando comando dtypes para verificar a alteração
   df_vale.head()
    
**Este é o resultado:**

.. image:: images/grafico/head_vale_date_index.png
   :align: center
   :width: 550
   
03.Construindo um gráfico de linhas
============
 
.. image:: images/grafico/figura_axe.png
   :align: center
   :width: 550
    
.. code-block:: python
   :linenos:
   
   #Criar objeto figure e axe
   fig, ax_vale = plt.subplots()


.. code-block:: python
   :linenos:

   #Escolher os dados e plotar o gráfico
   df.Close.plot(kind="line", ax=ax_vale)

.. code-block:: python
   :linenos:

   #Customizar o Axe
   ax_vale.set_title("Ações da Vale")
   ax_vale.set_xlabel("Preço")
   ax_vale.set_ylabel("Tempo")

.. code-block:: python
   :linenos:

   #Mostrar o gráfico
   plt.show()

**Este é o resultado:**

.. image:: images/grafico/resultado_linha.png
   :align: center
   :width: 550
