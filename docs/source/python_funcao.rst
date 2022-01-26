FUNÇÕES.
********************

Uma função é composta basicamente por duas partes:

.. code-block:: python
   :linenos:
   
   def nome_da_função( ):
    
    bloco de código da função
    
Podemos entender uma função como: 

- Função é um bloco de código que só é executado quando é chamado.

- Funções nos ajudam a diminuir repetições tornando o código mais organizado.

- Função é sempre uma ação de fazer algo.


01.Criando uma função
============

Para criar uma função usamos o comando ``def``.
    
Veja o exemplo de como criar e chamar uma função:

.. code-block:: python
   :linenos:
  
    #Criando uma função chamada parabens
    def parabens( ):
     
      #Estabelecendo o bloco de código que a função parabens irá executar
      print('Parabéns, você criou uma função.')

.. code-block:: python
   :linenos:
   
   #Chamando a função parabéns
   parabens()
 

**Este é o resultado:**

.. code-block:: python

   >>> Parabéns, você criou uma função.



02.Criando uma função com parâmetros
===================

Quando precisamos que a função seja executada de forma específica é necessário usar:

- **Parâmetro:** é a variável que recebe um valor (argumento) para ser usado na função.

- **Argumento:** valor atribuído ao parâmetro.

Uma função com parâmetros e argumentos é composta basicamente da seguinte forma:

.. code-block:: python
   :linenos:
   
   def nome_da_função(parametro_01 = argumento_01, parametro_02 = argumento_02):
    
    bloco de código da função


Veja o exemplo de como criar uma função com parâmetros e argumentos:

.. code-block:: python
   :linenos:
   
   #Criando uma função chamada barra um, com os "parâmetros quantidade" e "caracter" e com os argumentos "40" e "@" 
   def barra_01(quantidade=40, caracter='@'):
   
      #Estabelecendo o bloco de código que a função barra_01 irá executar
      print(quantidade*caracter)
      
.. code-block:: python
   :linenos:
   
   #Chamando a função barra_01
   barra_01()
   

**Este é o resultado:**

.. code-block:: python

   >>> @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   
.. warning::

   Repare que como não passamos nenhum argumento para a função, ela nos devolve os argumentos padrões ``(default)``, que neste caso é 40 vezes o símbolo '@'.
   
02.a.Alterando os argumentos de uma função
----------------


Pense na função ``barra_01``:

.. code-block:: python
   :linenos:
   
   #Criando uma função chamada barra um, com os "parâmetros quantidade" e "caracter" e com os argumentos "40" e "@" 
   def barra_01(quantidade=40, caracter='@'):
   
      #Estabelecendo o bloco de código que a função barra_01 irá executar
      print(quantidade*caracter)
      
      
Caso deseje alterar a quantidade e o símbolo do caracter, sem precisar toda vez ir onde definiu a função, você pode fazê-lo ao chamar a função.

Veja o exemplo de como alterar os argumentos de uma função na hora de chamá-la:

.. code-block:: python
   :linenos:
   
   #Chamando a função barra_01 e alterando os argumentos para "quantidade = 10" e "caracter = !"
   barra_01(quantidade = 10, caracter = !)
   
**Este é o resultado:**

.. code-block:: python

   >>> !!!!!!!!!!
   


03. Variáveis globais e variáveis locais
============

É importante saber que existem dois tipos de variáveis:


03.a.Variáveis globais
--------

É criada **fora** de uma função, estrutura de repetição ou condição. 
Ou seja, podemos acessar o seu valor em **qualquer parte do código**.


03.b.Variáveis locais
-------

É criada **dentro** de uma função, estrutura de repetição ou condição. 
Sendo inicializada (criada) a cada vez que chamamos a função ou seja **não podemos acessar o valor fora** da função, estrutura de repetição ou condição .


03.c.Veja o exemplo de uma variável global e variável local:
-----------

- Pense no seguinte código:

.. code-block:: python
   :linenos:
   
   #Criando uma variável global chamada "ano_nascimento"
   ano_nascimento = 1987
   
   #Criando uma função chamada descobrir_idade
   def descobrir_idade():
      
      #Criando uma variável local chamada "idade"
      idade = 2021 - ano_nascimento
      
      #Pedindo para estabelecer o valor 
      print('Minha idade é: ', idade)
      
.. note:: 

   - ``ano_nascimento`` é uma variável global.
  
   - ``idade`` é uma variável local.
   
03.c.i.Exemplo variável global
++++++++

Repare que podemos usar a variável global ``ano_nascimento`` fora da função:

.. code-block:: python
   :linenos:
   
   #Imprimindo a variável global chamada "ano_nascimento"
   print(ano_nascimento)
   
**Este é o resultado:**

.. code-block:: python

   >>> 1987
   
03.c.ii.Exemplo variável local 
++++++++

Repare que não podemos usar a variável local ``idade`` fora da função:

.. code-block:: python
   :linenos:
   
   #Imprimindo a variável local chamada "idade"
   print(idade)
   
**Este é o resultado:**

.. code-block:: python

   >>> NameError: name 'idade' is not defined


04.Comando ``return``
=======

Em muitos casos, usamos uma função para executar **um bloco de código que nos retorne algo**, por exemplo o resultado de uma conta.
Quando queremos realizar isso, utilizamos o comando ``return``

O comando return é composta basicamente da seguinte maneira:

.. code-block:: python
   :linenos:
   
   def nome_da_função( ):
    
    bloco de código da função
    
    return conteúdo desejado
    
Podemos entender o comando ``return`` como: 

- O comando return dentro de uma função, nos retorna algum conteúdo.

Veja o exemplo de como usar o comando ``return`` dentro de uma função:

.. code-block:: python
   :linenos:
  
    #Criando uma função chamada "area_triangulo" com os parâmetros base e altura
    def area_triangulo(base, altura):
      
      #Estabelecendo para a função calcular a área do triangulo
      area = base*altura/2
      
      #Utilizando o comando return para nos devolver o valor da área
      return area
      
 
.. code-block:: python
   :linenos:
   
   #Chamando a função area_triangulo com os argumentos desejados
   area_triangulo(8, 10)
 

**Este é o resultado:**

.. code-block:: python

   >>> 40
   
04.a.Trabalhando com o valor do comando ``return``
-----------

Caso você deseje trabalhar com o valor que o comando ``return`` devolveu, basta atribuí-lo a uma variável

Veja o exemplo de como trabalhar com o valor do comando ``return`` :

Pense na função ``area_triangulo`` que vimos acima. 

.. code-block:: python
   :linenos:
  
    #Criando uma variável chamada "resultado" e atribuindo o valor da função "area_triangulo" nela
    resultado = area_triangulo(8,10)
 
 
.. code-block:: python
   :linenos:
  
    #Imprimindo a variável chamada "resultado"
    print(resultado)
    
    
**Este é o resultado:**

.. code-block:: python

   >>> 40    
