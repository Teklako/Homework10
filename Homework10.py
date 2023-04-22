import requests
def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return "Request failed with status code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return "Connection failed: " + str(e)



