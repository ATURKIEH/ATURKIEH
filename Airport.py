#Aref Turkieh
#this file contains the airport class consisting of representing the airport data, code, city, country



class Airport:
    def __init__(self, code, city, country):
        #initialized the airport with its code, city, and country
        self._code = code.strip()
        self._city = city.strip()
        self._country = country.strip()

    def __str__(self):
        # this function return the representation of the airport
        return f"{self._code} ({self._city}, {self._country})"

    def __eq__(self, other):
        #checks the equality based on the airport code
        if isinstance(other, Airport):
            return self._code == other._code
        return False

    def get_code(self):
        return self._code #this function is used to grab code of the airport

    def get_city(self):
        return self._city # same for city

    def get_country(self):
        return self._country # same for country

    def set_city(self, city):
        self._city = city.strip() #set the city that has passed to a new one

    def set_country(self, country):
        self._country = country.strip() # same thing for country
