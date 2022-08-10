def creation():
    from cgitb import reset
    import sqlite3

    try:
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        # Write a query and execute it with cursor
        listOfTables = cursor.execute("""SELECT tableName FROM sqlite_master WHERE type='table'
        AND tableName='wiki_info'; """).fetchall()

        if listOfTables == []:
            print('Table not found!')
            # if table doesn't exist, create table
            table = """ CREATE TABLE wiki_info (
                    name VARCHAR(255)
                ); """
            cursor.execute(table)
        else:
            print('Table found!')

            queryTableEntries = 'select count(*) from wiki_info;'
            cursor.execute(queryTableEntries)
            result = cursor.fetchall()
            result = str(''.join(map(str, result)))
            result = result.replace('(', '')
            result = int(result.replace(',)', ''))
            print(type(result))
            print()

            if result == 0:
                print('No Data Exists')

            else:
                # if any info exists, delete table and make an exact same new one
                print(result)

                cursor.execute("DROP TABLE wiki_info")

                table = """ CREATE TABLE wiki_info (
                    name VARCHAR(255) NOT NULL
                ); """
                cursor.execute(table)

        # Close the cursor
        cursor.close()

    # Handle errors
    except sqlite3.Error as error:
        print('Error occured - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')


def insertion(name):
    creation()

    from cgitb import reset
    import sqlite3

    try:
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print('DB Init')
        query = """INSERT INTO wiki_info VALUES ()"""
        query = query.replace('()', '('+str(name)+')')
        cursor.execute(query)
        print('Inserted into db')

        # Close the cursor
        cursor.close()

    # Handle errors
    except sqlite3.Error as error:
        print('Error occured - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')


def extraction():
    from cgitb import reset
    import sqlite3
    result = ''

    try:
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        # Write a query and execute it with cursor
        listOfTables = cursor.execute("""SELECT tableName FROM sqlite_master WHERE type='table'
        AND tableName='wiki_info'; """).fetchall()

        if listOfTables == []:
            print('Table not found!')
            # if table doesn't exist, create table
            table = """ CREATE TABLE wiki_info (
                    name VARCHAR(255) NOT NULL
                ); """
            cursor.execute(table)
        else:
            query = """SELECT name FROM wiki_info; """
            cursor.execute(query)
            result = cursor.fetchall()
            print('Extracted from db', result)

        # Close the cursor
        cursor.close()

    # Handle errors
    except sqlite3.Error as error:
        print('Error occured - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

    return result
