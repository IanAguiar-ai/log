# Log
Class to facilitate log creation

# Example:

```
pip install git+https://github.com/NOME_USUARIO/NOME_REPOSITORIO.git@COMMIT_HASH

```

```
from log import Log

log = Log()

log.add("Coment")

sleep(3)
log.add("Sleep", description = "sleep")

log.backup("backup_example")
```