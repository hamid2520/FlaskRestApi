#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

# mssql = {'host': 'dbhost',
#          'user': 'dbuser',
#          'passwd': 'dbPwd',
#          'db': 'db'}

postgresql = {'host': 'localhost',
              'user': 'jigar',
              'passwd': 'Hamid_2520',
              'db': 'sport'}


# mssqlConfig = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+10.0".format(mssql['user'], mssql['passwd'], mssql['host'], mssql['db'])
postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

