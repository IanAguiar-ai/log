# Log
Class to facilitate log creation

# Example:

```
pip install git+https://github.com/IanAguiar-ai/log.git
```

```
from log import Log

log = Log()

log.add("Coment")

sleep(3)
log.add("Sleep", description = "sleep")

log.backup("backup_example")
```
