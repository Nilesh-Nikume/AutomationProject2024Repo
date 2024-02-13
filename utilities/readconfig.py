import configparser

config = configparser.RawConfigParser()
config.read("D:\\pythonProject4\\Configure\\config.ini")


class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password
