from color_printing import print_rgb, Color


def simulate(city, following=None):
    if following is None:
        following = [car_id for car_id in city.cars]

    arrivals = 0
    for tick in range(city.time_allocated):
        print_rgb(f"TICK {tick}", Color.BLUE)

        # Update all car positions
        for car_id, car in city.cars.items():
            # Skip this car if it has arrived
            if car.arrived:
                continue

            road = city.roads[car.road]

            # Mark this car as arrived if if it has arrived
            if not car.arrived and car.on_last_road() and car.at_end_of_road(road.length):
                car.arrived = True
                arrivals += 1
                if car.id in following:
                    print_rgb(f"{car.name} ARRIVED", Color.GREEN)
                continue

            # Move car forward
            if car.at_end_of_road(road.length):
                light = city.lights[road.light_out]

                # Car just got to the light
                if not car.waiting:
                    car.waiting = True
                    road.cars_waiting.put(car_id)

                # Check if light is green and car is first in line, then move
                if light.is_green(road.id) and not light.used and road.is_first_in_line(car_id):
                    road.cars_waiting.get()
                    car.next_road()
                    light.used = True
                    next_road = city.roads[car.road]
                    if car.id in following:
                        print_rgb(f"{car.name} PASS {light.name} "
                                  f"{road.name} {next_road.name}", Color.PURPLE)
                else:
                    if car.id in following:
                        print_rgb(f"{car.name} WAIT {light.name}",
                                  Color.YELLOW)
            else:
                mile = car.drive()
                if car.id in following:
                    print_rgb(
                        f"{car.name} DRIVE {road.name} {mile}", Color.GRAY)

        # Update all lights
        for _, light in city.lights.items():
            light.tick()
            light.used = False

    return arrivals
