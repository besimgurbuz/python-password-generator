## Password Generator with logging

Generates password with current timestamp and random ascii digits.<br>
Length for password (Default Max 25 length)<br>
Levels<br>
1 - only uppercase charcters<br>
2 - uppercase and lowercase charcters<br>
3 - uppercase, lowercase charcters and symbols<br>
4 - uppercase, lowercase charcters and symbols with current timestamp this level will always unique<br>


## Use

### Required Libs
pip install pyperclip <br>

### Flags
-nl / --nolog : Will not log the generated passwords in the log file.<br>
-p / --private : Will display stars instead of the password in the console.<br>
-s / --security : will set the security level.<br>
-l / --length : will set the length of the password.<br>


### Example use
main.py --nolog --private<br>
main.py -l=16 -s=14 -p
