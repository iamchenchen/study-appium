# study-appium
My study notes for appium

## Installation
Since we are using appium python, we need to install pip
```shell
sudo easy_install pip
```
Install from [PyPi](https://pypi.python.org/pypi), as ['Appium-Python-Client'](https://pypi.python.org/pypi/Appium-Python-Client).
```shell
pip install Appium-Python-Client
```

## How to run appium?
I like to open two terminal, 1 for Appium, and 1 for running appium

/Users/chenchenzheng/github/appium/python-client 
![alt tag](https://raw.github.com/iamchenchen/study-appium/master/screenshots/howtouse1.png)

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


## Notes
* Read more information here: https://github.com/appium/python-client
* if encounter error: Brew doctor says: “Warning: /usr/local/include isn't writable.” 
     * user this: 
     ```shell
     sudo chown -R `whoami` /usr/local/
     ```
