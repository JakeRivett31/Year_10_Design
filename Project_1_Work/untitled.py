url = "https://swapi.dev/api/people/1/"
	response = requests.get(url)
	response_json = response.json()