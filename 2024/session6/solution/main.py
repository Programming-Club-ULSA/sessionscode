from menu import Menu
import utils
import os


def horario_clase(schedule_data: dict, clase: str) -> list[str]:
    schedule_list = schedule_data[clase]

    schedule_str_list = []
    for schedule in schedule_list:
        day = schedule[0]
        hour = schedule[1]
        schedule_str_list.append(f"{day} en horario de {hour}")

    return schedule_str_list

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