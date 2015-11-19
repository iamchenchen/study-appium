# study-appium
My study notes for appium

## Installation
Since we are using appium python, we need to install pip
```shell
sudo easy_install pip
```
Install from [PyPi](https://pypi.python.org/pypi), as ['Appium-Python-Client'](https://pypi.python.org/pypi/Appium-Python-Client).
```shell
sudo chown -R `whoami` /Library/Python/2.7/
pip install Appium-Python-Client
```
Install xcode command line tool
1. open xcode
2. click on xcode on the top left corner navigation bar->Open Developer Tool -> More Developer Tool
3. Find correct commend-line tool
4. download and install

Install brew
```shell
ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
```

Install Ideviceinstaller
```shell
brew install ideviceinstaller
```

## How to run appium?
I like to open two terminal, 1 for Appium, and 1 for running appium

/Users/chenchenzheng/github/appium/python-client 
![alt tag](https://raw.github.com/iamchenchen/study-appium/master/screenshots/howtouse1.png)

## How to build a debug version of app?

user commandline like this under your app directory
```shell
xcodebuild -workspace whistler.xcworkspace -scheme whistler -configuration Debug -sdk iphonesimulator9.1
```
## File Notes
# desired_capabilities.py
This is device configuration file, you need to choose the correct device.  In my example, I'm using a actual device.
You can find more definition here: http://appium.io/slate/en/master/?python#appium-server-capabilities
```python
def get_desired_capabilities(app):
    desired_caps = {
        'deviceName': 'iPhone 6s',
        'platformName': 'iOS',
            'platformVersion': '9.1',
        'udid': 'bc41d7bbe35223441656630117358998015b5c8f',
        # 'app' : '/Users/chenchenzheng/Desktop/whistler.ipa',
        'app': PATH('../../apps/' + app),
        'bundleId':'com.ar-devices.whistler'
    }

    return desired_caps
```

## Tests
1. verify walkthrough
2. verify facebook login
3. verify digits login
4. verify if there are five tabs
5. verify logout will bring app to walkthrough

## Notes
* Read more information here: https://github.com/appium/python-client
* if encounter error: Brew doctor says: “Warning: /usr/local/include isn't writable.” 
     * user this: 
        ```shell
        sudo chown -R `whoami` /usr/local/
        ```
