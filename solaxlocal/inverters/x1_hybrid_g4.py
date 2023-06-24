from pydantic import Field, computed_field
from solaxlocal.inverters import *
from solaxlocal.models.data import Data200Model
from solaxlocal.models.information import InformationModel
from solaxlocal.models.response import ResponseModel
from solaxlocal.utils.units import *
from typing import Any, Callable


class X1HybridG4(Inverter):
    def __init__(self, ip_address: str | None = None, password: str | None = None):
        super().__init__(ip_address, password)
        self.params = f'optType=ReadRealTimeData&pwd={self.password}'
        self.response_model: Callable = X1HybridG4Model
        self.information_model: Callable = X1HybridG4InformationModel
        self.data_model: Callable = X1HybridG4DataModel


class X1HybridG4Model(ResponseModel):
    sn: str
    ver: str
    type: int
    data: list[int] = Field(alias='Data')
    information: list[Any] = Field(alias='Information')


class X1HybridG4InformationModel(InformationModel):
    field1: float
    field2: int
    field3: str
    field4: int
    field5: float
    field6: int
    field7: float
    field8: float
    field9: int
    field10: int


class X1HybridG4DataModel(Data200Model):
    class Config:
        arbitrary_types_allowed = True

    @computed_field
    def inverter_ac_voltage(self) -> Volts:
        return Volts(self.field000 / 10)

    @computed_field
    def inverter_ac_current(self) -> Amps:
        return Amps(self.field001 / 10)

    @computed_field
    def inverter_ac_power(self) -> Watts:
        return Watts(self.field002)

    @computed_field
    def grid_frequency(self) -> Hz:
        return Hz(self.field003 / 100)

    @computed_field
    def pv1_voltage(self) -> Volts:
        return Volts(self.field004 / 10)

    @computed_field
    def pv2_voltage(self) -> Volts:
        return Volts(self.field005 / 10)

    @computed_field
    def pv1_current(self) -> Amps:
        return Amps(self.field006 / 10)

    @computed_field
    def pv2_current(self) -> Amps:
        return Amps(self.field007 / 10)

    @computed_field
    def pv1_power(self) -> Watts:
        return Watts(self.field008)

    @computed_field
    def pv2_power(self) -> Watts:
        return Watts(self.field009)

    @computed_field
    def on_grid_total_yield(self) -> Kwh:
        return Kwh(dual_register(self.field011, self.field012) / 10)

    @computed_field
    def on_grid_daily_yield(self) -> Kwh:
        return Kwh(self.field013 / 10)

    @computed_field
    def battery_voltage(self) -> Volts:
        return Volts(self.field014 / 100)

    @computed_field
    def battery_current(self) -> Amps:
        return Amps(signed_16_bit(self.field015) / 100)

    @computed_field
    def battery_power(self) -> Watts:
        return Watts(signed_16_bit(self.field016))

    @computed_field
    def battery_temperature(self) -> DegreesC:
        return DegreesC(self.field017)

    @computed_field
    def battery_soc(self) -> Percent:
        return Percent(self.field018)

    @computed_field
    def grid_power(self) -> Watts:
        return Watts(signed_16_bit(self.field032))

    @computed_field
    def total_feed_in_energy(self) -> Kwh:
        return Kwh(dual_register(self.field034, self.field035) / 100)

    @computed_field
    def total_consumption(self) -> Kwh:
        return Kwh(dual_register(self.field036, self.field037) / 100)
