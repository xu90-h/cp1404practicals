from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the class SilverServiceTaxi's method"""

    #define a taxi with fanciness
    fancy_taxi = SilverServiceTaxi("Test taxi", 100, 2)
    fancy_taxi.drive(18)
    # print output
    print(fancy_taxi)

