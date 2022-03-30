import mysql.connector

mydb = mysql.connector.connect(
    host="sh-cynosdbmysql-grp-dhfshspi.sql.tencentcdb.com",
    port=24839,
    user="cloudiful",
    password="T7:5CWr.jrFK-kj",
    database="raspberry"
)

cursor = mydb.cursor()


def fetch_all(table):
    """
    print all the data
    :param table: table name (int)
    :return: none
    """
    sql = "SELECT * FROM " + table
    cursor.execute(sql)

    result = cursor.fetchall()

    print(result)


def insert(table, deviceID, name, online):
    """

    :param table: table name (string)
    :param deviceID: device unique ID (string)
    :param name: device name (int)
    :param online: 0 for offline, 1 for online (int)
    :return: none
    """
    sql = "INSERT INTO " + table + " (deviceID, name, online) VALUES (%s, %s, %s)"
    val = (deviceID, name, online)
    cursor.execute(sql, val)

    mydb.commit()


def update(table, deviceID, online):
    """

    :param table: table name (string)
    :param deviceID: device ID (int)
    :param online: 0 for offline, 1 for online (int)
    :return: none

    """
    sql = "UPDATE " + table + " SET online = " + str(online) + " WHERE deviceID = " + str(deviceID)
    cursor.execute(sql)

    mydb.commit()


fetch_all("status")
update("status", 0, 1)
fetch_all("status")
