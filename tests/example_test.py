from example_package import example

def test_foo():
    assert example.example(3) == 4

def test_again():
    example.example(0)
