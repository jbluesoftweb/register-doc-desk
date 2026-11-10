import pytest

from registerdoc.domain.tipo_doc import LONGITUD_MAXIMA_NOMBRE, TipoDoc


def test_valores_por_defecto():
    tipo = TipoDoc("Oficio")
    assert tipo.nombre == "Oficio"
    assert tipo.activo is True
    assert tipo.id is None


def test_el_nombre_se_limpia_de_espacios():
    assert TipoDoc("  Informe  ").nombre == "Informe"


@pytest.mark.parametrize("nombre", ["", "   "])
def test_nombre_vacio_falla(nombre):
    with pytest.raises(ValueError):
        TipoDoc(nombre)


def test_nombre_demasiado_largo_falla():
    with pytest.raises(ValueError):
        TipoDoc("x" * (LONGITUD_MAXIMA_NOMBRE + 1))


def test_nombre_en_el_limite_es_valido():
    assert TipoDoc("x" * LONGITUD_MAXIMA_NOMBRE).nombre == "x" * LONGITUD_MAXIMA_NOMBRE


def test_dos_tipos_con_los_mismos_datos_son_iguales():
    assert TipoDoc("Oficio", id=1) == TipoDoc("Oficio", id=1)
    assert TipoDoc("Oficio", id=1) != TipoDoc("Oficio", id=2)