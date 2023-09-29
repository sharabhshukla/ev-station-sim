from ev_station_assets.assets import GenericBattery, GenericBatteryState


battery_initial_state = GenericBatteryState(
    soc=0.5,
    current_power=0.00
)

battery_1 = GenericBattery(
    name="battery_1",
    nameplate_capacity=350.00,
    capacity=350.00,
    inverter_size=150.00,
    current_state=battery_initial_state
)

