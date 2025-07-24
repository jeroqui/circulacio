from enum import Enum

class Sentit(Enum):
    DIRECCIO = "direcció"
    CONTRA_DIRECCIO = "contra direcció"

class Calçada:
    ...

class Carril(Calçada):
    ...


class Carretera:

    carrils = []

    def __init__(self, carrils: list[Carril]):
        if len(carrils) == 0:
            raise Exception("La carretera ha de tenir almenys un carril")

        self.carrils = carrils