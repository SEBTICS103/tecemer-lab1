import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from preparar_dataset import calcular_dia_lluvioso

def test_dia_con_lluvia_devuelve_uno():
    assert calcular_dia_lluvioso(2.5) == 1

def test_dia_sin_lluvia_devuelve_cero():
    assert calcular_dia_lluvioso(0.0) == 0

def test_precipitacion_negativa_se_trata_como_sin_lluvia():
    assert calcular_dia_lluvioso(-1.0) == 0