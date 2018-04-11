from django.shortcuts import render
import requests

def test(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'tests/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyA4XcwimiWKVJCOJIoSEY2kIU6bfkagcoI'  # Don't do this! This is just an example. Secure your keys properly.
    })