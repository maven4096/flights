class FlightsNotFound(Exception):
    """No flights were found."""
class FlightQueryError(Exception):
    """FlightQuery error."""
class AirportNotFound(FlightQueryError):
    """No airport was found."""