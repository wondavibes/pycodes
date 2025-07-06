from hola import hello

def test_hello():
    for name in ["Hert", "Dave", "Gabe"]:
        assert hello(name) == f"hola, {name}"
        