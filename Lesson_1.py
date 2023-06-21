
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

    def user_add(self, name, email):
        data = self.model.get_data()
        if name not in data.keys():
            a = {name: email}
            self.model.save_data(a)
        else:
            return False
        return True

    def users_list(self):
        data = self.model.get_data()
        return self.view.list_view(data=data)


    def get_user(self, name_inst):
        data = self.model.get_data()
        if name_inst in data:
            return self.view.user_view(name_inst=name_inst, data=data)
        else:
            return f"Имени {name_inst} нет в БД"


class View:
    def list_view(self, data):
        for key, value in data.items():
            print(f'Имя: {key}, электронная почта: {value}')

    def user_view(self, name_inst, data):
        return (f'Привет {name_inst}, на вашу почту {data.get(name_inst)} отправлен подарок')


def user_interface():
    while True:
        action = input(
            "Добвить новую запись - введите 1 \n"
            "Вывести список всез записей - введите 2 \n"
            "Вывести данные одного пользователя - введите 3 \n")

        if action == '1':
            name = input("Введите имя пользователя ")
            email = input("Введите email пользователя ")
            if Controller().user_add(name, email):
                print("Пользователь успешно добавлен в БД")
            else:
                print(f"Пользователь с именем {name} уже есть в БД")


        elif action == '2':
            Controller().users_list()

        elif action == '3':
            name_inst = input("Ввведите имя запрашиваемого пользователя\n")
            print(Controller().get_user(name_inst))
