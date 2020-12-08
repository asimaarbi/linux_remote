import shlex
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/api/volume/<status>')
def power_ops(status):
    if status == 'status':
        raw = subprocess.check_output(shlex.split("pacmd list-sinks"))
        is_muted = raw.find(b"muted: yes") != -1
        return is_muted
    subprocess.check_call(shlex.split(f"amixer -D pulse sset Master {status}"))
    return status


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
