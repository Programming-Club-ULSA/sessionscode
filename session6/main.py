from menu import Menu
import utils
import os


def horario_clase(schedule_data: dict, clase: str) -> list[str]:
    # Buscar la clase en el diccionario de horarios y retornar su horario en forma de lista de strings
    pass

def main():
    schedule_data = utils.read_csv(os.path.join("schedule.csv"))
    course_names = list(schedule_data.keys())

    menu = Menu("Menu para buscar clases", course_names)

    while True:
        menu.show()
        option = menu.select_option()
        if option == 0:
            break
        print(f"La clase {option} {course_names[option - 1]} "
              f"tiene el siguiente horario:")

        for schedule in horario_clase(schedule_data, course_names[option - 1]):
            print(schedule)

        input("Presione Enter para continuar...")



if __name__ == "__main__":
    main()