import requests

headers = {
    'referer': 'https://turo.com/en-us/search?defaultZoomLevel=11&delivery=true&deliveryLocationType=airport&endDate=01%2F31%2F2020&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&latitude=33.9415889&location=LAX%20-%20Los%20Angeles%20International%20Airport&locationType=Airport&longitude=-118.40853&maximumDistanceInMiles=50&placeId=ChIJtU-yE9KwwoAR8a2LaVd7qHc&sortType=RELEVANCE&startDate=01%2F11%2F2020&startTime=10%3A00',
}

params = (
    ('country', 'US'),
    ('defaultZoomLevel', '11'),
    ('delivery', 'false'),
    ('deliveryLocationType', 'googlePlace'),
    ('endDate', '01/31/2020'),
    ('endTime', '11:00'),
    ('international', 'true'),
    ('isMapSearch', 'false'),
    ('itemsPerPage', '300'),
    ('latitude', '33.9415889'),
    ('location', ''),
    ('locationType', 'airport'),
    ('longitude', '-118.40853'),
    ('maximumDistanceInMiles', '50'),
    ('placeId', 'ChIJtU-yE9KwwoAR8a2LaVd7qHc'),
    ('region', 'CA'),
    ('sortType', 'RELEVANCE'),
    ('startDate', '01/11/2020'),
    ('startTime', '10:00'),
)


r = requests.get('https://turo.com/api/search', headers = headers, params=params)
data = r.json()
listings = data['list']

for listing in listings:
    car_name = ' '.join([listing['vehicle']['make'], listing['vehicle']['model']])
    car_year = listing['vehicle']['year']
    car_trip = listing['renterTripsTaken']
    car_allstar = listing['owner']['allStarHost']
    print('CarModel'':',car_name,car_year,'/ ','TotalTrip' ':' ,car_trip, '/ ', 'Host' ':',car_allstar)
