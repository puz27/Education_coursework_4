from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        """Return request"""
        pass

    @staticmethod
    def get_connector(self):
        """Return instance of class Connector"""
        pass


class HH(Engine):
    """Class for work with HeadHunter"""
    def get_request(self):
        pass


class SJ(Engine):
    """Class for work with SuperJob """
    def get_request(self):
        pass
