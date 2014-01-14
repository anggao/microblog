To setup development environment run`bash -x setup.sh` first.

Know issues:

1. change `lib/python2.7/site-packages/migrate/changeset/ansisql.py` line 10
```python
#from sqlalchemy.schema import SchemaVisitor
from sqlalchemy.sql.base import SchemaVisitor
```

