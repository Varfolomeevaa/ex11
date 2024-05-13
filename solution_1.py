class AirConditioning:
    """
    The AirConditioning class represents an air conditioner model with the capability to control its status
    and temperature.

    Attributes:
        __status (bool): The on/off status of the air conditioner. Private class attribute.
        __temperature (int, optional): The current temperature set on the air conditioner. Private class attribute.

    Methods:
        status (property): Returns the current status of the air conditioner.
        status (status.setter): Sets a new status for the air conditioner.
        temperature (property): Returns the current temperature of the air conditioner.
        temperature (temperature.setter): Sets a new temperature for the air conditioner.
        switch_on (classmethod): Turns on the air conditioner and sets the temperature to 18 degrees Celsius.
        switch_off (classmethod): Turns off the air conditioner and resets the temperature to None.
        reset (classmethod): Resets the air conditioner to the default on status and temperature
        of 18 degrees Celsius if it is already on.
        get_temperature (classmethod): Retrieves the current temperature of the air conditioner.
        raise_temperature (classmethod): Increases the temperature by 1 degree Celsius, not exceeding the maximum
        limit of 43 degrees Celsius, if the air conditioner is on.
        lower_temperature (classmethod): Decreases the temperature by 1 degree Celsius, not going below the minimum
        limit of 0 degrees Celsius, if the air conditioner is on.
        __str__ (instance method): Returns a string representation of the air conditioner's status and temperature.
    """
    __status = False
    __temperature = None

    @property
    def status(self):
        """
        Returns the current status of the air conditioner.
        :return: The on/off status as a boolean.
        """
        return AirConditioning.__status

    @status.setter
    def status(self, new_status):
        """
        Sets a new status for the air conditioner.
        :param new_status: A boolean value representing the new status.
        """
        AirConditioning.__status = AirConditioning.__status

    @property
    def temperature(self):
        """
        Returns the current temperature of the air conditioner.
        :return: The temperature as an integer or None if the air conditioner is off.
        """
        return AirConditioning.__temperature

    @temperature.setter
    def temperature(self, new_temp):
        """
        Sets a new temperature for the air conditioner.
        :param new_temp: An integer value representing the new temperature.
        """
        AirConditioning.__temperature = AirConditioning.__temperature

    @classmethod
    def switch_on(cls):
        """
        Turns on the air conditioner and sets the temperature to 18 degrees Celsius.
        """
        AirConditioning.__status = True
        AirConditioning.__temperature = 18

    @classmethod
    def switch_off(cls):
        """
        Turns off the air conditioner and resets the temperature to None.
        """
        AirConditioning.__status = False
        AirConditioning.__temperature = None

    @classmethod
    def reset(cls):
        """
        Resets the air conditioner to the default on status and temperature of 18 degrees Celsius if it is already on.
        """
        if AirConditioning.__status:
            AirConditioning.__status = True
            AirConditioning.__temperature = 18

    @classmethod
    def get_temperature(cls):
        """
        Retrieves the current temperature of the air conditioner.
        :return: The current temperature as an integer or None if the air conditioner is off.
        """
        return AirConditioning.__temperature

    @classmethod
    def raise_temperature(cls):
        """
        Increases the temperature by 1 degree Celsius, not exceeding the maximum limit of 43 degrees Celsius,
        if the air conditioner is on.
        """
        if AirConditioning.__status:
            if 0 <= AirConditioning.__temperature + 1 <= 43:
                AirConditioning.__temperature += 1

    @classmethod
    def lower_temperature(cls):
        """
        Decreases the temperature by 1 degree Celsius, not going below the minimum limit of 0 degrees Celsius,
        if the air conditioner is on.
        """
        if AirConditioning.__status:
            if 0 <= AirConditioning.__temperature - 1 <= 43:
                AirConditioning.__temperature -= 1

    def __str__(self):
        """
        Returns a string representation of the air conditioner's status and temperature.
        :return: A string indicating whether the air conditioner is on or off and the current temperature setting.
        """
        if AirConditioning.__status:
            return f'Кондиционер включен. Температурный режим: {AirConditioning.__temperature} градусов.'
        return f'Кондиционер выключен.'
