# Vehicle Fuel Consumption Analyzer

A small Python project that analyzes sample vehicle trip records and identifies the least fuel-efficient vehicle, route, and time period.

## Features

- Validates required fields and positive distance/fuel measurements.
- Calculates overall fuel economy in kilometers per liter (km/L).
- Compares fuel economy by vehicle, route, and time period.
- Recommends which vehicle and route to review.

## Requirements

- Python 3
- No third-party packages required

## Run

```bash
python vehicle_fuel_consumption_analyzer.py
```

## Data fields

Each record includes a vehicle ID, route, period, distance in kilometers, and fuel in liters. Replace or extend the records list in the script with your own verified data.

Fuel economy is calculated as distance divided by fuel in km/L. A lower km/L value indicates more fuel used per kilometer. The included records are demonstration data, not real fleet measurements.
