from enum import Enum


class Rol(Enum):
    REGISTRADOR = 1
    ADMIN = 2
    SISTEMAS = 3

    @property
    def nivel(self) -> int:
        return self.value
    
    def tiene_al_menos(self, minimo: "Rol") -> bool:
        return self.nivel >= minimo.nivel
