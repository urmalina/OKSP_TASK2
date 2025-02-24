# user_input.py

class UserInput:
    """Класс для получения ввода от пользователя."""
    def __init__(self):
        pass

    def get_part_and_color(self):
        """Запрашивает у пользователя деталь и цвет."""
        print("Введите наименование детали (например, капот, передняя дверь, крыша):")
        part = input().strip().lower()

        print("Введите цвет (белый, синий, желтый, красный, перламутровый, серый металлик):")
        color = input().strip().lower()

        return part, color