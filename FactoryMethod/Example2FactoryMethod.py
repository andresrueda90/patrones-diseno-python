from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def deliver(self):
        pass

    def transporte(self) -> str:
        # Call the factory method to create a Product object.
        transporte = self.deliver()

        # Now, use the product.
        result = f"Creator: transporte {transporte.enviar()}"

        return result


class Transporte(ABC):

    @abstractmethod
    def enviar(self) -> str:
        pass


class Aereo(Transporte):
    def enviar(self) -> str:
        return "Ya se encuentra el paquete en el avion"


class Terrestre(Transporte):
    def enviar(self) -> str:
        return "Ya se encuentra el paquete en el camion"


class Carro(Creator):

    def deliver(self) -> Transporte:
        return Terrestre()


class Avion(Creator):
    def deliver(self) -> Transporte:
        return Aereo()


def despachar_carga(creator: Creator) -> None:
    print(f"Client: Se ha iniciado el despacho de carga.\n"
          f"{creator.transporte()}", end="")


if __name__ == "__main__":
    print("App: Despachar Carga ")
    despachar_carga(Carro())
    print("\n")

    print("App: Despachar Carga .")
    despachar_carga(Avion())
