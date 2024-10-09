import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content  # Return raw bytes
        else:
            raise Exception(f"Failed to get data: {response.status_code}")

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))  # Decode bytes to string and then load JSON

# Example usage:
if __name__ == "__main__":
    get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
    data = get_requester.load_json()
    print(data)
