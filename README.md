# SolaX Local
A python API for accessing SolaX data locally from a SolaX Pocket Wifi Dongle.
## Installation
Installation is using pip directly from GitHub:
```bash
pip install git+https://github.com/SimonPiercy/SolaxLocal.git#egg=solaxlocal
```
## Usage
First set up an inverter supplying your inverter's IP address
and password (serial number). These can be passed directly, or alternatively set the 
`SOLAX_LOCAL_IP_ADDRESS` and `SOLAX_LOCAL_PASSWORD` environment variables.
```
from solaxlocal import SolaxLocal, X1HybridG4
inverter = X1HybridG4(ip_address='192.168.0.101', password='ABCDEFGHIJ')
```
Now create the SolaxLocal object:
```
solax_local = SolaxLocal(inverter)
```
Use the built-in iterator to list all the calculated attributes,
along with their unit of measure:
```
for sensor, value in solax_local:
    print(f'{sensor}: {value} {value.unit_of_measure}')
```
Alternative you can access the attributes from the data property

```
ac_power = solax_local.data.inverter_ac_power
print(ac_power, ac_power.unit_of_measure)
```
or dump the entire model:
```
print(solax_local.data.model_dump())
```
## API Reference: attributes
`data` stores the response from the API listed as a series of fields
(field000 to field 199). Also includes any calculated fields and their units of measure.
## API Reference: methods
`refresh()` refreshes the data from the dongle.
## Supported Inverters
The following inverters are supported. For additional inverter support, please submit a PR or raise an issue.
- SolaX X1 Hybrid (Gen 4)
## Notes
This is an unofficial API and is there is no affiliation with Solax Power.

To get your inverter's IP you will need to go into your router config
and locate the it from the list of connected devices.
Consider setting the IP to a static IP address.

As the dongle response can be intermittent, the API will retry
up to 10 times, each 3 seconds apart, before failing.

This package uses the v2 beta of pydantic, partly for future-proofing
, partly as it has some useful features.



