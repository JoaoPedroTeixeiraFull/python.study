import requests

# The ZIP code (CEP) we want to look up
zip_code = "01001000"  # Praça da Sé, São Paulo

# The API URL
api_url = f"https://viacep.com.br{zip_code}/json/"

# Making the HTTP GET request to the API
response = requests.get(api_url)

# Converting the response data into a Python dictionary
address_data = response.json()

# Extracting and printing the info
if "erro" not in address_data:
    street = address_data["logradouro"]
    neighborhood = address_data["bairro"]
    city = address_data["localidade"]
    state = address_data["uf"]
    
    print(f"Address Found:\n{street}, {neighborhood} - {city}/{state}")
else:
    print("Invalid ZIP code.")

import requests
print("Instalado com sucesso!")