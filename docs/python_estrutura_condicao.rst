ESTRUTURA DE CONDIÇÃO.
********************

01.Operadores de comparação
============

Em Python usamos os **operadores de comparação junto com a estrutura de condição**.

São eles:

+------------------------------+
|   OPERADORES DE COMPARAÇÃO   |
+------------------------------+
|         igual: a == b        |
+------------------------------+
|       não igual: a != b      |
+------------------------------+
|       menor que: a < b       |
+------------------------------+
|   menor ou igual a: a <= b   |
+------------------------------+
|       maior que: a > b       |
+------------------------------+
| maior ou igual a que: a >= b |
+------------------------------+


02. Estrutura de condição - ``if``
============

Muitas vezes é interessante decidir qual parte do código deve ser executada segundo uma condição e é para isso que existem as estruturas de condição, como por exemplo a ``if``.

A estrutura de condição ``if`` é composta basicamente por duas partes:

.. code-block:: python
   :linenos:
   
   if condição:
   
    execute esse bloco de código.

Podemos entender a estrutura de condição ``if`` como:

- ``if`` é o “se” em português. Portanto “se a condição for verdadeira, execute um bloco de código.”

Veja o exemplo de uma estrutura de condição ``if``:

.. code-block:: python
   :linenos:
   
   #Criando variáveis
   saldo = 300
   preco = 50
   
   #Estabelecendo uma condição de que se o saldo for maior que o preço
   if saldo > preco:
   
    #imprima o texto "compra aprovada"
    print("Compra aprovada")
   
**Este é o resultado:**

.. code-block:: python

   >>> Compra aprovada
   
.. warning::

  O bloco de código ``print("Compra aprovada")`` só foi executado pois a condição ``saldo > preco`` é verdadeira! Caso contrário, não seria executado. 
  
  
03.Identação
======

Identação nada mais é que o deslocamentodo código à direita/espaço em branco no início da linha.
Algumas coisas sobre identação:

- Em Python usa-se identação para  definir o escopo do bloco do código.

- Repare que usamos identação dentro de uma estrutura de condição como o ``if``

- A falta ou o excesso pode ocasionar erros no código.


04.Estrutura de condição - ``elif``.
=========

Usamos o ``elif`` quando a condição anterior não é verdadeira e queremos testar uma nova condição.

A estrutura de condição ``elif`` é composta basicamente da seguinte maneira:

.. code-block:: python
   :linenos:
   
   if condição:
   
    execute esse bloco de código.
    
   elif condição anterior não foi verdadeira:
   
    execute esse outro bloco de código.
    
Podemos entender a estrutura de condição ``elif`` como:

- ``elif`` é o “e se” em português. Portanto “e se a condição anterior não é verdadeira, então teste esta outra condição".

Veja o exemplo de uma estrutura de condição ``elif``:


.. code-block:: python
   :linenos:
   
   #Criando variáveis
   saldo = 300
   preco = 300
   
   #Estabelecendo uma condição de que se o saldo for maior que o preço
   if saldo > preco:
   
    #imprima o texto "compra aprovada"
    print("Compra aprovada")
   
   #Estabelecendo uma condição de que se o saldo for maior que o preço
   elif saldo == preco:
    
    #imprima o texto "compra aprovada , mas seu saldo é (0) zero)"
    print("Compra aprovada, mas seu saldo é (0) zero")
   
**Este é o resultado:**

.. code-block:: python

   >>> Compra aprovada, mas seu saldo é (0) zero
   
.. warning::

  O bloco de código ``print("Compra aprovada, mas seu saldo é (0) zero")`` só foi executado pois a condição ``saldo == preco`` é verdadeira! Caso contrário, não seria executado.
  
  
05.Estrutura de condição - ``else``.
=========

Usamos o ``else`` quando para executar um bloco de código quando o resultado de todas as condições anteriores não é verdadeira.

A estrutura de condição ``elif`` é composta basicamente da seguinte maneira:

.. code-block:: python
   :linenos:
   
   if condição:
   
    execute esse bloco de código.
    
   elif condição anterior não foi verdadeira:
   
    execute esse outro bloco de código.
    
   else:
   
    execute esse outro bloco de código.
    
Podemos entender a estrutura de condição ``else`` como:

- ``else`` é o “então” em português. Portanto “então nenhuma outra condição é verdadeira, faça isso".

Veja o exemplo de uma estrutura de condição ``else``:


.. code-block:: python
   :linenos:
   
   #Criando variáveis
   saldo = 300
   preco = 700
   
   #Estabelecendo uma condição de que se o saldo for maior que o preço
   if saldo > preco:
   
    #imprima o texto "compra aprovada"
    print("Compra aprovada")
   
   #Estabelecendo uma condição de que se o saldo for maior que o preço
   elif saldo == preco:
    
    #imprima o texto "compra aprovada , mas seu saldo é (0) zero)"
    print("Compra aprovada, mas seu saldo é (0) zero")
    
    #Caso nenhuma condição seja verdadeira
    else:
    
    #imprima o texto "Compra rescusada, saldo insuficiente"
    print("Compra rescusada, saldo insuficiente")
   
**Este é o resultado:**

.. code-block:: python

   >>> Compra rescusada, saldo insuficiente
   
.. warning::

  O bloco de código ``print("Compra rescusada, saldo insuficiente")`` só foi executado pois nenhuma das outras condições eram verdadeiras! Caso contrário, não seria executado.
  
  Repare também que não utilizamos nenhum operador de comparação no ``else`` pois presumimos que já tentamos de tudo e que o else é nossa última condição possível.
 

06.Operadores lógicos
=======

Dentro de estruturas de condições como o ``if``, usamos operadores lógicos para combinar duas ou mais condições.

06.a.Operador lógico ``and``
-------

Usamos o operador lógico ``and`` quando desejamos que a condição um **e** condição dois sejam verdadeiras.

O operador lógico ``and`` é composta basicamente por esse formato:

.. code-block:: python
   :linenos:
   
   if condição_1 and condição_2:
   
    execute esse bloco de código.

Podemos entender o operador lógico ``and`` como:

- ``and`` é o “e” em português. Portanto “se a condição for verdadeira **e** condição dois forem verdadeiras, execute um bloco de código.”

Veja o exemplo do operador lógico ``and``:

.. code-block:: python
   :linenos:
   
   #Criando variáveis
   a = 400
   b = 300
   c = 1000
   
   #Estabelecendo condições de que se a for maior que b e c maior que a
   if a>b and c>a:
   
    #imprima o texto "As duas condições são verdadeiras"
    print("As duas condições são verdadeiras")
   
**Este é o resultado:**

.. code-block:: python

   >>> As duas condições são verdadeiras
   
06.b.Operador lógico ``or``
-------

Usamos o operador lógico ``or`` quando desejamos que a condição um **ou** condição dois sejam verdadeiras.

O operador lógico ``or`` é composta basicamente por esse formato:

.. code-block:: python
   :linenos:
   
   if condição_1 or condição_2:
   
    execute esse bloco de código.

Podemos entender o operador lógico ``or`` como:

- ``or`` é o “ou” em português. Portanto “se a condição for verdadeira **ou** condição dois forem verdadeiras, execute um bloco de código.”

Veja o exemplo do operador lógico ``and``:

.. code-block:: python
   :linenos:
   
   #Criando variáveis
   a = 400
   b = 300
   c = 1000
   
   #Estabelecendo condições de que se a for maior que b e a for maior que c
   if a>b and a>c:
   
    #imprima o texto "Uma ou outra condição é verdadeira"
    print("Uma ou outra condição é verdadeira")
   
**Este é o resultado:**

.. code-block:: python

   >>> Uma ou outra condição é verdadeira
