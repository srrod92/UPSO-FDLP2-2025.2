from abc import ABC, abstractmethod

class IVolar(ABC):

    @abstractmethod
    def despegar():
        pass

    @abstractmethod
    def volar():
        pass

    @abstractmethod
    def aterrizar():
        pass