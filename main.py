import logging
import generatepassword

PasswordGenerator = generatepassword.GeneratePassword


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="./log/generator.log",
                    level=logging.DEBUG, format= LOG_FORMAT,)

logger = logging.getLogger()

generator = PasswordGenerator(4,14)

password = generator.generate_password()

if password[1] == 'error':
  logger.error(password[0])
  print(password[1]," : ",password[0])
else:
  logger.info("Generated: " + password[0])
  print(password[1]," : ",password[0])
