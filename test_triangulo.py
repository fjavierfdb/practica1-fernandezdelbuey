import pytest
from triangulo import checktriangle

def test_caso1():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"

def test_caso2():
    assert checktriangle(3, 3, 4) == "Triangulo isosceles"

def test_caso3():
    assert checktriangle(6, 6, 6) == "Triangulo equilatero"

def test_caso4():
    assert checktriangle(4, 3, 0) == "No es un triangulo"

def test_caso5():
    assert checktriangle(8, 2, 4) == "No es un triangulo"

def test_caso6():
    assert checktriangle(3, 7, 2) == "No es un triangulo"

def test_caso7():
    assert checktriangle(6, 3, 10) == "No es un triangulo"

def test_caso8():
    assert checktriangle(3, 4, 4) == "Triangulo isosceles"

def test_caso9():
    assert checktriangle(4, 5, 4) == "Triangulo isosceles"

def test_caso10():
    assert checktriangle(5, 2, 5) == "Triangulo isosceles"

def test_caso11():
    assert checktriangle(3, 4, 7) == "No es un triangulo"

def test_caso12():
    assert checktriangle(7, 3, 4) == "No es un triangulo"

def test_caso13():
    assert checktriangle(0, 0, 0) == "No es un triangulo"

def test_caso14():
    assert checktriangle(-3, 4, 4) == "No es un triangulo"
