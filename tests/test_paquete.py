import importlib

import pytest

SUBPAQUETES = ["domain", "repositories", "services", "security", "ui", "db"]


def test_paquete_principal_se_importa():
    modulo = importlib.import_module("registerdoc")
    assert modulo is not None


@pytest.mark.parametrize("nombre", SUBPAQUETES)
def test_subpaquete_se_importa(nombre):
    modulo = importlib.import_module(f"registerdoc.{nombre}")
    assert modulo is not None