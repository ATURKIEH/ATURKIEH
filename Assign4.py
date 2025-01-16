#Aref Turkieh
#this file import both airport and flight files, it is the engine of the project it will access them through the get.()



from Flight import *
from Airport import *


all_flights = {}# dictionary
all_airports = []  #sets

def load_data(airport_file, flight_file):
    #passes through the 2 files
    try:
        airport_file = open(airport_file, "r") #opens the file to read them
        flight_file = open(flight_file, "r")

        for line in airport_file:# loops through every single line in a_file
            line = line.strip()#strips them and then splits them with dashes under
            section = line.split("-")
            code = section[0].strip()
            country = section[1].strip()#this sets the next section into a country
            city = section[2].strip()#same but for city
            all_airports.append(Airport(code, city, country))#this adds them together
        for line in flight_file:#same as the file before
            line = line.strip()
            section = line.rsplit("-", 3)
            flight_no = section[0].strip()
            origin_code = section[1].strip()
            dest_code = section[2].strip()
            duration = float(section[3].strip())

            origin = None#clears the origin and destination
            dest = None
            for airport in all_airports: #check through in a for loop airport in all airports
                if airport.get_code() == origin_code:
                    origin = airport
                if airport.get_code() == dest_code:
                    dest = airport
                if origin and dest:
                    break

            if origin and dest:
                flight = Flight(flight_no, origin, dest, duration)
                if origin_code not in all_flights:
                    all_flights[origin_code] = []
                all_flights[origin_code].append(flight)

        return True
    #exceptions below
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False

def get_airport_by_code(code):#gets the aiport code
    for airport in all_airports:
        if airport.get_code() == code:  # Use getter method
            return airport
    raise ValueError(f"No airport with the given code: {code}")

def find_all_city_flights(city):#finds all the city flights
    flights = []#list storing city flights

    for flight_list in all_flights.values():
        for flight in flight_list:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:   #checks if the flight origin or destination match the desired city
                flights.append(flight)

    return flights

def find_all_country_flights(country):#same thing
    flights = []
    for flight_list in all_flights.values():
        for flight in flight_list:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                flights.append(flight)
    return flights


def find_flight_between(orig_airport, dest_airport):
    #this function finds the connecting flights
    for flight in all_flights.get(orig_airport.get_code(), []):
        if flight.get_destination() == dest_airport:#if they are both equal then its a direct flight
            return f"Direct Flight: {orig_airport.get_code()} to {dest_airport.get_code()}"

    connections = set()
    for flight in all_flights.get(orig_airport.get_code(), []):
        #this loop runs through all the flights
        for connecting_flight in all_flights.get(flight.get_destination().get_code(), []):
            #this for loop runs through all of the connected flights
            if connecting_flight.get_destination() == dest_airport:
                connections.add(flight.get_destination().get_code())

    if connections:             # and tries to find a connection
        return connections

    raise ValueError(f"There are no direct or single-hop connecting flights from {orig_airport.get_code()} to {dest_airport.get_code()}")

def shortest_flight_from(orig_airport): #this function finds the shortest flight from the chosen airport
    flights_from_origin = all_flights.get(orig_airport.get_code(), [])
    if not flights_from_origin:
        raise ValueError(f"No flights found originating from {orig_airport.get_code()}")

    shortest_flight = flights_from_origin[0]
    #this sets the first one found as the shortest
    shortest_duration = shortest_flight.get_duration()

    for flight in flights_from_origin[1:]:
        if flight.get_duration() < shortest_duration:
            shortest_flight = flight
            shortest_duration = flight.get_duration()
            # finds the shortest duration

    return shortest_flight
#return the shortest flight

def find_return_flight(first_flight):
    for return_flight in all_flights.get(first_flight.get_destination().get_code(), []):
        if return_flight.get_destination() == first_flight.get_origin():        #when destination = origin it returns
            return return_flight
        #this will return the return flight

    raise ValueError(f"There is no flight from {first_flight.get_destination().get_code()} to {first_flight.get_origin().get_code()}")