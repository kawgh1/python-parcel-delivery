# Kolton Webber

import datetime
from Package.CSVPackages import get_hash_map
from Package.CSVPackages import global_distance


class Main:
    # Message display on startup. User input provides data readout
    print('Welcome to the Parcel Tracking System!')
    print('Today\'s route was completed in', '{0:.2f}'.format(global_distance, 2), 'miles.')
    start = input(" - Type 'search' to view a specific packageID number\n"
                  " - Type 'time value' to view delivery status for all packages at a specific time. \n"
                  " - Type 'exit' to quit. \n\n\n ")

    # Space-time complexity is O(N)
    while start is not 'exit':
        # if user types 'time value' then they are asked to enter a time value. Once a time value is provided it will
        # display all packages and their status at that time value. Runtime is O(N)
        if start == 'time value':
            try:

                # package_status_time = input('Please enter a time value as \'HH:MM:SS\' : ')
                package_status_time = input('---Please enter a 24 hour time value as HH:MM:SS : ')
                if package_status_time == 'exit':
                    print('--Thank you for using the Parcel Tracking System')
                    print('--Goodbye')
                    exit()
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Space-time complexity is O(N^2)

                for count in range(1, 41):
                    try:

                        first_time = get_hash_map().get(count).start_time
                        # second_time = second_time
                        (h, m, s) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        # (h, m, s) = second_time.split(':')
                        # convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                        truck_delivered = get_hash_map().get(count).time_delivered

                        convert_truck_delivered = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = truck_delivered.split(':')

                    except ValueError:
                        pass
                    # First checks all packages to see if it has left the HUB yet
                    # displays "HUB" and "not delivered"
                    if convert_first_time > convert_user_time:
                        get_hash_map().get(count).delivery_status = 'HUB'

                        print('Package ID:', get_hash_map().get(count).packageID_value, '   Package address:',
                              get_hash_map().get(count).address_value, get_hash_map().get(count).city,
                              get_hash_map().get(count).state, get_hash_map().get(count).zip_code,
                              '  Required delivery time:', get_hash_map().get(count).delivery_time_value,
                              ' Package weight:', get_hash_map().get(count).weight_value, '  Truck status:',
                              get_hash_map().get(count).delivery_status, '  Delivery status: not delivered')

                    # Then checks to see which packages have left the hub but have not yet been delivered
                    # displays "IN TRANSIT"
                    elif convert_first_time <= convert_user_time:

                        truck_delivered = get_hash_map().get(count).time_delivered

                        convert_truck_delivered = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = truck_delivered.split(':')

                        if convert_user_time < convert_truck_delivered:
                            get_hash_map().get(count).delivery_status = 'IN TRANSIT'

                            print('Package ID:', get_hash_map().get(count).packageID_value, '   Package address:',
                                  get_hash_map().get(count).address_value, get_hash_map().get(count).city,
                                  get_hash_map().get(count).state, get_hash_map().get(count).zip_code,
                                  '  Required delivery time:', get_hash_map().get(count).delivery_time_value,
                                  ' Package weight:', get_hash_map().get(count).weight_value, '  Truck status:',
                                  get_hash_map().get(count).delivery_status, '  Delivery status:',
                                  get_hash_map().get(count).delivery_status)

                        # If package has been delivered, display time delivered and "DELIVERED"
                        else:
                            get_hash_map().get(count).delivery_status = 'Delivered at ' + get_hash_map().get(count).time_delivered
                            print('Package ID:', get_hash_map().get(count).packageID_value, '   Package address:',
                                  get_hash_map().get(count).address_value, get_hash_map().get(count).city,
                                  get_hash_map().get(count).state, get_hash_map().get(count).zip_code,
                                  '  Required delivery time:', get_hash_map().get(count).delivery_time_value,
                                  ' Package weight:', get_hash_map().get(count).weight_value,'  Truck status:',
                                  get_hash_map().get(count).delivery_status, '  Delivery status: DELIVERED')

                    else:
                        print('---Invalid Entry.')
                        package_status_time = input('Please enter a 24 hour time value as HH:MM:SS : ')

            except (NameError, ValueError):
                print('---Invalid entry.')
                start = input(" - Type 'search' to view a specific packageID number\n"
                              " - Type 'time value' to view delivery status for all packages at a specific time. \n"
                              " - Type 'exit' to quit. \n")


        # If 'search' is entered the user is asked for a package ID and time value for that package
        # Space-time complexity is O(1)
        elif start == 'search':

            try:
                # get_hash_map().printHashMap()
                count = input('---Please enter a package ID to review: ')
                if count == 'exit':
                    print('--Thank you for using the Parcel Tracking System')
                    print('--Goodbye')
                    exit()
                first_time = get_hash_map().get(count).start_time
                # second_time = second_time
                # package_status_time = input('Please enter a time value as \'HH:MM:SS\' : ')
                package_status_time = input('---Please enter a 24 hour time value as HH:MM:SS : ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # (h, m, s) = second_time.split(':')
                # convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                truck_delivered = get_hash_map().get(count).time_delivered

                convert_truck_delivered = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = truck_delivered.split(':')
                # First checks all packages to see if it has left the HUB yet
                # displays "HUB" and "not delivered"
                if convert_first_time >= convert_user_time:

                    get_hash_map().get(count).delivery_status = 'HUB'
                    print ('\n  Package ID:', get_hash_map().get(count).packageID_value)
                    print ('  Package address:', get_hash_map().get(count).address_value, ' ', get_hash_map().get(count).city, ',',
                           get_hash_map().get(count).state, get_hash_map().get(count).zip_code)
                    print ('  Required delivery time:', get_hash_map().get(count).delivery_time_value)
                    print ('  Package weight:', get_hash_map().get(count).weight_value)
                    print ('\n     Truck status:', get_hash_map().get(count).delivery_status)
                    print ('     Delivery status:  not delivered ')
                    print ('\n')
                # Then checks to see which packages have left the hub but have not yet been delivered
                # displays "IN TRANSIT"
                elif convert_first_time <= convert_user_time:

                    truck_delivered = get_hash_map().get(count).time_delivered

                    convert_truck_delivered = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = truck_delivered.split(':')

                    if convert_user_time < convert_truck_delivered:
                        get_hash_map().get(count).delivery_status = 'IN TRANSIT'

                        print ('\n  Package ID:', get_hash_map().get(count).packageID_value)
                        print ('  Package address:', get_hash_map().get(count).address_value, ' ', get_hash_map().get(
                            count).city, ',', get_hash_map().get(count).state, get_hash_map().get(count).zip_code)
                        print ('  Required delivery time:', get_hash_map().get(count).delivery_time_value)
                        print ('  Package weight:', get_hash_map().get(count).weight_value)
                        print ('\n     Truck status:', get_hash_map().get(count).delivery_status)
                        print ('     Delivery status:', get_hash_map().get(count).delivery_status)
                        print ('\n')
                    # If package has been delivered, display time delivered and "DELIVERED"
                    else:
                        get_hash_map().get(count).delivery_status = 'Delivered at ' + get_hash_map().get(
                            count).time_delivered

                        print ('\n  Package ID:', get_hash_map().get(count).packageID_value)
                        print ('  Package address:', get_hash_map().get(count).address_value, ' ', get_hash_map().get(
                            count).city, ',', get_hash_map().get(count).state, get_hash_map().get(count).zip_code)
                        print ('  Required delivery time:', get_hash_map().get(count).delivery_time_value)
                        print ('  Package weight:', get_hash_map().get(count).weight_value)
                        print ('\n     Truck status:', get_hash_map().get(count).delivery_status)
                        print ('     Delivery status: DELIVERED')
                        print ('\n')

                else:
                    print('---Invalid Entry or package not found.\n')
                    count = input('--Please enter another package ID or type \'exit\' to exit the program')
                    # entry = input()
                    # if entry == 'exit':
                    #     print('--Thank you for using the Parcel Tracking System')
                    #     print('--Goodbye')
                    #     exit()



            # except NameError:
            #     print('Invalid entry. Shutting down.')
            #     exit()

            except (ValueError, AttributeError):
                print('---Invalid Entry or package not found.')
                start = input(" - Type 'search' to view a specific packageID number\n"
                              " - Type 'time value' to view delivery status for all packages at a specific time. \n"
                              " - Type 'exit' to quit. \n")




        elif start == 'exit':
            print('--Thank you for using the Parcel Tracking System')
            print('--Goodbye')
            exit()
        else:
            print('--Invalid entry. Please try again.')
            start = input(" - Type 'search' to view a specific packageID number\n"
                          " - Type 'time value' to view delivery status for all packages at a specific time. \n"
                          " - Type 'exit' to quit. \n")





