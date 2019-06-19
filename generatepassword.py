import time
import random

import constants

class GeneratePassword:
    """
    Password Generator
        *args[level,lenght]
        level 1 -> lowercase chars
        level 2 -> lowercase and uppercase chars
        level 3 -> lowercase, uppercase and symbols
        level 4 -> lowercase, uppercase, sybols and timestamp
    """
    def __init__(self,level,length):
        self.__level = level
        self.__length = length
    def __generate_string(self,level,length):
        """
        Generates strings with uppercase, lowercase and symbol charcters for password.
        """
        string = []
        for i in range(0, length):
            r = random.random()
            if level == 1:
                # * only uppercase characters allowed
                upper_choise = random.choice(constants.upper_chars)
                string.append(upper_choise)
            elif level == 2:
                # * uppercase and lowercase chars allowed
                if r < 0.4:
                    lower_choise = random.choice(constants.lower_chars)
                    string.append(lower_choise)
                else:
                    upper_choise = random.choice(constants.upper_chars)
                    string.append(upper_choise)
            elif level == 3 or level == 4:
                # * uppercase,lowercase and symbols allowed
                if r < 0.2:
                    symbol_choise = random.choice(constants.symbols)
                    string.append(symbol_choise)
                elif r > 0.2 and r < 0.5:
                    lower_choise = random.choice(constants.lower_chars)
                    string.append(lower_choise)
                else:
                    upper_choise = random.choice(constants.upper_chars)
                    string.append(upper_choise)
        return string
    def __get_timestamp(self):
        """Returns current timestamp"""
        ts = str(int(time.time()))
        ts_list = [s for s in ts]
        return ts_list
    def generate_password(self):
        """Generates Password with current timestamp and random ascii digits.
        Length for password (Max 25 length)
        Levels
        1 -> only uppercase charcters
        2 -> uppercase and lowercase charcters
        3 -> uppercase, lowercase charcters and symbols
        4 -> uppercase, lowercase charcters and symbols with current timestamp this level will always unique"""
        if self.__length > 25:
            return ("Exceeded character limit for password",'error')
        if self.__level < 1 or self.__level > 4:
            return ("Invalid level typed.",'error')
        elif self.__level == 4:
            if self.__length < 20:
                return ("Minimum length must 20 for level 4 security",'error')
            else:
                return (''.join(self.__generate_string(self.__level,self.__length) + self.__get_timestamp()),'success')
        else:
            return (''.join(self.__generate_string(self.__level,self.__length)),'success')

