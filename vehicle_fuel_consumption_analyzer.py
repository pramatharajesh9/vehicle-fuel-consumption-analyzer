from collections import defaultdict

# Sample records: distance in km, fuel in liters
records = [
    {"vehicle": "V101", "route": "City", "period": "Morning", "distance": 120, "fuel": 15},
    {"vehicle": "V102", "route": "Highway", "period": "Morning", "distance": 200, "fuel": 12},
    {"vehicle": "V101", "route": "Highway", "period": "Evening", "distance": 180, "fuel": 18},
    {"vehicle": "V103", "route": "City", "period": "Evening", "distance": 100, "fuel": 14},
    {"vehicle": "V102", "route": "City", "period": "Afternoon", "distance": 110, "fuel": 13},
]


def valid_record(record):
    """Check that a record has the required fields and valid measurements."""
    required = ("vehicle", "route", "period", "distance", "fuel")
    return (
        all(field in record for field in required)
        and isinstance(record["distance"], (int, float))
        and isinstance(record["fuel"], (int, float))
        and record["distance"] > 0
        and record["fuel"] > 0
    )


# Clean and validate records
clean_records = [r for r in records if valid_record(r)]
if not clean_records:
    raise ValueError("No valid fuel records to analyze.")

# Accumulate distance and fuel by category
by_vehicle = defaultdict(lambda: [0, 0])
by_route = defaultdict(lambda: [0, 0])
by_period = defaultdict(lambda: [0, 0])

total_distance = total_fuel = 0

for r in clean_records:
    distance, fuel = r["distance"], r["fuel"]
    total_distance += distance
    total_fuel += fuel

    by_vehicle[r["vehicle"]][0] += distance
    by_vehicle[r["vehicle"]][1] += fuel
    by_route[r["route"]][0] += distance
    by_route[r["route"]][1] += fuel
    by_period[r["period"]][0] += distance
    by_period[r["period"]][1] += fuel


def efficiency(distance, fuel):
    """Return fuel efficiency in km per liter."""
    return distance / fuel


# Lower km/L means more fuel used per kilometer
vehicle_efficiency = {
    vehicle: efficiency(distance, fuel)
    for vehicle, (distance, fuel) in by_vehicle.items()
}
route_efficiency = {
    route: efficiency(distance, fuel)
    for route, (distance, fuel) in by_route.items()
}
period_efficiency = {
    period: efficiency(distance, fuel)
    for period, (distance, fuel) in by_period.items()
}

worst_vehicle = min(vehicle_efficiency, key=vehicle_efficiency.get)
worst_route = min(route_efficiency, key=route_efficiency.get)
worst_period = min(period_efficiency, key=period_efficiency.get)

print("VEHICLE FUEL CONSUMPTION SUMMARY")
print(f"Records analyzed: {len(clean_records)}")
print(f"Total distance:   {total_distance} km")
print(f"Total fuel used:  {total_fuel} L")
print(f"Overall economy:  {efficiency(total_distance, total_fuel):.1f} km/L")
print(
    f"Least efficient vehicle: {worst_vehicle} "
    f"({vehicle_efficiency[worst_vehicle]:.1f} km/L)"
)
print(
    f"Least efficient route:   {worst_route} "
    f"({route_efficiency[worst_route]:.1f} km/L)"
)
print(
    f"Highest-use period:      {worst_period} "
    f"({period_efficiency[worst_period]:.1f} km/L)"
)
print(
    "Recommendation: Inspect the least-efficient vehicle and review "
    "driving conditions on the least-efficient route."
)
