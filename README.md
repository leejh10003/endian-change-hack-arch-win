# py-endian-change
![alt tag](https://api.travis-ci.org/leejh10003/py-endian-change.png?branch=master)
## Why do we need it?
Different kind of computers(in terms of operating system or hardware architecture)use different kind of numeric notation. There are two popular Hex notation which called "Big endian" and "Little Endian". This python application automatically change Hex string to the other endian. You can use it as CLI application or your python application's module.
This application support only python3 for now.
## How to use
First, clone this project to directory where you want it to be located with next command:
```sh
git clone https://github.com/leejh10003/py-endian-change
```
If you want to use it as python application, type next commands:
```sh
cd py-endian-change/
python3 main.py
Input the string you want to change the endian: {Type your HEX string}
```
Then it will print out endian changed string and write it to text file changed.txt in same directory. If you want to use it as your python application, import endianConversion from module endianChange like this:
```python
from endianChange import endianConversion
```
And pass hex string to this function. It will return endian-changed HEX string if you passed it right-formed HEX string. If your string is in wrong form, it will return boolean value False
