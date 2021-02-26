from color_printing import print_rgb, Color


def simulate(city):
    tick = 0
    completions = 0

    while tick < city.time_allocated:
        print_rgb(f"Tick: {tick}", Color.BLUE)

        # Update all car positions
        for car_id, car in city.cars.items():
            # Skip this car if it has arrived
            if car.arrived:
                continue

            road = city.roads[car.road]

            # Mark this car as arrived if if it has arrived
            if not car.arrived and car.on_last_road() and car.at_end_of_road(road.length):
                car.arrived = True
                completions += 1
                print_rgb(f"Car {car.name} completed its journey", Color.GREEN)
                continue

            # Move car forward
            if car.at_end_of_road(road.length):
                light = city.lights[road.light_out]

                # Car just got to the light
                if not car.waiting:
                    car.waiting = True
                    road.cars_waiting.put(car_id)

                # Check if light is green and car is first in line, then move
                if light.is_green(road.id) and road.is_first_in_line(car_id):
                    road.cars_waiting.get()
                    car.next_road()
                    next_road = city.roads[car.road]
                    print_rgb(f"{car.name} passed through {light.name} "
                              f"from {road.name} to {next_road.name}", Color.PURPLE)
                else:
                    print_rgb(f"{car.name} waiting at {light.name}", Color.YELLOW)
            else:
                mile = car.drive()
                print(f"{car.name} drove on {road.name} to mile {mile}")

        # Update all lights
        for _, light in city.lights.items():
            light.tick()

        tick += 1
    
    return completions