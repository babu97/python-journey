import sys
import ssl
from getpass import getpass
import routeros_api

# Function to create a new RouterOS connection
def create_connection():
    return routeros_api.RouterOsApiPool('192.168.51.1', username='admin', password='#MG.10T.C00l', use_ssl=False, port=8728,
                                        plaintext_login=True)

# RouterOS credentials and connection details
connection = create_connection()

# PPP user details
ppp_username = 'user2'  # Replace with the PPP username to add
ppp_password = '123'  # Replace with the PPP password

while True:
    try:
        api = connection.get_api()
        ppp_connection = api.get_resource('/ppp/secret')
        ppp_secret_data = {
            'name': ppp_username,
            'password': ppp_password,
            'service': 'pppoe',
            'profile': '3mpbs_CONN',
        }
        ppp_connection.add(**ppp_secret_data)
        print(f"{ppp_username} added successfully.")
        break  # Exit the loop if successful

    

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)