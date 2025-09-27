from abc import ABC, abstractmethod
class UnaClaseAbstracta(ABC):

    def decir_ramon(self):
        print("Ramon")

    
    @abstractmethod
    def decir_algo(self):
        pass