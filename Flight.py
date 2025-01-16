
#Aref Turkieh
#this file consists of the flight class representing the flight data with the flight number, duration, origin, destination



from Airport import * #import from the airport file

class Flight:
    def __init__(self, flight_no, origin, dest, dur):
        if not isinstance(origin, Airport) or not isinstance(dest, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        if not flight_no or not dur:
            raise ValueError("Invalid flight number or duration")
        #raise a valueError
        self._flight_no = flight_no.strip()
        self._origin = origin
        self._destination = dest
        self._duration = float(dur)
#this sets the destination, origin, flight and destination according with the function
    def __str__(self):
        domestic_status = "domestic" if self.is_domestic() else "international"# returns domestic if true else international
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({round(self._duration)}h) [{domestic_status}]"
# returns the city origin and city destination with the duration
    def __eq__(self, other):
        if isinstance(other, Flight):
            return self._origin == other._origin and self._destination == other._destination
        return False

    def __add__(self, conn_flight): # function that sets connecting flights while making sure its correct
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object.")
        if self._destination != conn_flight._origin:
            raise ValueError("These flights cannot be combined.")
        return Flight(
            self._flight_no,
            self._origin,
            conn_flight._destination,
            self._duration + conn_flight._duration
        )

    def get_flight_no(self):
        return self._flight_no # grabs the flight number

    def get_origin(self):
        return self._origin #same thing for origin

    def get_destination(self):
        return self._destination # same thing

    def get_duration(self):
        return self._duration # same thing

    def is_domestic(self):
        return self._origin.get_country() == self._destination.get_country()

    def set_origin(self, origin): # sets the past origin as the new origin
        if not isinstance(origin, Airport):
            raise TypeError("The origin must be an Airport object.")
        self._origin = origin

    def set_destination(self, destination): # same thing
        if not isinstance(destination, Airport):
            raise TypeError("The destination must be an Airport object.")
        self._destination = destination
