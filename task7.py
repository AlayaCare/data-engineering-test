
import mysql.connector as mariadb
import unittest


class Db_connector:
    """
    Class that takes username and password to initialize and has connection to mariadb database in docker as property
    """

    def __init__(self, uname, pword):
        try:
            # hard coded host, port values, ideally would want those explicitly
            # stated in the docker file so they could be read. The Database name is
            # hard coded too, could get that from the sql file.
            self.mariadb_connection = mariadb.connect(host='172.18.0.2', port='3306', user=str(
                uname), password=str(pword), database='test')
        except:
            print("Error: Invalid username, password combination or connection issue")


class TestDb_connector(unittest.TestCase):
    """
    Test to make sure that Db_connector is able to connect to the database by checking the type of
    Db_connector.mariadb_connection
    """

    def test_init(self):
        # using the defaults from the docker-compose file
        test_connector = Db_connector('root', 'root')
        self.assertTrue(type(test_connector.mariadb_connection)
                        == mariadb.connection_cext.CMySQLConnection)


if __name__ == '__main__':
    unittest.main()
