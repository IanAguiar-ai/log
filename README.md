# Log
Class to facilitate log creation

## To install:

```
pip install git+https://github.com/IanAguiar-ai/log.git
```

## Example:

```
from log import Log
from time import sleep

my_log = Log()
my_log.add("Start Ok")

sleep(3)

my_log.add("Wait 3 seconds ok")

print(my_log)

log = my_log.read()
print(log)
```
