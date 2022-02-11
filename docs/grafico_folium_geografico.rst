Gráfico de informaçoes geográficas com Folium
************

``Folium`` é uma biblioteca para Python que nos permite criar mapas, nos permitindo criar gráficos incríveis que mostrem a disperção geográfica de algo.

01.Instalando o Folium
========

Para instalar o Folium usamos o comando ``!pip install``:

.. code-block:: python
   :linenos:
   
   !pip install folium

**Este é o resultado:**

.. image:: images/grafico/pip_install.png
   :align: center
   :width: 550
 
02.Importando o Folium
======

Para importar o Folium usamos o comando ``import``:

.. code-block:: python
   :linenos:
   
   import folium
 
03.Criando um mapa com Folium
=======

Para gerar um mapa usamos o método ``.Map()`` do Folium para criarmos um objeto (que é o próprio mapa).

.. code-block:: python
   :linenos:
   
   #Usando o método .Map() para criar um mapa e salvando na variável mapa
   mapa = folium.Map()
   
.. code-block:: python
   :linenos:  
   
   #Para mostrar o mapa basta chamá-lo:
   mapa
   
**Este é o resultado:**

.. image:: images/grafico/metodo_map.png
   :align: center
   :width: 550
 
04.Customizando um mapa
======

04.a.Iniciando um mapa com a localização exata
-----

Para saber uma latitude e longitude específica:

1.	Abra o site do Google Mapas
2.	Digite o endereço do lugar desejado.
3.	Encontre a latitude e longitude na URL do site do Google Mapas. Elas estão logo após do sinal “@”.

Exemplo da URL localizando o Parque Ibirapuera na cidade de São Paulo/SP:

Início da URL: https://www.google.com.br/maps/place/Parque+Ibirapuera/@-23.5918264,-46.6576057,15z

•	latitude: -23.5918264
•	longitude: -46.6576057

PARÂMETRO E MÉTODO NECESSÁRIO:
++++

Para inicializar o objeto mapa com alguma localização específica, usamos o parâmetro ``location`` dentro do método ``.Map()``:

.. code-block:: python
   :linenos:
   
   #Usando o parâmetro location com o método .Map() para criar um mapa e salvando na variável mapa
   mapa = folium.Map(location=[-23.5918264,-46.6576057])
   
.. code-block:: python
   :linenos:  
   
   #Para mostrar o mapa basta chamá-lo:
   mapa
   
**Este é o resultado:**

.. image:: images/grafico/mapa_loc_especifico.png
   :align: center
   :width: 550
 
04.b.Iniciando um mapa com a localização e o zoom específico.
-----

Para sabermos qual o zoom ideal para o mapa:

1.	Abra o site do Google Mapas
2.	Digite o endereço do lugar desejado.
3.	Na URL, encontre o valor do zoom indicado por “z” (fica logo após a latitude e longitude.

Exemplo da URL localizando o Parque Ibirapuera na cidade de São Paulo/SP.

Início da URL: https://www.google.com.br/maps/place/Parque+Ibirapuera/@-23.5918264,-46.6576057,15z

•	latitude: -23.5918264
•	longitude: -46.6576057
•	zoom: 15

PARÂMETRO E MÉTODO NECESSÁRIO:

Para isso usamos o parâmetro ``zoom_start`` no método ``.Map()``.

.. code-block:: python
   :linenos:
   
   #Usando o parâmetro location com o método .Map() para criar um mapa e salvando na variável mapa com o zoom 15
   mapa = folium.Map(location=[-23.5918264,-46.6576057], zoom_start=15)
   
.. code-block:: python
   :linenos:  
   
   #Para mostrar o mapa basta chamá-lo:
   mapa
   
**Este é o resultado:**

.. image:: images/grafico/mapa_zoom_especifico.png
   :align: center
   :width: 550
 
05.Escolhendo o estilo de mapa
===========

Alguns estilos de mapas:

1.	OpenStreetMap (default) 
    > Igual ao Google Mapas.
    
2.	Stamen Terrain
    > Relevo.

3.	Stamen Toner
    > Preto e branco.

4.	Stamen Watercolor
    > Aquarela

Parâmetro e método necessário:

Para escolher o estilo de gráfico do nosso mapa usamos o parâmetro ``tiles`` dentro do nosso método ``Map()``.

.. code-block:: python
   :linenos:
   
   #Usando o parâmetro location com o método .Map() para criar um mapa e salvando na variável mapa com o zoom 15 e com estilo 'Stamen Terrain'
   mapa = folium.Map(location=[-23.5918264,-46.6576057], zoom_start=15, tiles='Stamen Terrain')
   
.. code-block:: python
   :linenos:  
   
   #Para mostrar o mapa basta chamá-lo:
   mapa
   
**Este é o resultado:**

.. image:: images/grafico/mapa_estilo_especifico.png
   :align: center
   :width: 550

06.Adicionando marcadores no mapa
=====

``Marquers`` são marcadores, pontos que queremos destacar no mapa de alguma maneira.

Para isso, usamos o método ``.Marker()`` e os seus seguintes parâmetros:

•	``location`` ---> localização do marcador em latitude e longitude.
•	``popup`` ---> texto que aparece após o clique do mouse no marker.
•	``tooltip`` ---> texto que aparece quando passamos o mouse sobre o marker.
•	``icon`` ---> customização do marcador (trocaremos a cor do marcador)

Para adicionar todos estes marcadores no mapa, usamos o método ``.add_to()`` após o método ``Marker()``.

.. code-block:: python
   :linenos:
   
   #Criando o mapa
   mapa = folium.Map(location=[-23.5918264,-46.6576057], zoom_start=15)
   

.. code-block:: python
   :linenos:
   
   #Adicionando marcadores
   folium.Marker(location=[-23.5919878,-46.6591159],
              popup='Parque do Ibirapuera',
              tooltip="Clique aqui",
              icon=folium.Icon(color="green")
              ).add_to(mapa)
   
.. code-block:: python
   :linenos:  
   
   #Para mostrar o mapa basta chamá-lo:
   mapa
   
**Este é o resultado:**

.. image:: images/grafico/mapa_marcador_especifico.png
   :align: center
   :width: 550
 
07.Adicionando áreas circulares
======

Para adicionar as áreas circulares usamos o método ``CircleMarker`` e os seus seguintes parâmetros:

•	``location`` ---> localização do marcador em latitude e longitude.
•	``radius`` ---> raio do círculo.
•	``color`` ---> cor da área dentro do círculo.
•	``fill`` ---> preenchimento ou não da área circular.
•	``fill_color`` ---> cor do preenchimento da área circular.


.. code-block:: python
   :linenos:
   
   #Criando o mapa
   mapa = folium.Map(location=[-23.5918264,-46.6576057], zoom_start=15)
   

.. code-block:: python
   :linenos:
   
   #Criando a area circular
   folium.CircleMarker(location=[-23.5918264,-46.6576057],
                       radius=150,
                       color='red'
                       fill=True,
                       fill_color='red').add_to(mapa)
   
.. code-block:: python
   :linenos:  
   
   #Para mostrar o mapa basta chamá-lo:
   mapa
   
**Este é o resultado:**
 
.. image:: images/grafico/mapa_area_circular_especifico.png
   :align: center
   :width: 550
 
08.Usando o Folium com DataFrame
============

Como vamos precisar criar um Data Frame precisaremos da biblioteca Pandas. Por isso iremos importá-la para o Jupyter Notebbok.

.. code-block:: python
   :linenos:
   
   import pandas as pd
   
Também importaremos para o Jupyter Notebook um pacote do Folium chamado ``plugins`` (funcionalidade especial) que nos permitirá fazer alguns efeitos como mapa de calor. 
Para isso, usamos o comando:

.. code-block:: python
   :linenos:
   
   from folium import plugins

 
08.a.Usando um dataset para criar um DataFrame
-----------

O dataset utilizado nesta aula é sobre o acompanhamentos de queimadas registrados por satélite da NASA nos últimos 7 dias.

.. code-block:: python
   :linenos:
   
   #Criando o DataFrame
   df = pd.read_csv("/content/MODIS_C6_South_America_7d.csv")

.. code-block:: python
   :linenos:
   
   #Visualizando as 5 primeiras entradas do DataFrame
   df.head()
   
**Este é o resultado:**

.. image:: images/grafico/head_nasa.png
   :align: center
   :width: 550

.. code-block:: python
   :linenos:
   
   #Visualizando o formato do DataFrame
   df.shape
   
**Este é o resultado:**

.. code-block:: python
   
   >>> (5909, 13)
 
08.b.Extraindo os valores do DataFrame
---------

Vamos extrair os valores do Data Frame e salvá-los em variáveis para que possamos usá-las para construir o mapa.

.. code-block:: python
   :linenos:
   
   #Extraindo valores e salvando em variáveis
   latitude = df.latitude.values
   longitude = df.longitude.values

.. code-block:: python
   :linenos:
   
   #Criando um mapa
   mapa_queimadas_brasil = folium.Map(location=[-14.0565789,-57.6047293],zoom_start=4.5)

.. code-block:: python
   :linenos:
   
   #Adicionando marcadores no mapa
   for lat, lon in zip(latitude,longitude):
       folium.Marker(location=[lat,lon]).add_to(mapa_queimadas_brasil)

.. code-block:: python
   :linenos:
   
   #Exibindo o mapa
   mapa_queimadas_brasil
   
 **Este é o resultado:**

.. image:: images/grafico/mapa_nasa_marcador.png
   :align: center
   :width: 550
 
09.Criando um mapa de calor (``heatmap``).
========

Para criarmos um mapa de calor usamos um plugin (funcionalidade especial) chamado ``.HeatMap`` dentro do método ``.add_child()`` desta forma:

.. code-block:: python
   :linenos:
   
   #Extrair coordenadas geográficas do DataFrame
   latitude = df.latitude.values
   longitude = df.longitude.values

.. code-block:: python
   :linenos:
   
   #Criar uma lista com latitude e longitude usando o for
   coordenadas=[]

   for lat,lon in zip(latitude,longitude):
       coordenadas.append([lat,lon])
 
.. code-block:: python
   :linenos:
   
   #Criar o mapa    
   mapa_queimadas_LATAM = folium.Map(location[-14.0565789,-57.6047293],
                                     zoom_start=4.5,
                                     tiles='Stamen Terrain')

.. code-block:: python
   :linenos:
   
   #Adicionando coordenadas para criar um mapa de calor e mostrando o mapa
   mapa_queimadas_LATAM.add_child(plugins.HeatMap(coordenadas))

 
**Este é o resultado:**

.. image:: images/grafico/mapa_nasa_calor.png
   :align: center
   :width: 550
