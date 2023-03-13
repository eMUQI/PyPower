from flask import Flask, render_template, request, redirect, url_for, session
import requests,os
from wakeonlan import send_magic_packet

app = Flask(__name__)
app.secret_key = "secret-key"

# Windows IP and Port
WINDOWS_IP = "192.168.1.10"
WINDOWS_PORT = 5000
WINDOWS_MAC_ADDRESS = "00:00:00:00:00:00"

# message = "init"

@app.route("/", methods=["GET", "POST"])
def index():
    print('This is a debug message')
    message = session.get("message")
    status = check_status()
    if request.method == "POST":
        print(request.form)
        if request.form["submit"] == "shutdown":
            password = request.form.get("password")
            response = requests.post(f"http://{WINDOWS_IP}:{WINDOWS_PORT}/shutdown", data={"password": password})
            message = response.text
        elif request.form["submit"] == "wakeup":

            wake_up(WINDOWS_MAC_ADDRESS)
            message = "正在唤醒，请稍候。"
        session["message"] = message
        status = check_status()
        return redirect(url_for('index'))
    return render_template("index.html", message=message, status=status)

@app.route("/check_status")
def check_status():
    try:
        requests.get(f"http://{WINDOWS_IP}:{WINDOWS_PORT}",timeout=1)
        return True
    except:
        return False
    
@app.route("/refresh")
def refresh():
    session.pop("message", None)
    return redirect(url_for('index'))

def wake_up(mac_address):
    try:
        send_magic_packet(mac_address)
    except:
        print("Error: Failed to wake up the computer.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
