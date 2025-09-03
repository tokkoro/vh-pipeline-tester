import json
import valohai
import shutil


def log_metadata(md):
    print(json.dumps(md))


inputs = {
    "input_1": "",
    "result": "",
}

valohai.prepare(
    step='inference',
    image='python',
    default_inputs=inputs
)

batch_size = valohai.parameters('batch_size').value
precision = valohai.parameters('precision').value
confidence_threshold = valohai.parameters('confidence_threshold').value

quality = 0.97
confidence = 0.9456

analyzed_image = "no image"
for data_path in valohai.inputs("input_1").paths():
    analyzed_image = data_path


out_path = valohai.outputs('report').path('report.json')
with open(out_path, "w") as f:
    f.write(json.dumps({
        "batch_size": batch_size,
        "precision": precision,
        "confidence_threshold": confidence_threshold,
        "quality": quality,
        "confidence": confidence,
        "analyzed_image": analyzed_image,
    }))

for data_path in valohai.inputs("result").paths():
    out_path = valohai.outputs('analyzed_image').path(f'knot_result.png')
    shutil.copy(data_path, out_path)
    break

