class SimpleTest:

    person_list = []

    @staticmethod
    def fake_data():
        """Возвращаем тестовые данные"""

        return "Тетерин Глеб Ярославович, 14\n " \
               "Блинов Велор Ярославович, 21\n" \
                "Щербаков Гарри Протасьевич, 33\n" \
                "Носов Альфред Фролович, 65\n" \
                "Селиверстов Лавр Геласьевич, 9\n" \
                "Агафонов Корней Геннадиевич, 24\n" \
                "Сазонов Иосиф Павлович, 34\n" \
                "Данилов Осип Федотович, 12\n" \
                "Савин Вальтер Юлианович, 45\n" \
                "Филиппов Кассиан Артемович, 64\n" \
                "\n" \
                "\n"

    def print_person_lower_age(self, age):
        """Выводим на печать список персон младше age"""

        self.__parse_fake_data()
        self.person_list.sort(key = lambda x: x[1])
        for person in self.person_list:
            person_age, person_full_name = person[1], person[0].get_full_name()
            if person_age > age:
                break
            print("{} --> {}".format(person_full_name, person_age))

    def __parse_fake_data(self):
        """Парсим тестовые данные. Записываем в список кортежей (Person(), возраст)"""

        person_with_age_string_list = self.fake_data().split("\n")
        for person in person_with_age_string_list:
            if self.__check_test_data(person):
                person_and_age_list = person.split(',')
                self.person_list.append((self.__create_person(person_and_age_list[0]),
                                             int(person_and_age_list[1])))

    @staticmethod
    def __create_person(person_info):
        """Создаем экземпляр класса Person из строки ФИО"""

        person_data = person_info.split( )

        return Person(
            family_name=person_data[0],
            name=person_data[1],
            middle_name=person_data[2]
        )

    @staticmethod
    def __check_test_data(person_info):
        """Проверяем тестовые данные"""

        if len(person_info.split( )) == 4:
            return True


class Person(object):
    """Класс для хранения данных пользователя"""

    def __init__(self, family_name, middle_name, name):

        self.family_name = family_name
        self.middle_name = middle_name
        self.name = name

    def get_family_name(self):
        """Метод возвращает фамилию персоны"""

        return self.family_name

    def get_middle_name(self):
        """Метод возвращает отчество персоны"""

        return self.middle_name

    def get_name(self):
        """Метод возвращает имя персоны"""

        return self.name

    def get_full_name(self):

        return ' '.join([self.family_name, self.name, self.middle_name])

test = SimpleTest()
test.print_person_lower_age(30)


