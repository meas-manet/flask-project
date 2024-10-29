class LoginDto:
    __uname = None;
    __upass = None;
    __confirm_code = None;

    @property
    def UName(self):
        return self.__uname

    @UName.setter
    def UName(self, value):
        self.__uname = value

    @property
    def UPass(self):
        return self.__upass

    @UPass.setter
    def UPass(self, value):
        self.__upass = value

    @property
    def ConfirmCode(self):
        return self.__confirm_code

    @ConfirmCode.setter
    def ConfirmCode(self, value):
        self.__confirm_code = value

    @staticmethod
    def toDict(self):
        return {"uname": self.__uname, "upass": self.__upass, "confirm_code": self.__confirm_code}

    @staticmethod
    def printme():
        print("Hello!")
