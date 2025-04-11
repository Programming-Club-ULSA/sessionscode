
def read_csv(file_path: str) -> dict:
    schedule_data = {}
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip header
            class_name, day, hour = line.strip().split(',')
            if class_name not in schedule_data:
                schedule_data[class_name] = []
            schedule_data[class_name].append((day, hour))
    return schedule_data