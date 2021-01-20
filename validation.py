import psycopg2
import login


def conn():
    log = None
    try:
        con = psycopg2.connect(dbname='postgres', password='admin', user='postgres', host='localhost')
        cur = con.cursor()
        log = True
        return log
    except:
        print('cos nie tak')
        log = False
        return log


if conn():
    login()
else:
    print('nie zalogujesz się')