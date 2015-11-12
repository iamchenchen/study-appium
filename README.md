# study-appium
My study notes for appium

## Installation

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
