import mysql.connector

mydb = mysql.connector.connect(
    host="your servername",
    port=your port,
    user="your username",
    password="your password",
    database="your database"
)

cursor = mydb.cursor()


def fetch_all(table):
    """
    print all the data
    :param table: table name (int)
    :return: fetched data
    """
    sql = "SELECT * FROM " + table
    cursor.execute(sql)

    result = cursor.fetchall()

    return result


def insert(table, deviceID, name, online=0, command="None", result=0):
    """

    :param result: 0 for no command, 1 for success (int)
    :param command: command to do (string)
    :param table: table name (string)
    :param deviceID: device unique ID (string)
    :param name: device name (int)
    :param online: 0 for offline, 1 for online (int)
    :return: none
    """
    sql = "INSERT INTO " + table + " (deviceID, name, online, command, result) VALUES (%s, %s, %s, %s, %s)"
    val = (deviceID, name, online, command, result)
    cursor.execute(sql, val)

    mydb.commit()


def updateOnline(table, deviceID, online):
    """

    :param table: table name (string)
    :param deviceID: device ID (int)
    :param online: 0 for offline, 1 for online (int)
    :return: none

    """
    sql = "UPDATE " + table + " SET online = " + str(online) + " WHERE deviceID = " + str(deviceID)
    cursor.execute(sql)

    mydb.commit()


def updateCommand(table, deviceID, command):
    """

    :param table: table name (string)
    :param deviceID: device ID (int)
    :param command: command to do (string)
    :return: none

    """
    sql = "UPDATE " + table + " SET command = '" + str(command) + "' WHERE deviceID = " + str(deviceID)
    cursor.execute(sql)

    mydb.commit()


def updateResult(table, deviceID, result):
    """

    :param table: table name (string)
    :param deviceID: device ID (int)
    :param result: 0 for no command, 1 for success (int)
    :return: none

    """
    sql = "UPDATE " + table + " SET command = " + str(result) + " WHERE deviceID = " + str(deviceID)
    cursor.execute(sql)

    mydb.commit()
