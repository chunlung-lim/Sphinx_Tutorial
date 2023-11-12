from typing import Any


class SphinxDB:
    '''
    SphinxDB Class responsible for connecting to all the database with related to Sphinx documentation.
    '''

    def __init__(self, serverInfo) -> None:
        self.serverInfo = serverInfo

    def connectToDB(self, serverInfo) -> True:
        '''
        :func: connectToDB is used to connect to database.
        :param serverInfo: str
        :return: Bool
        '''
        print("Connected to database")