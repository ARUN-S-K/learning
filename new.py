import socket
import time
import keyboard  # Ensure the keyboard library is installed
#one pluse
CLOUD_IP = "4.240.96.209"  # Your cloud server's public IP
COMMAND_PORT = 5000

def run_user():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Register with the cloud server
    sock.sendto(b"register_user", (CLOUD_IP, COMMAND_PORT))
    print("Registered User with cloud server...")

    try:
        while True:
            command = 'STOP'  # Default command

            if keyboard.is_pressed('up'):
                if keyboard.is_pressed('left'):
                    command = 'UP_LEFT'
                elif keyboard.is_pressed('right'):
                    command = 'UP_RIGHT'
                else:
                    command = 'UP'
            elif keyboard.is_pressed('down'):
                if keyboard.is_pressed('left'):
                    command = 'DOWN_LEFT'
                elif keyboard.is_pressed('right'):
                    command = 'DOWN_RIGHT'
                else:
                    command = 'DOWN'
            elif keyboard.is_pressed('left'):
                command = 'LEFT'
            elif keyboard.is_pressed('right'):
                command = 'RIGHT'
                
            # Send the command
            timestamp = time.time()
            message = f"{command}|{timestamp}"
            
            # Send the command
            sock.sendto(message.encode(), (CLOUD_IP, COMMAND_PORT))

    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        sock.close()

if __name__ == "__main__":
    run_user()
#code ends no