######################################
# Airport-Flight-Schedule-Final-Part #
# MD MEZBAH UDDIN                    #
# Nantong University(China)          #
# CSE                                #
#                                    #
######################################


from TravelAgent import TravelAgent

def main():
    # print('main function is excuting: ')
    travel_agent = TravelAgent('Go Jaan')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC','PRA','05/07/2056')
    # print('aircraft', trip_info1[0])
    # print('price',trip_info1[1])
    # print('aircraft',trip_info1.aircraft)
    # print('aircraft',trip_info1.cost)

    trip_cities = ['DUB','ORD','LHR','SYD','JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities,'05/11/2565')
    print('price',trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)

if __name__ == '__main__':
    main()

    
    