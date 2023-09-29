from ev_station_assets.assets import GenericBattery, GenericBatteryState
from math import isclose


def test_battery_state():
    initial_state = GenericBatteryState(soc=0.5, current_power=100.5)
    assert initial_state.soc == 0.5
    assert initial_state.current_power == 100.5


def test_battery():
    initial_state = GenericBatteryState(soc=0.5, current_power=100.5)
    battery = GenericBattery(name="battery1",
                             nameplate_capacity=300.5,
                             inverter_size=50.5,
                             capacity=100.05,
                             current_state=initial_state)

    assert battery.name == "battery1"
    assert isclose(a=battery.nameplate_capacity, b=300.5, rel_tol=0.0001)
    assert isclose(a=battery.inverter_size, b=50.5, rel_tol=0.001)
    assert isclose(a=battery.current_state.soc, b=0.5, rel_tol=0.0001)
    assert isclose(a=battery.current_state.current_power, b=100.5, rel_tol=0.0001)
    assert isclose(a=battery.capacity, b=100.05, rel_tol=0.0001)
