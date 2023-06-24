import os

from solaxlocal.models.data import DataModel
from solaxlocal.models.information import InformationModel
from solaxlocal.models.response import ResponseModel


class Inverter:
    def __init__(self, ip_address: str | None = None, password: str | None = None) -> None:
        self.ip_address: str = ip_address or os.environ.get('SOLAX_LOCAL_IP_ADDRESS')
        self.password: str | None = password or os.environ.get('SOLAX_LOCAL_PASSWORD')

        if self.ip_address is None:
            raise ValueError(f"Please supply an IP address "
                             "or set the 'SOLAX_LOCAL_IP_ADDRESS' environment variable")

        self.url: str = f'http://{self.ip_address}'
        self.params: str = ''
        self.response_model: ResponseModel | None = None
        self.information_model: InformationModel | None = None
        self.data_model: DataModel | None = None
