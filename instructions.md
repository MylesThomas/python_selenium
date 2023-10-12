# Python Selenium

This selenium tutorial is designed for beginners to learn how to use the python selenium module to perform web scraping, web testing and create website bots. Selenium is an automation framework that allows you to interact with websites using something called a web driver.

Common things you can do with Selenium:
- Make bots
- Automated script that tests different aspects of our website
- Basic movements
    - Drag and drop
    - Clicking a button
    - Filling out a form
    - Entering something into a search filed
    - Grabbing data from specific tags
    - Finding an element in the source code
    - Reading the entire page source code
- And more! (Pretty much anything you'd want to do with a webpage)

## 0. Project Setup

Download a text editor, such as VSCode or Sublime Text. (I prefer VSCode)

[Link to Download VSCode](https://code.visualstudio.com/download)

[Link to Download Sublime Text](https://www.sublimetext.com/)

In the VSCode Terminal/Command Prompt, setup the local project directory:

```sh
mkdir python_selenium
cd python_selenium
```

Head to [Github](https://github.com/) and create a new remote repository named `python_selenium`.

Following the creation of your new remote repository, create a new local repository on the command line:

```sh
echo "# python_selenium" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/python_selenium.git
git push -u origin main
```

Save this file as a markdown file `python_selenium/instructions.md`, then open up a new VSCode instance and Open folder > `python_selenium`.

Next, setup a virtual Python environment:

```sh
cd python_selenium
py -m venv env
```

You should now see a folder 'env' with a python.exe program in the /Scripts directory.

Create a .gitignore file for the Python project and save it in the root directory `python_selenium`:

```sh
cd python_selenium
echo > .gitignore
```

Code for .gitignore: [Link to file](https://github.com/github/gitignore/blob/main/Python.gitignore)

Activate the virtual environment in the terminal:

```sh
where python
.\env\Scripts\activate

python.exe -m pip install --upgrade pip
pip list
```

Note: You can leave the virtual environment with this call:

```sh
deactivate
```

Install the necessary packages into your virtual environment:

```sh
pip install selenium
```

Create a requirements.txt file to ensure that you have the necessary dependencies to run this code:

```sh
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

Note:
- 1st line of code: Creates a requirements.txt file
- 2nd line of code: Download the necessary libraries again (Optional)

Create a main Python file, which we will be working from:

```sh
echo > main.py
```

Begin with the necessary imports:

```py
# main.py
import selenium
```

Ensure this runs by heading into the terminal with the virtual environment running:

```sh
python main.py
```

Note: In Sublime, you can run the code with the following command: Ctrl-B

Save these files and update git before beginning the project:

```sh
cd python_selenium

git status
git add .
git commit -m "Completed project setup"
git push -u origin main
git status
git log --oneline
q
```

## 1. Web Scraping, Bots & Testing

### Chrome Web Driver

We will be using Google Chrome for this series, and I highly recommend that you do as well!

Once you have Google Chrome downloaded, head to [this site](https://sites.google.com/chromium.org/driver/downloads) to download the the ChromeDriver binary for your platform.
- Upon landing on that page, I was prompted to navigate to [this page](https://googlechromelabs.github.io/chrome-for-testing/#stable) for the more recent versions of Google Chrome.

I am running on a 64-bit operating system, which has the [following link to its binary](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/118.0.5993.70/win64/chromedriver-win64.zip).
- Make sure that you get the URL for 'chromedriver' and not 'chrome'!

Note: If you do not know if you are running on a 32-bit of 64-bit Windows, follow these instructions:
1. Click Start, type system in the search box, and, under Control Panel, click System.
2. Under System, look at the System type entry. It will say either 32-bit Operating System or 64-bit Operating System.

Note: If you do not know your version of Google Chrome, follow these instructions:
1. Open Chrome
2. Click the three-dot icon in the top right corner of the browser window
3. Click or hover over Help
4. Click About Google Chrome
5. Look for the Version number just under the Google Chrome heading and icon
- I am currently using the most up to date version (as of 10/12/2023): Version 118.0.5993.71 (Official Build) (640bit)

Once you have downloaded the .zip folder, we need to extract that and place it on a specific location on our operating system (A location that is easier to access).
- Find the chromedrive.exe Application
    - After extracting, here is the path: C:\Users\Myles\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe
- Move chromedriver.exe to C:\Program Files (x86)
    - New path: C:\Program Files (x86)\chromedriver.exe

Note: You do not need to place it here, but just make sure you know where you are placing it, so we can reference that file location going forward.

Go ahead and add a PATH variable to your Python file:

```py
# main.py
import selenium
PATH = "C:\Program Files (x86)\chromedriver.exe"
```

Now that we have that done, we are ready to begin working with Selenium!

### Working with Selenium

The first thing we need to do is change our code so that we can actually open up a webpage with Selenium:

```py
# main.py
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
```

What is going on here:
- We imported the webdriver from selenium
    - The webdriver drives all of our actions
        - It links up the browser to drive these actions
- We also picked the browser that we will be using
    - Google Chrome, of course

Now that we have all of that setup, let's look at some common commands that we can do with our driver!

I will start by using my own website, so that we don't run any bots on the wrong website. (ha)

```py
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://mylesthomas.io/")
print(driver.title) # print the title of the website
driver.close()  # closes the current tab (if you have 1 tab, which we do, it closes the browser)
# driver.quit()   # closes the browser
```

## 2. Locating Elements From HTML

## 3. Page Navigating and Clicking Elements

## 4. ActionChains & Automating Cookie Clicker

## 5. UnitTest Framework

---

### References

References:
- 