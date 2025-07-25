from enum import Enum

class Sentit(Enum):
    DIRECCIO = "direcció"
    CONTRA_DIRECCIO = "contra direcció"

class Calçada:
    ...

class Carril(Calçada):
    es_lent = False
    es_reservat = False

class Carretera:

    carrils = []

    def __len__(self) -> int:
        # Article 16.2
        return len(list(filter(lambda x: not (x.es_reservat or x.es_lent), self.carrils)))


    def __init__(self, carrils: list[Carril]):
        if len(self) == 0:
            raise Exception("La carretera ha de tenir almenys un carril")

        self.carrils = carrils