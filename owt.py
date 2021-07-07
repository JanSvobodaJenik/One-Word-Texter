#!/usr/bin/python
from time import sleep, strftime
from os import system, name
from sys import argv

# Import modules that are not pre-installed
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
except:
    if not ('-s' in argv):
        system('cls' if (name == 'nt') else 'clear')
        print("  ____                 __          __           _     _______        _")
        print(" / __ \                \ \        / /          | |   |__   __|      | |")
        print("| |  | |_ __   ___ _____\ \  /\  / /__  _ __ __| |______| | _____  _| |_ ___ _ __")
        print("| |  | | '_ \ / _ \______\ \/  \/ / _ \| '__/ _` |______| |/ _ \ \/ / __/ _ \ '__|")
        print("| |__| | | | |  __/       \  /\  / (_) | | | (_| |      | |  __/>  <| ||  __/ |")
        print(" \____/|_| |_|\___|        \/  \/ \___/|_|  \__,_|      |_|\___/_/\_\\\__\___|_|")
        print("")
        print("Author: Jeník")
        print("Instagram: @JanSvobodaJenik")
        print("Github: @JanSvobodaJenik")
        print("")
        print("")
        print("It seems that either Colorama, Selenium, and/or WebDriver-Manager is not installed.")
        print("But don't worry, I will install them for you.")
        print("")
        input("Press enter to continue. ")
        print("")
        print("Installing Colorama...")
        system('pip install colorama')
        print("")
        print("Installing Selenium...")
        system('pip install selenium')
        print("")
        print("Installing WebDriver-Manager...")
        system('pip install webdriver-manager')
        print("")
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
        except:
            print("It seems that I couldn't install some of the libraries.")
            print("Check the output for more detail.")
            print("")
            exit(0)

# Define args and opts
opts = [opt for opt in argv[1:] if opt.startswith("-")]
args = [arg for arg in argv[1:] if not arg.startswith("-")]

# Show head
def head():
    system('cls' if (name == 'nt') else 'clear')
    print("" if ('-c' in opts) else Fore.GREEN + Style.BRIGHT, end="")
    print("  ____                 __          __           _     _______        _")
    print(" / __ \                \ \        / /          | |   |__   __|      | |")
    print("| |  | |_ __   ___ _____\ \  /\  / /__  _ __ __| |______| | _____  _| |_ ___ _ __")
    print("| |  | | '_ \ / _ \______\ \/  \/ / _ \| '__/ _` |______| |/ _ \ \/ / __/ _ \ '__|")
    print("| |__| | | | |  __/       \  /\  / (_) | | | (_| |      | |  __/>  <| ||  __/ |")
    print(" \____/|_| |_|\___|        \/  \/ \___/|_|  \__,_|      |_|\___/_/\_\\\__\___|_|")
    print("" if ('-c' in opts) else Fore.BLUE  + Style.BRIGHT)
    print("Author: Jeník")
    print("Instagram: @JanSvobodaJenik")
    print("Github: @JanSvobodaJenik")
    print("" if ('-c' in opts) else Fore.WHITE + Style.NORMAL)
    print("")

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
    print("delay - delay between each word in seconds can be either an interger or a float number")
    print("browser - 'edge', 'chrome', 'firefox', or 'opera'")
    print("")
    print("Options:")
    print("")
    print("OPTION   DESCRIPTION")
    print("-s       skip automatic requirement installation")
    print("-c       turn off color")
    print("-r       don't remove EOL characters")
    print("")
    exit(0)

# Verify correct usage
head()
print("Checking for correct usage, please wait... ")

# Check for options in arguments
for i in argv[1:5]:
    if (i in opts):
        head()
        print("" if ('-c' in opts) else Fore.RED, end="")
        print("Incorrect usage. Arguments go before options.")
        print("" if ('-c' in opts) else Fore.WHITE, end="")
        print("Run the script with no arguments or options to display usage information.")
        print("" if ('-c' in opts) else Style.RESET_ALL)
        exit(1)

# Check for arguments in options
for i in argv[5:]:
    if (i in args):
        head()
        print("" if ('-c' in opts) else Fore.RED, end="")
        print("Incorrect usage. Arguments go before options.")
        print("" if ('-c' in opts) else Fore.WHITE, end="")
        print("Run the script with no arguments or options to display usage information.")
        print("" if ('-c' in opts) else Style.RESET_ALL)
        exit(2)

# Check if file exists
try:
    open(argv[2])
except:
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. File dowsn't exist.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(3)

# Check if delay is a number
try:
    float(argv[3])
except:
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. Delay is not a valid number.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(4)

# Check if browser is supported
if not argv[4].lower() in ('edge','chrome','firefox','opera'):
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. Browser is not supported.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(5)

# Create a list of words from the text file
head()
print("Processing your file, please wait... ")

# Open file
try:
    file1 = open(argv[2])
except:
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. Couldn't open file.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(6)

# Read file
try:
    file2 = file1.read()
except:
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. Couldn't read file.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(7)

# Remove EOL characters
try:
    if ('-r' in opts):
        file3 = file2
    else:
        file3 = file2.replace('\r', '').replace('\n', '').replace('\r\n', '')
except:
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. Couldn't remove EOL characters.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(8)

# Split to words
try:
    wordlist = file3.split()
except:
    head()
    print("" if ('-c' in opts) else Fore.RED, end="")
    print("Error encountered. Couldn't split file into words.")
    print("" if ('-c' in opts) else Fore.WHITE, end="")
    print("Run the script with no arguments or options to display usage information.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(9)

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
print("")
input("Press enter to continue. ")

# Install WebDrivers
head()
print("Installing WebDrivers, please wait... ")
if argv[4].lower() == 'edge':
    driver = webdriver.EdgeDriver(EdgeChromiumDriverManager().install())
elif argv[4].lower() == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif argv[4].lower() == 'firefox':
    driver = webdriver.Firefox(FirefoxDriverManager().install())
elif argv[4].lower() == 'opera':
    driver = webdriver.Opera(OperaDriverManager().install())

# Load WhatsApp, wait for code scan and click on chat
head()
try:
    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title,' + '"' + argv[1] + '"' + ')]'))).click()
except:
    head()
    print("Closed before completion.")
    print("" if ('-c' in opts) else Style.RESET_ALL)
    exit(0)

# Send the messages
head()
for i in range(len(wordlist)):
    try:
        driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0].send_keys(wordlist[i])
        driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0].click()
        print("Just sent this word: " + wordlist[i])
    except:
        driver.close()
        print("")
        print("Closed before completion.")
        print("" if ('-c' in opts) else Style.RESET_ALL)
        exit(0)
    sleep(float(argv[3]))

# Finish
driver.close()
print("")
print("Completed.")
print("" if ('-c' in opts) else Style.RESET_ALL)
exit(0)
