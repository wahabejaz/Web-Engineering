import os

# Use PyMySQL as the MySQL client backend on Windows and other environments.
# If you are using MySQL and Django's mysql backend,
# PyMySQL provides a pure-Python MySQLdb replacement.
if os.environ.get('DJANGO_DB_ENGINE') == 'django.db.backends.mysql':
    import pymysql

    pymysql.install_as_MySQLdb()
