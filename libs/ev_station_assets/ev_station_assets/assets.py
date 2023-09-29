from ev_station_assets.abstract.battery import AbstractBattery, AbstractBatteryState
from ev_station_assets.abstract.ev_chargers import AbstractCharger, AbstractChargerState
from ev_station_assets.abstract.onsite_loads import AbstractSiteLoad, AbstractSiteLoadState
from ev_station_assets.abstract.generators import AbstractGenerator, AbstractGeneratorState


class GenericBatteryState(AbstractBatteryState):
    pass


class GenericBattery(AbstractBattery):
    pass


class GenericEVChargerState(AbstractChargerState):
    pass


class GenericEVCharger(AbstractCharger):
    pass


class GenericSiteLoadState(AbstractSiteLoadState):
    pass


class GenericSiteLoad(AbstractSiteLoad):
    pass


class GenericGeneratorState(AbstractGeneratorState):
    pass


class GenericGenerator(AbstractGenerator):
    pass
