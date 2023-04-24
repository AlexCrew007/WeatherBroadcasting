from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method=='POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=35e18e5f5025dc2beda4c1d72b6873f1').read()
        list_of_data=json.loads(source)
        print(list_of_data)
        data={
            "city":city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '+ str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
            }
    else:
        data={}
    return render(request, "main/index.html", data)

