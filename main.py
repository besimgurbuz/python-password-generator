import logging
import argparse
import pyperclip
import generatepassword

#command line arguments so that you can now generate passwords without touching
#the python code itself.
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--security", help="Set the security level", type=int, default=1)
parser.add_argument("-l", "--length", help="Set the password length", type=int, default=12)
parser.add_argument("-p", "--private", help="Hide the password in the console", action='store_true')
parser.add_argument("-nl", "--nolog", help="Prevent the logging of the password", action='store_true')
args = parser.parse_args()


PasswordGenerator = generatepassword.GeneratePassword


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="./log/generator.log",
                    level=logging.DEBUG, format= LOG_FORMAT,)

logger = logging.getLogger()

generator = PasswordGenerator(args.security, args.length)

password = generator.generate_password()

#Copies the resulting password to the clipboard for you.
pyperclip.copy(password[0])


if args.nolog == False:
  if password[1] == 'error':
    logger.error(password[0])
    print(password[1]," : ",password[0])
  else:
    logger.info("Generated: " + password[0])
  
if args.private == False:
  print(password[1]," : ",password[0])
else:
  print(password[1]," : ", "************")
