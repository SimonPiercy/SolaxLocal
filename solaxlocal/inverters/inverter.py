from solaxlocal.models.data import DataModel
from solaxlocal.models.information import InformationModel
from solaxlocal.models.response import ResponseModel


class Inverter:
    def __init__(self, ipaddress: str, pwd: str | None = None) -> None:
        self.ipaddress: str = ipaddress
        self.pwd: str | None = pwd
        self.url: str = f'http://{self.ipaddress}'
        self.params: str = ''
        self.response_model: ResponseModel | None = None
        self.information_model: InformationModel | None = None
        self.data_model: DataModel | None = None
