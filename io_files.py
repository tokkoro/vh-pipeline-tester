import json
import valohai


def log_metadata(md):
    print(json.dumps(md))


inputs = {
    "input_1": "",
    "input_2": "",
}

valohai.prepare(
    step='step-io',
    image='python',
    default_inputs=inputs
)

param_1 = valohai.parameters('param_1').value

for data_path in valohai.inputs("input_1").paths():
    with open(data_path) as f:
        data = json.load(f)
        print(f"my file contains {data}")
else:
    "ei"

for i in range(5):
    out_path = valohai.outputs('output_1').path(f'output_{i}.json')
    with open(out_path, "w") as f:
        f.write(json.dumps({"dataa": "on", "kaljaa": "ei", "kertoja": i}))
