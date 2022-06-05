import json


class Quadrilatero:
    def __init__(self):
        self.tipo = None

    def le_dados(self):
        self.lado1 = float(input("Digite o valor do primeiro lado: "))
        self.lado2 = float(input("Digite o valor do segundo lado: "))
        self.lado3 = float(input("Digite o valor do terceiro lado: "))
        self.lado4 = float(input("Digite o valor do quarto lado: "))

    def indica_tipo_quadrilatero(self):
        if self.tipo != None:
            return self.tipo
        if (
            self.lado1 == self.lado2
            and self.lado2 == self.lado3
            and self.lado3 == self.lado4
        ):
            self.tipo = "Quadrado"
        elif (
            self.lado1 == self.lado3
            and self.lado2 == self.lado4
            and self.lado1 != self.lado2
        ):
            self.tipo = "Retângulo"
        else:
            self.tipo = "Quadrilátero"

    def __str__(self):
        return f"{self.tipo}: L1 = {self.lado1}, L2 = {self.lado2}, L3 = {self.lado3}, L4 = {self.lado4}"

    def mostra_dados(self):
        print(self)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(json_str):
        obj = Quadrilatero()
        obj.__dict__ = json.loads(json_str)
        return obj
