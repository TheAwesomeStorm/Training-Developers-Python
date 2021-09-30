from src import environment


class Configurations:

    """

    Class that defines the configuration for the program

    """

    __instance = None

    def __init__(self, debug: bool = environment.IS_DEBUG):

        self.bottle_host = environment.HOST

        if debug:

            self.bottle_port = environment.DEBUG_PORT

            self.json_indent = 4

        else:

            self.bottle_port = environment.OPERATION_PORT

            self.json_indent = None

    @classmethod
    def singleton(cls):

        if cls.__instance is None:

            cls.__instance = cls()

        return cls.__instance