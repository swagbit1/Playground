from bank import value

def main():
    test_different_start()
    test_case()


def test_case():
    assert value("hsduakygj") == 20
    assert value("Hasjhfmgkdasfj") == 20
    assert value("1286hwdukysfjd") == 100

def test_different_start():
    assert value("Hello how are you") == 0
    assert value("Hey how are you") == 20
    assert value("Hi how are you") == 20

