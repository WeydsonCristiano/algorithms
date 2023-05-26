import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("Cristiano", "0")

    with pytest.raises(TypeError):
        encrypt_message(0, 0)

    message = "Sambatech"
    key = len(message) // 2
    output = "etabmaScha"
    assert encrypt_message(message, key) == output

    key_big = 1000
    correct_message = "paralelepipedo"
    output_expected = "odidepilelalap"

    assert encrypt_message(correct_message, key_big) == output_expected
