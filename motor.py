# udp_client.py
import socket
import keyboard
import time

UDP_IP = "192.168.183.180"  # Replace with your Raspberry Pi IP address
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_command(command):
    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))

try:
    print("Keyboard controller started. Use arrow keys. Press ESC to exit.")
    while True:
        if keyboard.is_pressed('esc'):
            break

        if keyboard.is_pressed('up'):
            if keyboard.is_pressed('left'):
                send_command('UP_LEFT')
            elif keyboard.is_pressed('right'):
                send_command('UP_RIGHT')
            else:
                send_command('UP')

        elif keyboard.is_pressed('down'):
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

        time.sleep(0.05)  # Avoid flooding

except KeyboardInterrupt:
    print("Exiting...")

finally:
    sock.close()
