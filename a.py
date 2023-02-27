import json
import valohai


def log_metadata(md):
    print(json.dumps(md))


exec_id = valohai.parameters('exec_id').value
log_metadata({"id": exec_id, "next_ids": [13, 15, 17]})
log_metadata({"last": True, "percent": 1})

log_metadata({"publish_results": "False"})
