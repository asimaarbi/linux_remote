import os
import shlex
import subprocess

from flask import Flask

from lock_screen import Display
from pesh_service import Discovery

app = Flask(__name__)
display = Display()
discovery = Discovery(9000)


@app.route('/api/volume/<status>')
def volume_ops(status):
    if status == 'status':
        print("yhn hoon main2")
        raw = subprocess.check_output(shlex.split("pacmd list-sinks"))
        is_muted = raw.find(b"muted: yes") != -1
        return f'{is_muted}'
    elif status == 'lock':
        subprocess.check_call(shlex.split("loginctl lock-session"))
        return 'lock'
    elif status == 'unlock':
        subprocess.check_call(shlex.split("loginctl unlock-session"))
        return 'unlock'
    subprocess.check_call(shlex.split(f"amixer -D pulse sset Master {status}"))
    return status


@app.route('/api/lock/')
def lock():
    return str(True if display.is_locked() else False), 200


if __name__ == '__main__':
    discovery.publish()
    app.run(host='0.0.0.0', port=5009, debug=True)
