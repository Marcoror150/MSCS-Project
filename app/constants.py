make_numbers = {'American Motors': 1,
                'Jeep/Kaiser-Jeep/Willys Jeep': 2, 
                'AM General': 3, 
                'Chrysler': 6, 
                'Dodge': 7, 
                'Imperial': 8, 
                'Plymouth': 9, 
                'Eagle': 10, 
                'Ford': 12, 
                'Lincoln': 13, 
                'Mercury': 14, 
                'Buick/Opel': 18, 
                'Cadillac': 19, 
                'Chevrolet': 20, 
                'Oldsmobile': 21, 
                'Pontiac': 22, 
                'GMC': 23, 
                'Saturn': 24, 
                'Grumman': 25, 
                'Coda': 26, 
                'Other Domestic': 29, 
                'Volkswagon': 30, 
                'Alfa Romeo': 31, 
                'Audi': 32, 
                'Austin/Austin-Healey': 33, 
                'BMW': 34, 
                'Datsun/Nissan': 35, 
                'Fiat': 36, 
                'Honda': 37, 
                'Isuzu': 38, 
                'Jaguar': 39, 
                'Lancia': 40, 
                'Mazda': 41, 
                'Mercedes-Benz': 42, 
                'MG': 43, 
                'Peugeot': 44, 
                'Porsche': 45, 
                'Renault': 46, 
                'Saab': 47, 
                'Subaru': 48, 
                'Toyota': 49, 
                'Triumph': 50, 
                'Volvo': 51, 
                'Mitsubishi': 52, 
                'Suzuki': 53, 
                'Acura': 54, 
                'Hyundai': 55, 
                'Merkur': 56, 
                'Yugo': 57, 
                'Infiniti': 58, 
                'Lexus': 59, 
                'Daihatsu': 60, 
                'Land Rover': 62, 
                'Kia': 63, 
                'Daewoo': 64, 
                'Smart': 65, 
                'Mahindra': 66, 
                'Scion': 67, 
                'Other Imports': 69, 
                'BSA': 70, 
                'Ducati': 71, 
                'Harley-Davidson': 72, 
                'Kawasaki': 73, 
                'Moto Guzzi': 74, 
                'Norton': 75, 
                'Yamaha': 76, 
                'Victory': 77, 
                'Other Make Moped': 78, 
                'Other Make Motored Cycle': 79, 
                'Brockway': 80, 
                'Diamond Reo/Reo': 81, 
                'Freightliner': 82, 
                'FWD': 83, 
                'International Harvester/Navistar': 84, 
                'Kenworth': 85, 
                'Mack': 86, 
                'Peterbilt': 87, 
                'Iveco/Magirus': 88, 
                'White/Autocar, White/GMC': 89, 
                'Bluebird': 90, 
                'Eagle Coach': 91, 
                'Gillig': 92, 
                'MCI': 93, 
                'Thomas Built': 94, 
                'Not Reported': 97, 
                'Other Make': 98, 
                'Unknown': 99
            }

model_numbers = {
    'Automobiles': 0, 
    'Other(Autos)': 1, 
    'Unknown (Autos)': 2, 
    'Light Trucks': 3, 
    'Other (Light Trucks)': 4, 
    'Unknown (LT)': 5, 
    'Other (LSV or NEV)': 6, 
    'Unknown (LSV OR NEV)': 7, 
    'Motorcycles': 8, 
    'Electric Motorcycle': 9, 
    'Unknown cc (Motorcycles)': 10, 
    'All-Terrain Vehicles': 11, 
    'Unknown cc (ATV)Unkown (motored cycle)': 12, 
    'Other Make (Med/Heavy Trucks)': 13, 
    'Motor Home': 14, 
    'Med/Heavy Van-Based Vehicle': 15, 
    'Med/Heavy Pickup': 16, 
    'Med/Heavy Trucks - CBE': 17, 
    'Med/Heavy Trucks - COE': 18, 
    'Med/Heavy Trucks - COE (low entry)': 19, 
    'Med/Heavy Trucks - COE (high entry)': 20, 
    'Med/Heavy Trucks - Unknown engine location': 21, 
    'Med/Heavy Trucks - COE (entry position unknown)': 22, 
    'Other (Med/Heavy Trucks)': 23, 
    'Other Make (Buses)': 24, 
    'Buses': 25, 
    'Other (Bus)': 26, 
    'Unknown (Bus)': 27, 
    'Not Reported': 28, 
    'Other (Vehicle)': 29
    }

stateDict = {'AL': '1', 'AK': '2', 'AZ': '4', 'AR': '5', 'CA': '6', 'CO': '8', 'CT': '9', 'DE': '10', 'DC': '11', 'FL': '12', 'GA': '14', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20', 'KY': '21', 'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28', 'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54', 'WI': '55', 'WY': '56'}
percentDict = {
1: 2.48,
2: 0.18,
4: 2.42,
5: 1.47,
6: 9.73,
8: 1.72,
9: 0.77,
10: 0.35,
11: 0.06,
12: 8.41,
13: 4.30,
15: 0.25,
16: 0.61,
17: 2.85,
18: 2.35,
19: 0.88,
20: 1.05,
21: 2.21,
22: 2.08,
23: 0.42,
24: 1.49,
25: 0.89,
26: 2.88,
27: 1.10,
28: 1.80,
29: 2.50 ,
30: 0.46,
31: 0.63,
32: 0.91,
33: 0.29,
34: 1.59,
35: 0.89,
36: 2.77,
37: 3.95,
38: 0.30,
39: 3.23,
40: 1.84,
41: 1.22,
42: 3.39,
44: 0.14,
45: 2.74,
46: 0.30,
47: 2.79,
48: 10.08,
49: 0.79,
50: 0.15,
51: 2.12,
53: 1.55,
54: 0.72,
55: 1.60,
56: 0.32,
}

percentAvg = 0.87

agePctDict = {
"1923" : 0.0007 ,
"1927" : 0.0007 ,
"1928" : 0.0014 ,
"1929" : 0.0033 ,
"1930" : 0.0014 ,
"1931" : 0.0014 ,
"1932" : 0.0049 ,
"1933" : 0.0007 ,
"1934" : 0.0019 ,
"1936" : 0.0007 ,
"1937" : 0.0021 ,
"1938" : 0.0007 ,
"1939" : 0.0005 ,
"1940" : 0.0042 ,
"1941" : 0.0026 ,
"1942" : 0.0005 ,
"1945" : 0.0007 ,
"1946" : 0.0026 ,
"1947" : 0.0021 ,
"1948" : 0.0012 ,
"1949" : 0.0014 ,
"1950" : 0.0021 ,
"1951" : 0.0007 ,
"1952" : 0.0014 ,
"1954" : 0.0026 ,
"1955" : 0.0007 ,
"1956" : 0.0021 ,
"1957" : 0.0035 ,
"1958" : 0.0035 ,
"1959" : 0.0007 ,
"1960" : 0.0007 ,
"1961" : 0.0021 ,
"1962" : 0.0033 ,
"1963" : 0.0040 ,
"1964" : 0.0061 ,
"1965" : 0.0098 ,
"1966" : 0.0107 ,
"1967" : 0.0184 ,
"1968" : 0.0168 ,
"1969" : 0.0165 ,
"1970" : 0.0235 ,
"1971" : 0.0168 ,
"1972" : 0.0191 ,
"1973" : 0.0205 ,
"1974" : 0.0275 ,
"1975" : 0.0273 ,
"1976" : 0.0291 ,
"1977" : 0.0312 ,
"1978" : 0.0419 ,
"1979" : 0.0485 ,
"1980" : 0.0408 ,
"1981" : 0.0508 ,
"1982" : 0.0627 ,
"1983" : 0.0767 ,
"1984" : 0.1230 ,
"1985" : 0.1524 ,
"1986" : 0.1904 ,
"1987" : 0.1932 ,
"1988" : 0.2880 ,
"1989" : 0.3248 ,
"1990" : 0.4264 ,
"1991" : 0.5042 ,
"1992" : 0.6249 ,
"1993" : 0.8579 ,
"1994" : 1.2075 ,
"1995" : 1.5372 ,
"1996" : 1.6099 ,
"1997" : 2.3112 ,
"1998" : 2.7998 ,
"1999" : 3.4210 ,
"2000" : 4.2897 ,
"2001" : 4.5612 ,
"2002" : 5.0798 ,
"2003" : 5.5447 ,
"2004" : 5.7146 ,
"2005" : 6.1470 ,
"2006" : 6.1405 ,
"2007" : 6.1072 ,
"2008" : 5.0095 ,
"2009" : 3.2556 ,
"2010" : 3.3213 ,
"2011" : 3.7244 ,
"2012" : 4.2890 ,
"2013" : 4.6695 ,
"2014" : 4.9049 ,
"2015" : 5.0565 ,
"2016" : 3.4043 ,
"2017" : 1.4311 ,
"2018" : 0.1200 ,
}

ageAvg = 1.4487

topTenStates = {'TX': 10.079759161352108, 'CA': 9.734905060267915, 'FL': 8.414906085509836, 'GA': 4.301355882442033, 'NC': 3.9460163526086585, 'PA': 3.3898226098465165, 'OH': 3.2283470071091203, 'MI': 2.8816288298028505, 'IL': 2.845046333944595, 'TN': 2.7949492854762834}

topTenYears = {2005: 6.1470243518257455, 2006: 6.140500085048477, 2007: 6.107179722578857, 2004: 5.714558668303947, 2003: 5.544694722567206, 2002: 5.079840714686823, 2015: 5.056539761910864, 2008: 5.009471837303427, 2014: 4.904850559339372, 2013: 4.669510936302186}
topTenModels = {
    "Automobiles"                                  : 41.301405,
    "Light Trucks"                                 : 39.180319,
    "Motorcycles"                                  :  9.518905,
    "Med/Heavy Trucks - COE"                       :  5.799607,
    "Med/Heavy Trucks - Unknown engine location"   :  1.640387,
    "Med/Heavy Trucks - CBE"                       :  0.629126,
    "Unknown cc (Motorcycles)"                     :  0.392155,
    "All-Terrain Vehicles"                         :  0.260272,
    "Buses"                                        :  0.183145,
    "Med/Heavy Trucks - COE (low entry)"           :  0.154718
}

topTenMakes = {
    12     :14.727600,
    20     :14.258552,
    49     :8.214285,
    37     :7.517353,
    7      :6.421044,
    35     :4.922559,
    72     :3.934599,
    23     :3.142833,
    2      :2.622289,
    82     :2.437513
}