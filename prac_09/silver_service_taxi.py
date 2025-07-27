from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A specialized Taxi with a higher fare based on fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness