
DADOS
*************

01. Tipos de dados
==================

Existem alguns tipos de dados na linguagem de programação, por enquanto vamos utilizar três tipos de dados mais comuns:

- Texto são chamados de ``string — str``

- Números inteiros são chamados de ``int``

- Números com casas decimais são chamados de ``float``

Para identificarmos o tipo de dado de um valor usamos o comando ``type()``


02. Texto (``string``) 
=====================

Texto em programação é um tipo de dado chamado de ``string``. 

Podem ser letras, palavras, textos, caracteres especiais (*&%$#)

.. warning::

  Sempre que usamos o tipo de dados string devemos usá-lo entre aspas (aspas simples ou dupla). 
  

Veja o exemplo para criar uma variável que o valor armazenado é um dado tipo ``string``:

.. code-block:: python
   :linenos:


   #Criando uma variável chamada estacao_do_ano e armazenando o valor verão
   estacao_do_ano = "Verão"
   
   
.. code-block:: python
   :linenos:
   
   #Vendo o tipo de dado armazenado na variável chamada estacao_do_ano
   type(estacao_do_ano)
   
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> str
   
 
03. Número inteiro (``int``)
=====================


Números inteiros em programação é um tipo de dado chamado ``int`` , ou seja, sem casa decimal.

Veja o exemplo para criar uma variável que o valor armazenado é um dado tipo ``int``:


.. code-block:: python
   :linenos:

   #Criando uma variável chamada quantidade_de_pessoas e armazenando o valor 12
   quantidade_de_pessoas = 12
   
   
.. code-block:: python
   :linenos:
   
   #Vendo o tipo de dado armazenado na variável quantidade_de_pessoas
   type(quantidade_de_pessoas)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> int
   
 
 
04. Número com casa decimal (``float``)
=====================

Números com casa decimal em programação é um tipo de dado chamado ``float``.

.. warning::
  
  Para indicar a separação decimal usamos o ponto “.” e não a vírgula “,”.


Veja o exemplo para criar uma variável que o valor armazenado é um dado tipo ``float``:


.. code-block:: python
   :linenos:

   #Criando uma variável chamada temperatura_do_corpo e armazenando o valor 37.5
   temperatura_do_corpo = 37.5
   
   
.. code-block:: python
   :linenos:
   
   #Vendo o tipo de dado armazenado na variável temperatura_do_corpo
   type(temperatura_do_corpo)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> float
   

05.Transformação de dados
========================

É muito comum precisarmos transformar os tipos de dados dependendo da nossa necessidade.

Para isso usamos os seguintes comandos para cada tipo de dado:


05.a.Transformar os dados para ``string`` (texto):
-------

.. code-block:: python
   :linenos:
   
   #Transformando o valor 99 em string
   str(99)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> '99'


05.b.Transformar os dados para ``int`` (número inteiro):
-----------

.. code-block:: python
   :linenos:
   
   #Transformando o valor 99.5 em int
   int(99.5)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 99
 
 
05.c.Transformar os dados para ``float`` (número com casa decimal):
----------

.. code-block:: python
   :linenos:
   
   #Transformando o valor 99 em float
   float(99)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> 99.0
   

06.Entrada de Dados
===================


0.6.a.Coletando dados pelo comando ``input()``
-------------------------------------------

Podemos solicitar que o usuário de um programa insira um valor. Por exemplo, quando fazemos um cadastro em sites e aplicativos.

Para isso usamos o comando ``input()``. 
Muitas vezes atribuímos o valor recebido pelo comando ``input()`` em uma variável.

Veja o exemplo para criar uma variável armazenando o dado recebido através do comando ``input()``:

.. code-block:: python
   :linenos:
   
   #Captando dados com o comando input()
   idade = inpput("Insira sua idade: ")
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> Insira sua idade: 20
   

0.6.b.Tipo de dado fornecido pelo comando ``input()``
-------------------------------------------

Independente do tipo de dado que o usuário forneça, o comando ``input()`` sempre irá nos fornecer um dado do tipo ``string``

.. code-block:: python
   :linenos:
   
   #Verificando o tipo de dado da variável idade
   type(idade)
   
**Este é o resultado:**
   
.. code-block:: python   
   
   >>> str
   
   
0.6.c.Transformando o dado fornecido pelo comando ``input()``
-------------------------------------------

Caso seja necessário transformar o tipo de dado fornecido pelo comando ``input()`` usamos a transformação de dados antes do dado ser atribuído na variável.

.. code-block:: python
   :linenos:
   
   #Captando dados com o comando input() e transformando em int.
   idade = int(inpput("Insira sua idade: "))
 
.. code-block:: python
   :linenos:
   
   #Verificando o tipo de dado da variável idade
   type(idade)

**Este é o resultado:**
   
.. code-block:: python   
   
   >>> int
