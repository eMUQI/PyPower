from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    password = request.form.get("password")
    if password == "mypassword":
        # subprocess.call(["shutdown", "/s", "/t", "60"])
        subprocess.call(["calc"])
        return "电脑将在60秒后关机，请保存好未保存的数据并退出程序。"
    else:
        return "密码错误，请重新输入。"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
