def map_to_gmpro(request_data):
    shipments = []

    for job in request_data.jobs:
        shipments.append({
            "deliveries": [{
                "arrivalWaypoint": {
                    "location": {
                        "latLng": {
                            "latitude": job.location.lat,
                            "longitude": job.location.lng
                        }
                    }
                },
                "duration": f"{job.service_time}s"
            }],
            "loadDemands": {
                "weight": {
                    "amount": str(job.demand)
                }
            }
        })

    vehicles = []

    for v in request_data.vehicles:
        vehicles.append({
            "startWaypoint": {
                "location": {
                    "latLng": {
                        "latitude": v.start_location.lat,
                        "longitude": v.start_location.lng
                    }
                }
            },
            "endWaypoint": {
                "location": {
                    "latLng": {
                        "latitude": v.start_location.lat,
                        "longitude": v.start_location.lng
                    }
                }
            },
            "loadLimits": {
                "weight": {
                    "maxLoad": str(v.capacity)
                }
            }
        })

    return {
        "model": {
            "shipments": shipments,
            "vehicles": vehicles
        }
    }
