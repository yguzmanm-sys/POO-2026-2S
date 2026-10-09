class CuentaBancaria:
    def __init__(self, nombresTitular: str, apellidosTitular: str,
                 numeroCuenta: int, tipoCuenta: str):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.saldo = 0.0

    def imprimir(self):
        print("Nombres del titular =", self.nombresTitular)
        print("Apellidos del titular =", self.apellidosTitular)
        print("Número de cuenta =", self.numeroCuenta)
        print("Tipo de cuenta =", self.tipoCuenta)
        print("Saldo =", self.saldo)

    def consultarSaldo(self):
        print("El saldo actual es =", self.saldo)
        return self.saldo

    def consignar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor}. Nuevo saldo: ${self.saldo}")
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    def retirar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor}. Nuevo saldo: ${self.saldo}")
            return True
        print("El valor a retirar debe ser menor o igual al saldo actual y mayor que cero.")
        return False

    def compararCuenta(self, cuenta: 'CuentaBancaria') -> bool:
        return (self.numeroCuenta == cuenta.numeroCuenta
                and self.nombresTitular == cuenta.nombresTitular
                and self.apellidosTitular == cuenta.apellidosTitular
                and self.tipoCuenta == cuenta.tipoCuenta)

    def transferencia(self, cuenta: 'CuentaBancaria', valor: float) -> bool:
        if self.retirar(valor):
            cuenta.consignar(valor)
            print(f"Se ha transferido ${valor} de la cuenta {self.numeroCuenta} a {cuenta.numeroCuenta}")
            return True
        print("No se pudo realizar la transferencia.")
        return False

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Pedro", "Pérez", 123456, "AHORROS")
    cuenta2 = CuentaBancaria("Juan", "López", 654321, "CORRIENTE")

    cuenta1.imprimir()
    cuenta1.consignar(500000)
    cuenta1.transferencia(cuenta2, 200000)
    cuenta1.consultarSaldo()
    cuenta2.consultarSaldo()
