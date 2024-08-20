import json


class DataBase:

    # @staticmethod
    def add_data(self, name, mail, pw):
        with open('db.json', 'r') as rf:
            database = json.load(rf)

        if mail in database:
            return 0
        else:
            database[mail] = [name, pw]
            with open("db.json", 'w') as wf:
                json.dump(database, wf)
            return 1

    def search(self, email, pw):

        with open('db.json', 'r') as rf:
            database = json.load(rf)

            if email in database:
                if database[email][1] == pw:
                    return 1
                else:
                    return 0
            else:
                return 0
