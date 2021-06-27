#!/usr/bin/python
from time import sleep, strftime
from os import system, name
from sys import argv

# Try to import modules that are not pre-installed
try:
    if not ('-c' in argv):
        from colorama import Fore, Back, Style
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.opera import OperaDriverManager

except ModuleNotFoundError:
    if (name == 'nt'):
        system('cls')
    else:
        system('clear')
    print("" if ('-c' in argv) else '\033[32m' + '\033[01m')
    print("  ____                 __          __           _     _______        _")
    print(" / __ \                \ \        / /          | |   |__   __|      | |")
    print("| |  | |_ __   ___ _____\ \  /\  / /__  _ __ __| |______| | _____  _| |_ ___ _ __")
    print("| |  | | '_ \ / _ \______\ \/  \/ / _ \| '__/ _` |______| |/ _ \ \/ / __/ _ \ '__|")
    print("| |__| | | | |  __/       \  /\  / (_) | | | (_| |      | |  __/>  <| ||  __/ |")
    print(" \____/|_| |_|\___|        \/  \/ \___/|_|  \__,_|      |_|\___/_/\_\\\__\___|_|")
    print("" if ('-c' in argv) else '\033[34m')
    print("Author: Jeník")
    print("Instagram: @JanSvobodaJenik")
    print("Github: @JanSvobodaJenik")
    print("" if ('-c' in argv) else '\033[0m')
    print("" if ('-c' in argv) else '\033[31m')
    print("Error encountered. Try this to fix it:")
    print("Install Colorama, Selenium and WebDriver-Manager by running 'pip install colorama selenium webdriver-manager'." if ('-c' in argv) else '\033[37m' + "Install Colorama, Selenium and WebDriver-Manager by running 'pip install colorama selenium webdriver-manager'.")
    print("" if ('-c' in argv) else '\033[0m')
    exit(1)

# Initiate Colorama and define args and opts
opts = [opt for opt in argv[1:] if opt.startswith("-")]
args = [arg for arg in argv[1:] if not arg.startswith("-")]

# Display head
def head():
    if (name == 'nt'):
        system('cls')
    else:
        system('clear')
    if ('-c' in opts):
        print("")
    else:
        print(Fore.GREEN + Style.BRIGHT)
    print("  ____                 __          __           _     _______        _")
    print(" / __ \                \ \        / /          | |   |__   __|      | |")
    print("| |  | |_ __   ___ _____\ \  /\  / /__  _ __ __| |______| | _____  _| |_ ___ _ __")
    print("| |  | | '_ \ / _ \______\ \/  \/ / _ \| '__/ _` |______| |/ _ \ \/ / __/ _ \ '__|")
    print("| |__| | | | |  __/       \  /\  / (_) | | | (_| |      | |  __/>  <| ||  __/ |")
    print(" \____/|_| |_|\___|        \/  \/ \___/|_|  \__,_|      |_|\___/_/\_\\\__\___|_|")
    if ('-c' in opts):
        print("")
    else:
        print(Fore.BLUE)
    print("Author: Jeník")
    print("Instagram: @JanSvobodaJenik")
    print("Github: @JanSvobodaJenik")
    if ('-c' in opts):
        print("")
    else:
        print(Fore.WHITE + Style.NORMAL)
    print("")

# Check for valid usage
head()
print("Checking for valid input, please wait... ")

# Check for arguments
try:
    test = argv[1]
    test = argv[2]
    test = argv[3]
    test = argv[4]
except IndexError:
    head()
    print("This is a script that can send any big text file word by word on WhatsApp insanely fast.")
    print("")
    print("Usage:")
    print("")
    print("python " + argv[0] + " [chat] [file] [delay] [browser] {options}")
    print("")
    print("chat - the exact title of the chat as it appears on your phone")
    print("file - path to the text file to send word by word")
    print("delay - delay between each word in seconds")
    print("browser - 'edge', 'chrome', 'firefox', or 'opera'")
    print("")
    print("Options:")
    print("")
    print("OPTION   DESCRIPTION")
    print("-c       turn off color")
    print("-s       do not display any output")
    print("")
    exit(0)

# Check for options in arguments
for i in argv[1:5]:
    if (i in opts):
        head()
        print("Incorrect usage. Arguments go before options." if ('-c' in opts) else Fore.RED + "Incorrect usage. Arguments go before options.")
        print("Run the script with no arguments or options to display usage information." if ('-c' in opts) else Fore.WHITE + "Run the script with no arguments or options to display usage information.")
        print("" if ('-c' in opts) else Style.RESET_ALL)
        exit(1)

# Check for arguments in options
for i in argv[5:]:
    if (i in args):
        head()
        print("Incorrect usage. Arguments go before options." if ('-c' in opts) else Fore.RED + "Incorrect usage. Arguments go before options.")
        print("Run the script with no arguments or options to display usage information." if ('-c' in opts) else Fore.WHITE + "Run the script with no arguments or options to display usage information.")
        print("" if ('-c' in opts) else Style.RESET_ALL)
        exit(1)

# Check if file exists
try:
    open(argv[2])
except IOError:
    head()
    print("Error encountered. File dowsn't exist." if ('-c' in opts) else Fore.RED + "Error encountered. File dowsn't exist.")
    print("Run the script with no arguments or options to display usage information." if ('-c' in opts) else Fore.WHITE + "Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(1)

# Check if delay is a number
try:
    float(argv[3])
except ValueError:
    head()
    print("Error encountered. Delay is not a valid number." if ('-c' in opts) else Fore.RED + "Error encountered. Delay is not a valid number.")
    print("Run the script with no arguments or options to display usage information." if ('-c' in opts) else Fore.WHITE + "Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(1)

# Check if browser is supported
if not (argv[4] == 'edge' or argv[4] == 'chrome' or argv[4] == 'firefox' or argv[4] == 'opera'):
    head()
    print("Error encountered. Browser is not supported." if ('-c' in opts) else Fore.RED + "Error encountered. Browser is not supported.")
    print("Run the script with no arguments or options to display usage information." if ('-c' in opts) else Fore.WHITE + "Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(1)

# Create a list of words from the text file
head()
print("Processing your file, please wait... ")
file1 = open(argv[2])
file2 = file1.read()
file3 = file2.replace('\r', '').replace('\n', '').replace('\r\n', '')
wordlist = file3.split()

# Show disclaimer
head()
print("This script is now going to open your browser.")
print("The browser must remain in foreground for the whole time.")
print("Scan the QR code on your screen with the WhatsApp app on your phone.")
print("Just click on the three dots in the top right corner and then select 'WhatsApp Web'.")
print("After that, the chat you chose should open and start sending the messages.")
print("If your chat doesn't open, try checking if you entered the title correctly.")
print("To stop this script, simply close the browser.")
print("The browser should close automatically after sending all the messages.")
print("This script is made strictly for educational purposes only.")
print("Don't use this script with harmful intentions.")
print("Don't share this script without a proper credit.")
print("Now, enjoy.")
input("Press enter to continue. ")

# Start browser
if not ('-s' in opts):
    head()
elif (name == 'nt'):
    system('cls')
else:
    system('clear')
if argv[4] == 'edge':
    driver = webdriver.EdgeDriver(EdgeChromiumDriverManager().install())
elif argv[4] == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif argv[4] == 'firefox':
    driver = webdriver.Firefox(FirefoxDriverManager().install())
elif argv[4] == 'opera':
    driver = webdriver.Opera(OperaDriverManager().install())

# Load WhatsApp, wait for code scan and click on chat
head()
driver.get('https://web.whatsapp.com/')
WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title,' + '"' + argv[1] + '"' + ')]'))).click()

# Start sending the messages
if not ('-s' in opts):
    head()
elif (name == 'nt'):
    system('cls')
else:
    system('clear')
for i in range(len(wordlist)):
    try:
        driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0].send_keys(wordlist[i])
        driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0].click()
        if not ('-s' in opts):
            print("Just sent this word: " + wordlist[i])
    except:
        driver.close()
        if not ('-s' in opts):
            print("")
            print("Closed before completion.")
            print("" if ('-c' in opts) else Style.RESET_ALL)
        exit(0)
    sleep(float(argv[3]))

# Exit the script
driver.close()
if not ('-s' in opts):
    print("")
    print("Completed.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
exit(0)
