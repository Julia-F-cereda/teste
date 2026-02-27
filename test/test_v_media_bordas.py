import pytest
from escola import v_media

@pytest.mark.parametrize( ("media", "resultado"),
                            [
                            (7, "aprovado"),
                            (5, "recuperação"),
                            (5.5, "recuperação"),
                            (0, "reprovado"),
                            (10, "aprovado"),
                             
                             
                             ]
                        )
def test_bordas(media, resultado):
    assert v_media(media) == resultado