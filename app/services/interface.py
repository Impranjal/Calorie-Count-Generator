from abc import ABC,abstractmethod
from typing import Optional


class AuthInterface(ABC):
    @abstractmethod
    def register(self,*args,**kwargs):
        pass

    @abstractmethod
    def login(self,*args,**kwargs):
        pass
