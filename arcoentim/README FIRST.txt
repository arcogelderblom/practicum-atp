In deze korte README willen wij kort toelichten waar in de repository de juiste files te 
vinden zijn. Allereerst zijn het testplan en de testrapportage te vinden in deze map. Onder 
de naam: 
*	Testplan: 'Testplan Advanced technical programming.pdf'
*	Testrapportage: 'Testrapport.docx'

De simulator in Python is te vinden in de map 'simulator'. Wanneer de main.py wordt 
gedraaid zal de simulator starten. Afhankelijk van de waarde van 'usingHardware' binnen het 
bestand 'gui.py' zal de simulator zelf simuleren of een aangesloten lemonator verwachten. 
Hierbij staat True voor het gebruiken van de hardware en moet er dus een lemonator 
aangesloten zijn, False staat voor het gebruiken van eigen waarden. Wanneer er False wordt 
gekozen wordt er gebruik gemaakt van geijkte waarden.

Onder vkatp-lemonator/cplusplustopython/ staan de bestanden waarbij vanuit C++ Python 
aangesproken wordt. Het werkt aan de hand van de simulator en hierbij zullen dan ook 
dezelfde bestanden te vinden zijn als in de eerdere simulator klasse. Wanneer er in de 
main.cpp gekeken wordt is er een reeks aan bijzondere functies te zien. Deze waren 
noodzakelijk om pybind werkend te krijgen. Zonder deze regels is het onmogelijk om pybind 
te gebruiken. Het heeft ons erg veel tijd gekost om deze fix te vinden en werkend te krijgen.
