import requests
import json


API_URL = "https://jsonplaceholder.typicode.com/posts/1"
OUTPUT_FILE = "response.json"

def make_api_call(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()

        return response_data
    except requests.exceptions.RequestException as e:

        print(f"Error making API call: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def save_response_to_file(data, filename):
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Response data saved to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")
        raise

def main():
    response_data = make_api_call(API_URL)
    save_response_to_file(response_data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
