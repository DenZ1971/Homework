data = {}


class Controller:
    def user_interface(self):
        while True:
            action = input(
                "Добвить новую запись - введите 1 \n"
                "Вывести список всез записей - введите 2 \n"
                "Вывести данные одного пользователя - введите 3 \n")

            if action == '1':
                name = input("Введите имя пользователя ")
                email = input("Введите email пользователя ")
                if name not in data.keys():
                    a = {name: email}
                    Model.save_data(self, user=a)
                else:
                    return print('Имя уже существует в БД')
                return

            elif action == '2':
                Model.get_data(self)
                View.list_view(self)
                return


            elif action == '3':
                name_inst = input("Ввведите имя запрашиваемого пользователя\n")
                Model.get_data(self)
                if name_inst in data:
                    View.user_view(self, name_inst=name_inst)
                    return
                else:
                    return print("Такого имени нет в БД")
            else:
                print("Введите число от 1 до 3")


class View:

    def list_view(self):
        for key, value in data.items():
            print(f'Имя: {key}, электронная почта: {value}')

    def user_view(self, name_inst):
        return print(f'Привет {name_inst}, на вашу почту {data.get(name_inst)} отправлен подарок')


class Model:
    def save_data(self, user):
        data.update(user)
        return

    def get_data(self):
        return data



