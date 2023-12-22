import requests
def get_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json().get('value')
    print(joke)

if __name__ == "__main__":
    get_joke()
