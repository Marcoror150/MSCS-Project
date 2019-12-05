#~/bin/bash
#Tests below
httpCode=$(curl -s -o /dev/null -I -w "%{http_code}" 'http://localhost:8080/dannymulick1/CARS_Capping2019/1.0.2/data?make=20,30&model=37&mod_year=2008&fatals=3')
echo $httpCode
if [ $httpCode -ne 200 ]
then
  return 1
else
  return 0
fi