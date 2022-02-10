Estrutura de dados
**************************

01.Introdução a estrutura de dados em Python.
==============================================

Em uma variável é possível armazenar apenas um valor. 

Para armazenar mais do que um valor usamos as **estrutura de dados**.
As mais usadas são:

- Listas

- Tuplas 

- Dicionários

02.Listas
=========

Lista é uma estrutura de dados para armazenar múltiplos valores em uma única variável.

02.a.Criando uma lista
-------------

Listas são criadas usando colchetes ``[]``

Veja o exemplo de como criar uma lista:

.. code-block:: python
   :linenos:

   #Criando uma lista
   nome_da_lista = ["maça", 2,"verde", 4.5]
   
   
02.b.Contando quantos itens tem em uma lista
-------------

Para saber quantos item há na lista, usamos o comando ``len()``.

Veja o exemplo de como criar usar o comando ``len()`` em uma lista:

.. code-block:: python
   :linenos:

   #Contando quantos itens há em uma lista
   print(len(nome_da_lista))

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 4
   
02.c.Estrutura de uma lista
-------------   

Os itens de uma lista são ordenados por índex.

Pense na lista ``nome_da_lista = ["maçã", 2,"verde", 4.5]``

Ela será ordenada da seguinte maneira:

+---------------+--------+---+---------+-----+
|     índex     |    0   | 1 | 2       | 3   |
+---------------+--------+---+---------+-----+
| nome_da_lista | 'maçã' | 2 | 'verde' | 4.5 |
+---------------+--------+---+---------+-----+


.. warning::

  Lembre-se que em programação sempre começamos a contar a partir do 0 (zero).
  

02.c.i.Acessando os itens de uma lista pelo índex
+++++++++++

Pense na lista ``nome_da_lista = ["maçã", 2,"verde", 4.5]``

Para acessar um item da lista através do índex fazemos desta forma:

.. code-block:: python
   :linenos:

   #Acessando um item da lista através do índex
   nome_da_lista[2]

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 'verde'
   
02.c.ii.Acessando uma fatia (slice) de uma lista pelo índex
+++++++++++ 

Pense na lista ``nome_da_lista = ["maçã", 2,"verde", 4.5]``

Para acessar uma fatia fazemos da seguinte forma:

.. code-block:: python
   :linenos:

   #Acessando uma fatia da lista através do índex
   nome_da_lista[1:3]

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> [2, 'verde']
   
.. warning::

  Repare que:
  
  - O primeiro item da fatia [1] **é incluso**
  
  - O último item da fatia [3] **não é incluso**
  
  
  
02.d.Lista são mutáveis
-------------   

Isso significa que podemos mudar/alterar os itens de uma lista.


02.d.i.Alterando um item de uma lista
++++++++++++++

Pense na lista ``nome_da_lista = ["maçã", 2,"verde", 4.5]``

Para alterar o item ``2`` por ``"limão"`` fazemos da seguinte forma:

.. code-block:: python
   :linenos:

   #Alterando um item da lista através do índex
   nome_da_lista[1] = "limão"
   
.. code-block:: python
   :linenos:

   #Visualizando a lista depois da alteração
   print(nome_da_lista)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> ['maçã', 'limão', 'verde', 4.5]
   
   
02.d.ii.Removendo um item de uma lista
++++++++++++++

Para remover um item de uma lista usamos o comando ``remove()`` indicando o item a ser removido. 

Pense na lista ``nome_da_lista = ["maçã", "limão", "verde", 4.5]``

Para remover o item ``maçã`` fazemos da seguinte forma:


.. code-block:: python
   :linenos:

   #Removendo um item da lista
   nome_da_lista.remove("maçã")
   
.. code-block:: python
   :linenos:

   #Visualizando a lista depois da remoção
   print(nome_da_lista)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> ['limão', 'verde', 4.5]
   
 
02.d.iii.Adicionando um item em uma lista
++++++++++++++

Pense na lista ``nome_da_lista = ["maçã", "limão", "verde", 4.5]``

Podemos acrescentar um item em uma lista de duas maneiras: 

- **Ao final da lista.** 

Para adicionar um item ao final da lista usamos o comando ``append()``, desta forma:

.. code-block:: python
   :linenos:

   #Adicionando um item ao final da lista
   nome_da_lista.append("laranja")
   
.. code-block:: python
   :linenos:

   #Visualizando a lista depois da remoção
   print(nome_da_lista)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> ['maçã', 'limão', 'verde', 4.5, 'laranja']


- **Em um índex específico.**


Para adicionar um item em um índex específico da lista usamos o comando ``insert()``, desta forma:


.. code-block:: python
   :linenos:

   #Adicionando um item em um índex específico
   nome_da_lista.insert(2, "laranja")
   
.. code-block:: python
   :linenos:

   #Visualizando a lista depois da remoção
   print(nome_da_lista)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> ['maçã', 'limão', 'laranja', 'verde', 4.5]
   

02.e.Resumo de comandos para usar com listas
-------------   

+---------------------------------------------+-------------------------------------------------------+
|                   COMANDO                   |                       DESCRIÇÃO                       |
+---------------------------------------------+-------------------------------------------------------+
| nome_lista = [valor_01, valor_02, valor_03] |          criando uma lista com colchetes [ ]          |
+---------------------------------------------+-------------------------------------------------------+
|               len(nome_lista)               |         descobrindo quantos itens há na lista.        |
+---------------------------------------------+-------------------------------------------------------+
|                nome_lista[2]                | acessando um item específico da lista pelo seu índex. |
+---------------------------------------------+-------------------------------------------------------+
|               nome_lista[1:3]               |       acessando um intervalo de itens na lista.       |
+---------------------------------------------+-------------------------------------------------------+
|         nome_lista[1] = "novo valor"        | alterando um item específico da lista pelo seu índex. |
+---------------------------------------------+-------------------------------------------------------+
|                remove(valor)                |          remove um item com valor específico.         |
+---------------------------------------------+-------------------------------------------------------+
|                append(valor)                |          adiciona um item ao final da lista.          |
+---------------------------------------------+-------------------------------------------------------+
|             insert(index,valor)             |        adiciona um item em um índex específico.       |
+---------------------------------------------+-------------------------------------------------------+




03. Tuplas
===========

Tupla é uma estrutura de dados para armazenar vários itens.

Os itens de uma tupla são ordenados por índex.
Permitem itens duplicados e são imutáveis, ou seja, depois que a tupla foi criada não conseguimos alterar, adicionar e remover os seus itens.


03.a.Criando uma Tupla
--------------------

Para criar um tupla usamos parênteses ``()``, onde inserimos os itens.

Veja o exemplo de como criar uma tupla:

.. code-block:: python
   :linenos:

   #Criando uma tupla
   nome_da_tupla = ("maça", 2,"verde", 4.5)
   
   
03.b.Contando quantos itens tem em uma tupla
-------------

Para saber quantos item há na tupla, usamos o comando ``len()``.

Veja o exemplo de como criar usar o comando ``len()`` em uma tupla:

.. code-block:: python
   :linenos:

   #Contando quantos itens há em uma tupla
   print(len(nome_da_tupla))

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 4 
   
03.c.Estrutura de uma tupla
-------------   

Os itens de uma lista são ordenados por índex.

Pense na tupla ``nome_da_tupla = ("maçã", 2,"verde", 4.5)``

Ela será ordenada da seguinte maneira:

+---------------+--------+---+---------+-----+
|     índex     |    0   | 1 | 2       | 3   |
+---------------+--------+---+---------+-----+
| nome_da_tupla | 'maçã' | 2 | 'verde' | 4.5 |
+---------------+--------+---+---------+-----+


.. warning::

  Lembre-se que em programação sempre começamos a contar a partir do 0 (zero).
  

03.c.i.Acessando os itens de uma tupla pelo índex
+++++++++++

Pense na tupla ``nome_da_tupla = ("maçã", 2,"verde", 4.5)``

Para acessar um item da tupla através do índex fazemos desta forma:

.. code-block:: python
   :linenos:

   #Acessando um item da tupla através do índex
   nome_da_tupla[2]

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 'verde'
   
03.c.ii.Acessando uma fatia (slice) de uma tupla pelo índex
+++++++++++ 

Pense na tupla ``nome_da_tupla = ("maçã", 2,"verde", 4.5)``

Para acessar uma fatia fazemos da seguinte forma:

.. code-block:: python
   :linenos:

   #Acessando uma fatia da tupla através do índex
   nome_da_tupla[1:3]

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> [2, 'verde']
   
.. warning::

  Repare que:
  
  - O primeiro item da fatia [1] **é incluso**
  
  - O último item da fatia [3] **não é incluso**
  

  
04.Dicionários
===========

Dicionário é uma estrutura de dados para armazenar itens no formato ``{'chave' : 'valor'}``

Os itens do dicionários são: ordenados (sem índex), mutáveis e não permitem itens duplicados.

**Estrutura de um dicionário:**
``novo_dic = {'chave_01' : 'valor_01', 'chave_02' : 'valor_02', 'chave_03' : 'valor_03'}``

04.a.Criando um dicionário
----------------------

Para criar um dicionário usamos chaves ``{ }`` e itens no formato ``{'chave': 'valor'}``.

Veja o exemplo de como criar um dicionário:

.. code-block:: python
   :linenos:

   #Criando um dicionário
   novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 1963 }
   
   
04.b.Contando quantos itens tem em um dicionário
-------------

Para saber quantos item há no dicionário, usamos o comando ``len()``.

Veja o exemplo de como criar usar o comando ``len()`` em um dicionário:

.. code-block:: python
   :linenos:

   #Contando quantos itens há em um dicionário
   print(len(novo_dic))

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 3
   
.. warning::
  
  Cada chave com seu respectivo valor (exemplo: {'artista': 'Jorge Ben Jor'}) conta como um no comando ``len()``


04.c.Acessando um item em um dicionário
-------------

Os itens de um dicionário são ordenados pela suas chaves.
Para acessar um item de um dicionário, basta se referir ao nome da chave deste item dentro de colchetes ``[ ]``.

Pense no dicionário ``novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 1963 }``

Veja o exemplo de como acessar um item em um dicionário:


.. code-block:: python
   :linenos:

   #Acessando o item em um dicionário
   novo_dic["álbum"]

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 'Samba Esquema Novo'
   

04.d.Dicionários são mutáveis
------------- 

Isso significa que podemos mudar/alterar os itens de uma lista

04.c.i.Alterar um item de um dicionário.
++++++++++++++++++++++++++++

Podemos trocar o valor de um item se referindo ao nome de sua chave.

Pense no dicionário ``novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 1963 }``

Veja o exemplo de como alterar um item em um dicionário:

.. code-block:: python
   :linenos:

   #Alterando o valor da chave ano
   novo_dic["ano"] = 2021
   
.. code-block:: python
   :linenos:

   #Visualizando a alteração
   print(novo_dic)  

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 2021 }
   
04.c.ii.Adicionar um item de um dicionário.
++++++++++++++++++++++++++++

Para adicionar um item em um dicionário, informamos a chave e o valor.

Pense no dicionário ``novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 1963 }``

Veja o exemplo de como adicionar um item em um dicionário:

.. code-block:: python
   :linenos:

   #Adicionando um item no dicionário
   novo_dic['música'] = 'Mas, que nada!'
   
.. code-block:: python
   :linenos:

   #Visualizando o dicionário com item adicionado
   print(novo_dic)  

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 1963, 'música': 'Mas, que nada!'}
   
04.c.iii.Remover um item de um dicionário.
++++++++++++++++++++++++++++ 

Para remover um item de um dicionário nós usamos o comando ``pop( )`` com a chave do item que queremos remover.

Pense no dicionário ``novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo', 'ano': 1963 }``

Veja o exemplo de como remover um item em um dicionário:

.. code-block:: python
   :linenos:

   #Adicionando um item no dicionário
   novo_dic.pop("ano)
   
.. code-block:: python
   :linenos:

   #Visualizando o dicionário com item removido
   print(novo_dic)  

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> novo_dic = {'artista': 'Jorge Ben Jor', 'álbum': 'Samba Esquema Novo'}
   
   
04.e.Resumo de comandos para usar com dicionários
-----------------


+--------------------------------+--------------------------------------------------------------+
|             COMANDO            |                           DESCRIÇÃO                          |
+--------------------------------+--------------------------------------------------------------+
| novo_dic = {'chave': valor}    | criando um dicionário com chaves { }                         |
+--------------------------------+--------------------------------------------------------------+
| len(novo_dic)                  | descobrindo quantos itens há no dicionário.                  |
+--------------------------------+--------------------------------------------------------------+
| nov_dic['chave']               | acessando um item específico do dicionário por sua chave.    |
+--------------------------------+--------------------------------------------------------------+
| novo_dic['chave'] = novo valor | alterando um item específico do dicionário por sua chave.    |
+--------------------------------+--------------------------------------------------------------+
| novo_dic.pop('chave')          | remove um item informando a sua chave.                       |
+--------------------------------+--------------------------------------------------------------+
| novo_dic['chave'] = 'valor'    | adiciona um item ao dicionário informando sua chave e valor. |
+--------------------------------+--------------------------------------------------------------+
| append(valor)                  | adiciona um item ao final da lista.                          |
+--------------------------------+--------------------------------------------------------------+
| insert(index,valor)            | adiciona um item em um índex específico.                     |
+--------------------------------+--------------------------------------------------------------+
