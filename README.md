


# Circulacio

Aquest es un repositori amb l'objectiu de replicar amb codi la llei de circulació
vigent a Catalunya (de moment espanya). Un projecte que emprenc per estudiar
per el test de teorica.

Es tracta d'un repositori de python, perque es el llenguatge més senzill que conec.

El codi esta elaborat a partir del text més recent de la llei de circulació que
he estat capaç de trobar:
https://www.boe.es/boe_catalan/dias/2015/10/31/pdfs/BOE-A-2015-11722-C.pdf

Al [Portal Jurídic de Catalunya](https://portaljuridic.gencat.cat/ca/) hi ha la versió oficial catalana del [Reial decret legislatiu 6/2015, de 30 d’octubre, pel qual s’aprova el text refós de la Llei sobre trànsit, circulació de vehicles de motor i seguretat viària](https://portaljuridic.gencat.cat/ca/document-del-pjur/?documentId=717689) (en PDF i també RDF, TTL i XML).

## Organització

El plantejament del codi és el d'una simulació computada per "decisions", que
vindrien a ser "torns" de acció de l'agent (conductor) - reacció de l'entorn.
Sempre des del punt de vista del "vehicle" protagonista simulat.

> Exemple: Si parlem de direcció o contra direcció, ho fem en relació al "vehicle"
> abstracte des del que parlaria la llei que "és conduit per nosaltres".

D'aquesta manera podem programar de forma bastant paralela les normes de transit
tal com es descriuen textualment a la llei.

