import json
import os


class Connector:

    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """

    def __init__(self, data_file: str) -> None:
        self.__data_file = data_file
        self.__path_file = None
        self.data_file = data_file

    @property
    def data_file(self) -> str:
        return self.__data_file

    @data_file.setter
    def data_file(self, value: str) -> None:
        self.__data_file = value
        self.__connect()

    def __connect(self) -> None:
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        # Создает файл, если его не существует
        self.__path_file = os.path.join(os.getcwd(), "data", self.__data_file)
        check_file = os.path.isfile(self.__path_file)
        if check_file is False:
            my_file = open(self.__path_file, "w+", encoding="utf8")
            my_file.close()
            print(f"Файл {self.__data_file} для хранения данных создан.")

    def insert(self, data: str) -> None:
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        json_object = json.dumps(data, indent=4, ensure_ascii=False)
        with open(self.__path_file, "w", encoding='utf-8') as write_file:
            write_file.write(json_object)
            print(f"Заносим данные в файл {self.__data_file}.")

    def select(self, query: dict) -> list:
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        # Счытывает информацию из файла
        data_filter = []
        with open(self.__path_file, "r", encoding='utf-8') as read_file:
            datas = json.load(read_file)
            print(datas)
        if query == {"*": "*"}:
            for data in datas:
                data_filter.append(data)
        else:
            # Поиск данных в списке словарей по ключу
            for data in datas:
                search_key = data.get(*query, None)
                if search_key is not None:
                    if search_key == list(query.values())[0]:
                        data_filter.append(data)
        return data_filter

    def delete(self, query: dict) -> None:
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        # Список который не попадает под условия фильрации, его будем сохранять
        data_not_delete = []
        # Счытывает информацию из файла
        with open(self.__path_file, "r", encoding='utf-8') as read_file:
            datas = json.load(read_file)

        # Поиск данных в списке словарей по ключу и удаление
        for data in datas:
            search_key = data.get(*query, None)
            if search_key is not None:
                if search_key != list(query.values())[0]:
                    data_not_delete.append(data)

        # Запись информации в файл
        json_object = json.dumps(data_not_delete, indent=4, ensure_ascii=False)
        with open(self.__path_file, "w", encoding='utf-8') as write_file:
            write_file.write(json_object)

    def __len__(self):
        return len(self.select({"*": "*"}))

    def validate(self):
        try:
            with open(self.__path_file, "r", encoding='utf-8') as read_file:
                json.load(read_file)
        except ValueError:
            print("! Файл для обработки неверного формата, либо пустой !\n")
        return False



