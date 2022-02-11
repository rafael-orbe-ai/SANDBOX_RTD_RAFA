Gráfico histograma
*********

01.Para que serve um histograma
================

Usamos um histograma quando queremos entender a distribuição da **frequência em que algo ocorre dentro de um intervalo numérico**.

Exemplo: 

Quantos produtos custam entre:

•	0–100 reais

•	101–200 reais

•	201–300 reais

•	301–400 reais

•	401–500 reais

•	501–600 reais

•	601–700 reais

•	701–800 reais

•	801–900 reais

•	901–1.000 reais

.. image:: images/grafico/grafico_histograma.png
   :align: center
   :width: 550
   
02.Preparando os dados
========

02.a.Importando as bibliotecas necessárias
--------

.. code-block:: python
   :linenos:
   
   #Importando as bibliotecas necessárias
   import pandas as pd
   import matplotlib.pyplot as plt


02.b.Criando o DataFrame
--------- 

Para este grpafico usaremos uma base de dados ("olist_order_payments_dataset.xlsx") sobre pagamentos de pedidos da empresa de varejo online Olist.

.. code-block:: python
   :linenos:
   
   #Criando o DataFrame
   df = pd.read_excel("/content/oilist_order_payments_dataset.xlsx")
   
.. code-block:: python
   :linenos:
   
   #Visualizandoo DataFrame
   df.head()
      
**Este é o resultado:**


.. image:: images/grafico/head_oilist.png
   :align: center
   :width: 650

.. code-block:: python
   :linenos:
   
   #Verificando o formato do DataFrame
   df.shape
   
**Este é o resultado:**

.. code-block:: python
   
   >>> (102698, 5)

.. note::
  Por uma questão de didática fizemos pequenas alterações no dataset que retiramos do site da Kaggle.
  

 
03.Construindo um gráfico de histograma
========

.. image:: images/grafico/figura_axe.png
   :align: center
   :width: 550

.. code-block:: python
   :linenos:
   
   #Criar o objeto figure e axes
   fig, ax_01 = plt.subplots()

.. code-block:: python
   :linenos:
   
   #Escolher os dados e somá-los para plotar o gráfico
   df.payment_value.plot(kind="hist", ax=ax_01, bins = 20)

.. code-block:: python
   :linenos:
   
   #Customizando o Axes
   ax_01.set_title("Histograma preço dos produtos")
   ax_01.set_xlabel("Preço dos produtos.")
   ax_01.set_ylabel("Quantidade vendida.")


.. code-block:: python
   :linenos:
   
   #Exibindo o gráfico
   plt.show()

**Este é o resultado:**

.. image:: images/grafico/grafico_histograma.png
   :align: center
   :width: 550

.. note::
  
  1. Usar o método e os parâmetros ``figsize(altura,largura)`` se necessário.
  2. Usar parâmetro ``bins`` se necessário, que serve para definir o número de intervalos que o matplotlib considera para criar as barras no histograma..
