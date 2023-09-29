# Welcome to EV Station Assets

# EV Charging Station Models

Welcome to the documentation for the **EV Charging Station Models** project. This project provides Pydantic models for commonly found assets in an electric vehicle (EV) charging station. These models are designed to facilitate data validation and manipulation in EV charging station management systems.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Available Models](#available-models)
5. [Usage Examples](#usage-examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The **EV Charging Station Models** project aims to simplify the handling of data related to EV charging stations. It provides a set of Pydantic models that you can use to validate, serialize, and work with data structures commonly found in EV charging stations, including connectors, charging sessions, and station configurations.

## Installation

You can install the **EV Charging Station Models** package using pip:

```bash
pip install ev-charging-station-models

```
Getting Started
To get started, import the necessary models from the package into your Python project and use them for data validation and manipulation.

```python
from ev_charging_station_models import ConnectorModel

# Create an instance of the ConnectorModel
connector_data = {
    "connector_id": 1,
    "connector_type": "CCS",
    "power_output_kw": 50.0,
}
connector = ConnectorModel(**connector_data)

# Validate data
connector.validate()

```
Available Models
The following Pydantic models are available in this package:

ConnectorModel: Represents an EV charging connector.
ChargingSessionModel: Represents an EV charging session.
StationConfigurationModel: Represents the configuration of an EV charging station.
For detailed information about each model and its attributes, refer to the API Reference section.

Usage Examples
Explore various usage examples and code snippets in the Usage Examples section to understand how to work with the models effectively.

Contributing
We welcome contributions from the community! If you'd like to contribute to the EV Charging Station Models project, please follow our contribution guidelines.

License
This project is licensed under the MIT License.




