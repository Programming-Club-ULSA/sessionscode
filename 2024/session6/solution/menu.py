
class Menu:
    def __init__(self, title: str = "Menu para buscar clases", options: list[str] = ["Clase 1", "Clase 2", "Clase 3"]):
        self.title = title
        self.options = options

    def show(self):
        print(self.title)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")
        print("0. Salir")

    def select_option(self):
        return int(input("Seleccione una opción: "))

