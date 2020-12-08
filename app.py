import shlex
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/api/volume/<status>')
def power_ops(status):
    if status == 'mute':
        stt = subprocess.check_call(shlex.split("amixer -D pulse sset Master mute"))
        return 'Muted'
    elif status == 'unmute':
        subprocess.check_call(shlex.split("amixer -D pulse sset Master unmute"))
        return 'Unmuted'
    else:
        raw = subprocess.check_output(shlex.split("pacmd list-sinks"))
        is_muted = raw.find("muted: yes") != -1
        return is_muted


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7778, debug=True)
