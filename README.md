🌟 Full Guide: Fun Colored Python Password Generator

This guide works for Windows users.

1️⃣ Install Python

Go to Python official download page
.

Download the latest stable version for Windows.

During installation, check the box:

Add Python to PATH


Click Install Now and wait until it finishes.

Verify installation: Open PowerShell and type:

python --version


You should see something like:

Python 3.8.10

2️⃣ Install Colorama Library

Colorama is used to print colored text in the terminal.

Open PowerShell.

Type:

pip install colorama


You should see a success message when installed.

3️⃣ Create the Python Script

Open Notepad.

Copy and paste the following code:

import random
import string
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Print primary text in purple and password in green
print(Fore.MAGENTA + "Your random password is: " + Fore.GREEN + generate_password())

4️⃣ Save the File

Click File → Save As

Navigate to Documents (or Desktop if you prefer)

File name: password_generator.py

Save as type: All Files

Click Save

5️⃣ Run the Script

Open PowerShell.

Navigate to the folder where you saved the script. For Documents:

cd C:\Users\YourUsername\Documents


(replace YourUsername with your Windows username)

Run the script:

python password_generator.py

6️⃣ Result

You’ll see output like this in your terminal:

“Your random password is:” → purple

The generated password → green

Example:

Your random password is: 7@kF!b2Pq$9

Optional Fun Tweaks

Change password length:

generate_password(16)   # 16-character password


Generate multiple passwords:

for _ in range(5):
    print(Fore.MAGENTA + "Password:" + Fore.GREEN + generate_password())


Make it interactive with Tkinter (button click to generate).
