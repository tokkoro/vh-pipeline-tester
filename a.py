import json
import valohai


def log_metadata(md):
    print(json.dumps(md))


valohai.prepare(
    step='step-a',
    image='python',
    default_parameters={
        'exec_id': 1
    }
)

exec_id = valohai.parameters('exec_id').value
log_metadata({"id": exec_id, "next": [13, 15, 17]})
log_metadata({"last": True, "percent": 1})
