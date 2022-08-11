import json
import valohai


def log_metadata(md):
    print(json.dumps(md))


param_1 = valohai.parameters('param_1').value
log_metadata({"param_1": param_1})
