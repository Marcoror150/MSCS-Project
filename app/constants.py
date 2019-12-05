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