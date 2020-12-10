import requests
import json
import swapi






for planet in swapi.get_all("planets").order_by("diameter"):
    print(planet.name)
