import json
import valohai
import shutil


def log_metadata(md):
    print(json.dumps(md))


valohai.prepare(
    step='preprocessing',
    image='python',
    default_parameters={
        'd': 30.0
    }
)

diameter = valohai.parameters('d').value
log_metadata({"diameter": diameter})
log_metadata({"last": True, "percent": 1})

for data_path in valohai.inputs("input_1").paths():
    out_path = valohai.outputs('image').path(f'preprocessed_output_0.png')
    shutil.copy(data_path, out_path)
    break

