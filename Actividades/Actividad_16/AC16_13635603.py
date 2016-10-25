import pytest
import string
import encriptador
import os

# Para verificar que la funcion es biyectiva puedes usar:
def check_bijection(rot):
    dom = 26
    rec = []
    num = []

    for x in range(dom):
        num.append(x)
        y = rot.get(x)
        assert y is not None
        rec.append(y)

    assert set(num) == set(rec)


def setup_module(module):
    encriptador.create_alphabet((list(string.ascii_lowercase)))


class TestRotor:

    def setup_class(cls):
        cls.rotors = []
        for i in range(1, 4):
            cls.rotors.append(
                encriptador.Rotor('files\\rotor{0}.txt'.format(i))
            )

    def test_function(self):
        for i in self.rotors:
            check_bijection(i)



class TestReflector:

    def setup_class(cls):
        cls.reflector = encriptador.Reflector('files\\reflector.txt')

    def test_function(self):
        # Puedes usar al reflector llamando: self.reflector
        check_bijection(self.reflector)
        num = []
        for i in range(26):
            num.append(i)
            y = self.reflector.get(i)
            assert y is not None
            assert self.reflector.get(y) == i


class TestEncoder:
    lista= ['thequickbrownfoxjumpsoverthelazydog', 'python', 'bang', 'libelula', 'csharp']

    def setup_class(cls):
        rots = ['files\\rotor1.txt', 'files\\rotor2.txt', 'files\\rotor3.txt']
        refl = 'files\\reflector.txt'
        cls.enc = encriptador.Encoder(rots, refl)

    def test_encoding(self):
        for i in TestEncoder.lista:
            y = self.enc.encrypt(i)
            assert y != i
            assert self.enc.encrypt(y) == i

    def test_exception(self):
        with pytest.raises(ValueError):
            excepcion = "ñandu"
            self.enc.encrypt(excepcion)


