import json
import os

input_file = "response.json"
output_file = "modified_response.json"

try:

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' does not exist.")

    with open(input_file, "r") as file:
        try:
            response_data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in '{input_file}': {e}")


    response_data["title"] = "Modified Title"

    with open(output_file, "w") as file:
        json.dump(response_data, file, indent=4)

    print(f"Successfully modified the response and saved to '{output_file}'.")

except FileNotFoundError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error: {e}")

except PermissionError as e:
    print(f"Permission error when accessing files: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
