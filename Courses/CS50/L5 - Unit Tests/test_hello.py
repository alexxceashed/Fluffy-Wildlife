from hello import hello 
def test_hello():
    names = ["Alex", "Daddy", "Ale", "SD"]
    for name in names:
        assert hello(name) == f"Hello, {name}"

def test_empty():
    assert hello() == "Hello, world"