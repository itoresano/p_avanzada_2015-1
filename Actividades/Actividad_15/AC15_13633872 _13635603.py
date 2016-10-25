import unittest
from banco import Banco, CajeroAutomatico, Usuario


class TestCajeros(unittest.TestCase):

    def SetUp(self):
        self.banco = Banco("banco")
        self.cajero = CajeroAutomatico(self.banco)
        self.banco.agregar_usuario("rut2", "nombre2", "clave2")
        self.banco.agregar_usuario("rut", "nombre", "clave")
        self.banco.usuarios[0].saldo = 100000
        self.monto = 50000


    def test_credenciales(self):
        self.cajero.login(self.banco.usuarios[0].rut, self.banco.usuarios[0].clave)
        self.assertIsNotNone(self.banco.usuarioactual)
        self.cajero.login("rut_falso","clave_falsa")
        self.assertIsNone(self.banco.usuarioactual)

    def test_dinero_disponible(self):
        self.cajero.retirar_dinero('rut','clave',self.monto)
        self.assertGreaterEqual(self.banco.usuarioactual.saldo,0)
        self.monto = 100001
        self.assertGreaterEqual(self.banco.usuarioactual.saldo,0)

    def test_actualizacion_saldo(self):
        self.cajero.login('rut','clave')
        self.saldo_anterior = self.banco.usuarioactual.saldo
        self.cajero.retirar_dinero('rut','clave',self.monto)
        self.assertEqual(self.banco.usuarioactual.saldo, self.saldo_anterior - self.monto)

    def comprobar_tercero(self):
        self.cajero.transferir_dinero(self.banco.usuarios[0].rut, self.banco.usuarios[0].clave, self.banco.usuarios[1].rut, self.monto)
        self.assertisNotNone(self.banco.usuariotercero.rut)
        self.cajero.transferir_dinero(self.banco.usuarios[0].rut, self.banco.usuarios[0].clave, "rut_falso", self.monto)
        self.assertisNone(self.banco.usuariotercero)

    def monto_correcto(self):
        monto_inicial = self.banco.usuario[0].saldo
        monto_inicial2 = self.banco.usuario[1].saldo
        self.cajero.transferir_dinero(self.banco.usuarios[0].rut, self.banco.usuarios[0].clave, self.banco.usuarios[1].rut, self.monto)
        self.assertEqual(monto_inicial - self.monto, self.banco.usuarioactual.saldo)
        self.assertEqual(monto_inicial2 + self.monto, self.banco.usuariotercero.saldo)

    def error_transferencia(self):
        monto_inicial = self.banco.usuario[0].saldo
        self.cajero.transferir_dinero(self.banco.usuarios[0].rut, self.banco.usuarios[0].clave, "rut_falso", self.monto)
        self.assertEqual(self.banco.usuarioactual.saldo, monto_inicial)







if __name__ == "__main__":
    unittest.main()
