from carretera import Calçada, Sentit



class Vehicle:

    passatgers = []
    conductor = None

    carretera = None

    # Propietats
    es_de_mobilitat_reduida = False

    sentit = Sentit.DIRECCIO

    def condiuir(self):
        if self.conductor is None:
            raise Exception("Un cotxe no pot estar no tripulat.")

        if self.carretera is None:
           raise Exception("Cal conduir per una carretera habilitada.")


        # Article 16.1
        if not any([
            self.es_de_mobilitat_reduida,
            # TODO: "es un vehicle especial amb la masa maxima autoritzada que es determini regulatoriament"
        ]):
            if not issubclass(Calçada, self.carretera.carril_actual()):
                raise Exception("Article 16.1: Cal conduir per la calçada")

            # 16.1 a
            if (
                self.carretera.doble_sentit
                and self.carretera.carrils_sentit(self.sentit)
            ):
                if not self.carretera.carril_actual().dreta:
                    raise Exception("Article 16.1.a: Cal conduir per la dreta")

            # 16.1 b
            # TODO.

class VehicleAMotor(Vehicle):
    ...

class VehicleNoMotor(Vehicle):
    ...

class VehicleEspecial(VehicleAMotor):
    ...

class Automovil(VehicleAMotor):
    ...