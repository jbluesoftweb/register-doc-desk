from dataclasses import dataclass

LONGITUD_MAXIMA_NOMBRE = 50

@dataclass
class TipoDoc:
    nombre: str
    activo: bool = True
    id: int | None = None

    def __post_init__(self) -> None:
        self.nombre = self.nombre.strip()
        if self.nombre == "":
            raise ValueError("El nombre del tipo de documento es obligatorio.")
        if len(self.nombre) > LONGITUD_MAXIMA_NOMBRE:
            raise ValueError(f"El nombre no puede superar {LONGITUD_MAXIMA_NOMBRE} caracteres.")

