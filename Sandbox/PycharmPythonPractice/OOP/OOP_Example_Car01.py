class car:

    # Note: no return, it's just used to build the object,
    #       this is a class constructor
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, speed_difference):
        self.speed += abs(speed_difference)
        self.speed = min(self.max_speed, self.speed)

    def slowdown(self, speed_difference):
        self.speed -= abs(speed_difference)
        self.speed = max(self.speed, -5)


class vehicle:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, speed_difference):
        self.speed += abs(speed_difference)
        self.speed = min(self.max_speed, self.speed)

    def slowdown(self, speed_difference):
        self.speed -= abs(speed_difference)
        self.speed = max(self.speed, -5)


class Bus(vehicle): # Inheritance,

    def slow_down(self, speed_difference):
        super().slowdown(speed_difference)  # overrides the behaviour of vehicle class,
                                            # The super() statement makes a call to the parent class
                                            # to find the new speed, and then makes sure that this speed
                                            # is not below 0 km/h.
        self.speed=max(self.speed, 0)

bmw_x6 = car(model="BMW X6", max_speed=230)
print(bmw_x6.accelerate(30))


