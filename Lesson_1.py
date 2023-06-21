
class Model:
    data = {}

    def save_data(self, *args):
        self.data.update(*args)
        return

    def get_data(self):
        return self.data


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def user_add(self):
        name = input("Введите имя пользователя ")
        email = input("Введите email пользователя ")
        data = self.model.get_data()
        if name not in data.keys():
            a = {name: email}
            self.model.save_data(a)
        else:
            return print(f'Имя {name} уже существует в БД')
        return

    def users_list(self):
        data = self.model.get_data()
        self.view.list_view(data=data)
        return

    def get_user(self):
        name_inst = input("Ввведите имя запрашиваемого пользователя\n")
        data = self.model.get_data()
        if name_inst in data:
            self.view.user_view(name_inst=name_inst, data=data)
            return
        else:
            return print(f"Имени {name_inst} нет в БД")


class View:
    def list_view(self, data):
        for key, value in data.items():
            print(f'Имя: {key}, электронная почта: {value}')

    def user_view(self, name_inst, data):
        return print(f'Привет {name_inst}, на вашу почту {data.get(name_inst)} отправлен подарок')


def user_interface():
    while True:
        action = input(
            "Добвить новую запись - введите 1 \n"
            "Вывести список всез записей - введите 2 \n"
            "Вывести данные одного пользователя - введите 3 \n")

        if action == '1':
            Controller().user_add()

        elif action == '2':
            Controller().users_list()

        elif action == '3':
            Controller().get_user()
