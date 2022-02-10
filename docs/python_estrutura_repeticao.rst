Estrutura de repetição
********************

01.Estrutura de repetição ``while``
============

A estrutura de repetição ``while`` é composta basicamente por duas partes:

.. code-block:: python
   :linenos:
   
   while condição:
   
    execute esse bloco de código.

Podemos entender a estrutura de condição ``while`` como:

- ``while`` é o “enquanto” em português. Portanto “enquanto a condição for verdadeira, execute esse bloco de código.”

Veja o exemplo de uma estrutura de repetição ``while``:

.. code-block:: python
   :linenos:
  
     #Criando uma variável chamada número e atribuíndo o valor de um
     numero = 1

     #Estabelecendo que enquanto número for menor que 6
     while numero < 6:

       #imprima o valor do número
       print(numero)

       #salve o valor atual da variável numero + 1 dentro da variável numero
       numero = numero + 1

**Este é o resultado:**

.. code-block:: python

   >>> 1
   >>> 2
   >>> 3
   >>> 4
   >>> 5

01.a.Incremento de variável
------

Na maioria das vezes usamos um incremento da variável dentro da estrutura de repetição ``while`` para que ela altere de valor e assim altere o estado da condição (verdadeiro ou falso).

Para incrementarmos o valor de uma variável numérica em uma unidade, podemos fazer de duas formas:

01.a.i.Adicionando uma unidade
++++++

.. code-block:: python
   :linenos:
   
   variavel = variavel + 1

______________________________________________________________________________________________________________________________________________

01.a.ii.Usando um operador de atribuição especial
++++++

.. code-block:: python
   :linenos:
   
   variavel += 1
   
 
01.a.iii.Looping infinito
+++++

.. warning::

  Caso uma condição do while sempre fique verdadeira, o while entrará em looping infinito (repetição infinita)
  
Veja o exemplo de um looping infinito:

.. code-block:: python
   :linenos:
  
   #Criando uma variável chamada número e atribuíndo o valor de um
   numero = 1
  
   #Criando um looping infinito
   while numero:
  
      #imprima o valor do número
      print(numero)
    
      #salve o valor atual da variável numero + 1 dentro da variável numero
      numero = numero + 1
  
  
**Este é o resultado:**

.. code-block:: python

   >>> 1
   >>> 2
   >>> ...
   >>> 4051
   >>> 4052
   >>> ...
   
01.b.Comando ``break``
------

Com o comando ``break`` (pausa) podemos pausar a repetição mesmo se a condição ainda for verdadeira.

Veja o exemplo do comando ``break``:

.. code-block:: python
   :linenos:
  
   #Criando uma variável chamada número e atribuíndo o valor de um
   numero = 1
  
   #Estabelecendo que enquanto número for menor que 6
   while numero < 6:
  
      #imprima o valor do número
      print(numero)
    
      #criando uma condição
      if numero == 3:
    
         #utilizando o comando break para encerrar a repetição
         break
    
      #salve o valor atual da variável numero + 1 dentro da variável numero
      numero = numero + 1

**Este é o resultado:**

.. code-block:: python

   >>> 1
   >>> 2
   >>> 3
   

01.c.Comando ``continue``
------

Com o comando continue podemos parar a repetição e continuar com o próximo bloco de código.

Veja o exemplo do comando ``continue``:

.. code-block:: python
  :linenos:
  
  #Criando uma variável chamada número e atribuíndo o valor de um
  numero = 0
  
  #Estabelecendo que enquanto número for menor que 6
  while numero < 6:
  
    #imprima o valor do número
    print(numero)
    
    #criando uma condição
    if numero == 3:
    
      #utilizando o comando continue para encerrar a repetição e continuar com o próximo bloco de código
      continue
    
    #salve o valor atual da variável numero + 1 dentro da variável numero
    numero = numero + 1

**Este é o resultado:**

.. code-block:: python

   >>> 1
   >>> 2
   >>> 4
   >>> 5
   >>> 6


02.Estrutura de repetição ``for``
============

Com a estrutura de repetição ``for`` executamos um bloco de código uma vez **para cada item** de uma estrutura de dados (Ex: listas, tuplas, dicionários).

A estrutura de repetição ``for`` é composta basicamente por duas partes:

.. code-block:: python
   :linenos:
   
   for variável in estrutura de dados:
   
    execute esse bloco de código.

Podemos entender a estrutura de condição ``for`` como:

- ``for`` é o “para” em português. Portanto “para esta variável nesta estrutura de dados, execute esse bloco de código.”

Veja o exemplo de uma estrutura de repetição ``for``:

.. code-block:: python
   :linenos:
  
   #Criando uma estrutura de dados 
   lista_compra = ['laranja', 'limão', 'maracujá', 'goiaba']
   
   #Establecendo para o for atribuir a variável "fruta" cada item da estrutura lista_compra
   for fruta in lista_compra:
      
      #imprimir o valor atribuído a variável fruta
      print(fruta)

**Este é o resultado:**

.. code-block:: python

   >>> laranja
   >>> limão
   >>> maracujá
   >>> goiaba
  
  
.. warning::

   Para cada item da lista o ``for`` atribui este item à uma variável (que funciona somente dentro do for e em seguida executa um bloco de código.
   
   
02.a.Comando ``break``
------

Com o comando ``break`` podemos parar a repetição antes de percorrer todos os itens da lista.

Veja o exemplo de como usar o comando ``break`` em uma estrutura de repetição ``for``:

.. code-block:: python
   :linenos:
  
   #Criando uma estrutura de dados 
   lista_compra = ['laranja', 'limão', 'maracujá', 'goiaba']
   
   #Establecendo para o for atribuir a variável "fruta" cada item da estrutura lista_compra
   for fruta in lista_compra:
      
      #imprimir o valor atribuído a variável fruta
      print(fruta)
      
      #estabelecendo a condição de que se o valor atribuído a variável fruta for igual limão
      if fruta == 'limão':
    
         #encerre essa repetição    
         break

**Este é o resultado:**

.. code-block:: python

   >>> laranja
   >>> limão
   

02.b.Comando ``continue``
------

Com o comando ``continue`` podemos parar a repetição atual e continuar com a próxima repetição.

Veja o exemplo de como usar o comando ``continue`` em uma estrutura de repetição ``for``:

.. code-block:: python
   :linenos:
  
   #Criando uma estrutura de dados 
   lista_compra = ['laranja', 'limão', 'maracujá', 'goiaba']
   
   #Establecendo para o for atribuir a variável "fruta" cada item da estrutura lista_compra
   for fruta in lista_compra:
      
      #imprimir o valor atribuído a variável fruta
      print(fruta)
      
      #estabelecendo a condição de que se o valor atribuído a variável fruta for igual limão
      if fruta == 'limão':
    
         #encerre essa repetição e continue na para a próxima  
         continue

**Este é o resultado:**

.. code-block:: python

   >>> laranja
   >>> maracujá
   >>> goiaba
   
02.b.Comando ``range()``
------

Para repetir um bloco de código uma quantidade específica de vezes usamos o comando ``range()``, que nos retorna uma sequência de números.

Veja o exemplo de como usar o comando ``range`` em uma estrutura de repetição ``for``:

.. code-block:: python
   :linenos:
   
   #Establecendo para o for atribuir a variável "i" os valores 0 à 5
   for i in range(5):
      
      #imprimir o valor atribuído a variável "i"
      print(i)

**Este é o resultado:**

.. code-block:: python

   >>> 0
   >>> 1
   >>> 2
   >>> 3
   >>> 4
   
   
 Podemos entender o comando ``range()`` como:

- ``range()`` significa “faixa” em português. Portanto “para esta variável nesta faixa, execute esse bloco de código.”

02.b.i.Padrões do comando ``range()``
++++++++

Por padrão o comando ``range()```sempre começa por 0 (zero), mas podemos alterar desta forma:

.. code-block:: python
   :linenos:
   
   for i in range(inicio, fim)
   
.. warning::

   No comando ``range()`` o **início é incluso** e o **fim não é incluso**
   
Veja o exemplo de como alterar o comando ``range`` em uma estrutura de repetição ``for``:

.. code-block:: python
   :linenos:
   
   #Establecendo para o for atribuir a variável "i" os valores 3 à 7
   for i in range(3, 7):
      
      #imprimir o valor atribuído a variável "i"
      print(i)

**Este é o resultado:**

.. code-block:: python

   >>> 3
   >>> 4
   >>> 5
   >>> 6
   

02.b.ii.Incremento com o comando ``range()``
++++++++

Por padrão o comando ``range()```sempre incrementa um valor unitário (1), mas podemos alterar desta forma:

.. code-block:: python
   :linenos:
   
   for i in range(inicio, fim, incremento)
   
Veja o exemplo de como usar o incremento com o comando ``range`` em uma estrutura de repetição ``for``:

.. code-block:: python
   :linenos:
   
   #Establecendo para o for atribuir a variável "i" os valores 2 à 10, sempre pulando de 2 em 2
   for i in range(2, 10, 2):
      
      #imprimir o valor atribuído a variável "i"
      print(i)

**Este é o resultado:**

.. code-block:: python

   >>> 2
   >>> 4
   >>> 6
   >>> 8
 
