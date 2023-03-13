# shutdown-web-control

[English](README.md) | [中文](https://github.com/eMUQI/PyPower/blob/main/README.md)

This project implements the remote shutdown function through a Flask web application.

## Project File Description

*Please do not deploy outside a trusted network environment!*

- `server.py`: Server (Windows) code file, used to receive shutdown requests sent by the client and execute the shutdown command.
- `client.py`: Client (Raspberry Pi) code file, provides a web page for users to enter the password and sends a shutdown request to the server. The server can also be woken up using wakeonlan.
- `templates/index.html`: Client web page template file.

## Modifying Code Files

1. If you need to modify the server-side shutdown command, you can modify the parameters of the `subprocess.call()` function in the `server.py` file.
2. If you need to modify the style or functionality of the client-side page, you can modify the `templates/index.html` file.
3. Before running the `client.py` file on the client computer, please make sure to modify `WINDOWS_IP` and `WINDOWS_PORT` to the IP address and port number of the server computer. Modify `WINDOWS_MAC_ADDRESS` to the MAC address of the server computer.


## Running

1. Run the `server.py` file on the server computer to start the Flask server (default using port 5000).
2. Run the `client.py` file on the client computer to start the Flask client (default using port 8000).
3. Enter the IP address and port number of the client computer in the browser to enter the shutdown page. Enter the correct password and click the "Shutdown" button to achieve remote shutdown.
4. This project is for learning and testing purposes only. Do not use it for illegal purposes.


## Acknowledgments

Thanks to ChatGPT for their contribution and help to this project.
