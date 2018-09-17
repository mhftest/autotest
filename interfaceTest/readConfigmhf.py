import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]      #D:\python\interfaceTest\testFile
print(proDir)
configPath = os.path.join(proDir, "config.ini")
print(configPath)

fd = open(configPath)
data = fd.read()
# print(data)
print(type(data))
print(data[:3])
print(codecs.BOM_UTF8)
print("=====")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

# r=ReadConfig()
# c=r.get_email("mail_host")
# print(c)
# print(type(c))