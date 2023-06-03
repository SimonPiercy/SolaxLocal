import logging
import requests
import time
from solaxlocal.inverters import Inverter


class SolaxLocal:
    def __init__(self, inverter: Inverter) -> None:
        self.inverter: Inverter = inverter

        for _ in range(10):
            try:
                response = requests.post(self.inverter.url, data=self.inverter.params)
                break
            except requests.exceptions.ConnectionError as e:
                logging.info('Sleeping for 2 seconds', exc_info=e)
                time.sleep(2)
        else:
            raise ConnectionError(f"Unable to connect to inverter at {self.inverter.url}")

        solax_data = self.inverter.response_model.model_validate(response.json())
        info_fields = dict(zip(self.inverter.information_model.model_fields, solax_data.information))
        self.solax_information = self.inverter.information_model.model_validate(info_fields)
        data_fields = dict(zip(self.inverter.data_model.model_fields, solax_data.data))
        self.data = self.inverter.data_model.model_validate(data_fields)

    def __iter__(self):
        for sensor, value in self.data.model_dump().items():
            if not hasattr(value, 'unit_of_measure'):
                continue

            yield sensor, value
