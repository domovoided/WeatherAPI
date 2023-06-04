class CantGetCoordinates(Exception):
    def __init__(self, city_name: str = None):
        if city_name:
            self.message = f'Программа не может получить координаты города "{city_name}"'
        else:
            self.message = f'Программа не может получить ваши координаты'
