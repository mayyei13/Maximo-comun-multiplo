class NumeroNatural:
    def __init__(self):
        # Inicializa el atributo privado _numero
        self._numero = None

    @property  # Getter
    def numero(self):
        # Devuelve el valor del número
        return self._numero

    @numero.setter  # Setter
    def numero(self, valor):
        # Valida que el valor sea un entero positivo antes de asignarlo
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        self._numero = valor

    def solicitar_numero(self, mensaje):
        """
        Solicita un número entero positivo al usuario.
        Usa el setter para validar la entrada.
        """
        while True:
            entrada = input(mensaje)
            try:
                entrada = int(entrada)
                self.numero = entrada  # Se usa el setter para validar
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
            except Exception as e:
                print(e)

    @staticmethod
    def gcd(a, b):
        """
        Calcula el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides.
        Este método es estático porque no depende de una instancia específica.
        """
        while b != 0:
            a, b = b, a % b
        return a


# --- Uso del programa principal ---
if __name__ == "__main__":
    # Crear dos instancias de NumeroNatural
    numero1 = NumeroNatural()
    numero2 = NumeroNatural()

    # Solicitar al usuario ambos números
    numero1.solicitar_numero("Ingrese el primer número entero positivo: ")
    numero2.solicitar_numero("Ingrese el segundo número entero positivo: ")

    # Calcular el MCD usando el método estático
    resultado = NumeroNatural.gcd(numero1.numero, numero2.numero)

    # Mostrar el resultado
    print(f"El Máximo Común Divisor de {numero1.numero} y {numero2.numero} es: {resultado}")

