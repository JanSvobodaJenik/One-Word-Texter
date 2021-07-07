# One-Word-Texter

![Screenshot](https://raw.githubusercontent.com/JanSvobodaJenik/One-Word-Texter/main/Screenshots/1.png)

This is a script that can send any big text file word by word on WhatsApp insanely fast.

# Installation

First install Python 3 from the Microsoft Store (Windows) or with your preferred package manager (Linux),

it should come pre-installed with MacOS, then download [owt.py](https://github.com/JanSvobodaJenik/One-Word-Texter/releases/download/1.1/owt.py).

# Usage

![Screenshot](https://raw.githubusercontent.com/JanSvobodaJenik/One-Word-Texter/main/Screenshots/2.png)

Run the script by typing `python owt.py` and let the script install all the requirements.

Upon running the script, you'll be asked to run the command again along with some arguments.

After doing that, a browser window should pop up, scan the QR code with the WhatsApp app on your phone.

The script should then do all the work for you, just keep the browser in foreground and don't close the terminal.

![Screenshot](https://raw.githubusercontent.com/JanSvobodaJenik/One-Word-Texter/main/Screenshots/3.png)

You can stop the script at any time by just closing the browser.

It does all this with the help of webdrivers and the Selenium webdriver.

# Some basic troubleshooting

### Python errors

Check that you are using the latest version of Python by running `python --version`.

Try running it with `python3` instead.

### Browser is not opening

Check that you have the browser installed on your PC.

Check if the version of your browser is compatible with the webdrivers.

Try using a different browser.

### The chat is not opening

Check that you entered the title correctly, capital letters matter.

If there are spaces in the name, put it in between two apostrophes (') or quotation marks (").

### Can't install requirements

Try to install them manually.

Run the script with `-s` at the end every time.

### Colors don't work

Try using a different terminal.

Run the script with `-c` at the end every time.

# Disclaimer

This script is made strictly for educational purposes only.

Don't use this script with harmful intentions.

Don't share this script without a proper credit.
