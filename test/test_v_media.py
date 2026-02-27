import pytest
from escola import v_media

def test_aprovado():
    assert v_media(8) == "aprovado"

def test_reprovado():
    assert v_media(4) == "reprovado"

def test_recuperacao():
    assert v_media(5) == "recuperação"