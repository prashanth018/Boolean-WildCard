# Boolean-WildCard
Procedure to compile the code:

Language used 	: Python 2.7

Requirements 	: NLTK installed
	          NLTK corpus downloaded

Corpus Used	: nltk.gutenberg


Run SearchEngine.py
Dictionary takes about 4 minutes to load.
A GUI would be displayed containing various components of the search engine.
Enter The search terms in the Query text box.
Select either Boolean Search or Wild Card Search from available radio buttons.
Click Search button
Results would be displayed in the text area.

Syntax for writing queries :

Boolean Queries	  : < Query >  -->  < A > (AND|OR) < Query > | < A >
		         < A > --> NOT < A > | Token

Wild Card Queries : X * Y | X * | * X | * X * (Any wild card query)
		    Space between terms is treated as AND operation.
