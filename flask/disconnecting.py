import sys
import ssl
from getpass import getpass
import routeros_api


# RouterOS credentials and connection details
connection = routeros_api.RouterOsApiPool('192.168.51.1', username='admin', password='#MG.10T.C00l',use_ssl=False, port=8728, 
                                          plaintext_login=True)


# PPP user details
ppp_username = 'user1'  # Replace with the PPP username to disconnect
ppp_password = '123'  # Replace with the PPP password

try:
    api = connection.get_api()
    ppp_connection = api.get_resource('/ppp/secret')
    secrets =ppp_connection.get()
    print(secrets)
    found = False
    for secret in secrets:
        if secret['name'] == ppp_username:
            print(f"Disconnecting {ppp_username}.....")
            ppp_connection.remove(id=secret['id'])
            print (f"{ppp_username} Disconnected Successfully.")
            found = True
            break 
    else:
        print (f"{ppp_username} is not found  in ppoe secrets.")

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)