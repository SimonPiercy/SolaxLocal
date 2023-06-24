from . import *
from .models.information import InformationModel
from .models.response import ResponseModel
from requests import Response
from solaxlocal.utils.units import Unit
import requests
import time


class SolaxLocal:
    def __init__(self, inverter: Inverter) -> None:
        self.inverter: Inverter = inverter
        self._processed: bool = False
        self._solax_information: InformationModel | None = None
        self._data: ResponseModel | None = None

    def refresh(self) -> Response:
        for _ in range(10):
            try:
                response: Response = requests.post(self.inverter.url, data=self.inverter.params)
                break
            except requests.exceptions.ConnectionError as e:
                logging.info('Sleeping for 3 seconds', exc_info=e)
                time.sleep(2)
        else:
            raise ConnectionError(f"Unable to connect to inverter at {self.inverter.url}")

        solax_data: ResponseModel = self.inverter.response_model.model_validate(response.json())
        info_fields = dict(zip(self.inverter.information_model.model_fields, solax_data.information))
        self._solax_information = self.inverter.information_model.model_validate(info_fields)
        data_fields = dict(zip(self.inverter.data_model.model_fields, solax_data.data))
        self._data = self.inverter.data_model.model_validate(data_fields)
        self._processed = True
        return response

    def check_processed(self) -> None:
        if self._processed is False:
            self.refresh()

    @property
    def solax_information(self) -> InformationModel:
        self.check_processed()
        return self._solax_information

    @property
    def data(self) -> ResponseModel:
        self.check_processed()
        return self._data

    def __iter__(self) -> tuple[str, Unit]:
        self.check_processed()

        for sensor, value in self.data.model_dump().items():
            if not isinstance(value, Unit):
                continue

            yield sensor, value
