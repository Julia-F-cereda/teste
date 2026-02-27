import pytest
from escola import v_media

def test_string():
    with pytest.raises(TypeError, match="Tipo invalido, entrada tem que ser numérica"):
        v_media("oito")