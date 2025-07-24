


# Circulació

Aquest és un repositori amb l'objectiu de replicar amb codi la Llei de circulació
vigent a Catalunya (de moment espanya). Un projecte que emprenc per estudiar
per al test de teòrica.

Es tracta d'un repositori de Python, perquè és el llenguatge més senzill que conec.

El codi està elaborat a partir del text més recent de la Llei de circulació que
he estat capaç de trobar:
https://www.boe.es/boe_catalan/dias/2015/10/31/pdfs/BOE-A-2015-11722-C.pdf

## Organització

El plantejament del codi és el d'una simulació computada per "decisions", que
vindrien a ser "torns" d'acció de l'agent (conductor) - reacció de l'entorn.
Sempre des del punt de vista del "vehicle" protagonista simulat.

> Exemple: Si parlem de direcció o contra direcció, ho fem en relació amb el "vehicle"
> abstracte des del qual la Llei explica que "és conduït per nosaltres".

D'aquesta manera podem programar de forma bastant paral·lela les normes de trànsit
tal com es descriuen textualment a la Llei.
