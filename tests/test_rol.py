import pytest

from registerdoc.domain.rol import Rol


def test_niveles_de_cada_rol():
    assert Rol.REGISTRADOR.nivel == 1
    assert Rol.ADMIN.nivel == 2
    assert Rol.SISTEMAS.nivel == 3


@pytest.mark.parametrize(
    ("rol", "minimo", "esperado"),
    [
        (Rol.REGISTRADOR, Rol.REGISTRADOR, True),
        (Rol.REGISTRADOR, Rol.ADMIN, False),
        (Rol.REGISTRADOR, Rol.SISTEMAS, False),
        (Rol.ADMIN, Rol.REGISTRADOR, True),
        (Rol.ADMIN, Rol.ADMIN, True),
        (Rol.ADMIN, Rol.SISTEMAS, False),
        (Rol.SISTEMAS, Rol.REGISTRADOR, True),
        (Rol.SISTEMAS, Rol.ADMIN, True),
        (Rol.SISTEMAS, Rol.SISTEMAS, True),
    ],
)
def test_tiene_al_menos(rol, minimo, esperado):
    assert rol.tiene_al_menos(minimo) is esperado


def test_rol_se_obtiene_por_nombre():
    assert Rol["ADMIN"] is Rol.ADMIN


def test_rol_inexistente_falla():
    with pytest.raises(KeyError):
        Rol["INVENTADO"]