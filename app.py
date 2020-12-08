import shlex
import subprocess

from flask import Flask
app = Flask(__name__)


@app.route('/api/volume/<status>')
def power_ops(status):
    if status == 'mute':
        stt = subprocess.check_call(shlex.split("amixer -D pulse sset Master mute"))
        print(stt)
        return 'Muted'
    elif status == 'unmute':
        subprocess.check_call(shlex.split("amixer -D pulse sset Master unmute"))
        return 'Unmuted'
    else:
        stat = subprocess.check_call(shlex.split("pacmd list-sinks | awk '/muted/ { print $2 }'"))
        print(type(stat))
        return status




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7778, debug=True)
