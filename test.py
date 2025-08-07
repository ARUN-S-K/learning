import requests
import keyboard
import time

CLOUD_SERVER_URL = "http://4.240.96.209:5000/command"  # Replace with the cloud server's endpoint

def send_command(command):
    try:
        response = requests.post(CLOUD_SERVER_URL, json={"command": command})
        if response.status_code == 200:
            print(f"Command '{command}' sent successfully.")
        else:
            print(f"Failed to send command '{command}'. Server response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending command '{command}': {e}")

try:
    while True:
        if keyboard.is_pressed('up'):
            send_command('UP')
            if keyboard.is_pressed('left'):
                send_command('UP_LEFT')
            elif keyboard.is_pressed('right'):
                send_command('UP_RIGHT')
            else:
                send_command('UP')
            
        elif keyboard.is_pressed('down'):
            send_command('DOWN')
            if keyboard.is_pressed('left'):
                send_command('DOWN_LEFT')
            elif keyboard.is_pressed('right'):
                send_command('DOWN_RIGHT')
            else:
                send_command('DOWN')
                
        elif keyboard.is_pressed('left'):
            send_command('LEFT')
            
        elif keyboard.is_pressed('right'):
            send_command('RIGHT') 

        else:
            send_command('STOP')

        time.sleep(0.00000001)  # Adjust the delay as needed to reduce request frequency

except KeyboardInterrupt:
    print("Exiting...")