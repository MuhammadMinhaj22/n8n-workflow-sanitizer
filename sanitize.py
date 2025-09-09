import json
import re
from tkinter import Tk, filedialog

Tk().withdraw()

file_path = filedialog.askopenfilename(
    title="Choose n8n workflow",
    filetypes=[("JSON files", "*.json")]
)

if not file_path:
    print("No file selected!")
    exit()

safe_path = file_path.replace(".json", "_safe.json")

with open(file_path, "r", encoding="utf-8") as f:
    flow = json.load(f)

for n in flow.get("nodes", []):
    n.pop("credentials", None)

for n in flow.get("nodes", []):
    if n.get("type") == "n8n-nodes-base.webhook":
        if "parameters" in n:
            n["parameters"]["path"] = "my-webhook"

def mask_ids(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.lower().endswith("id"):
                obj[k] = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            else:
                obj[k] = mask_ids(v)
    elif isinstance(obj, list):
        return [mask_ids(x) for x in obj]
    return obj

flow = mask_ids(flow)

text = json.dumps(flow, indent=2, ensure_ascii=False)

text = re.sub(
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    text
)

with open(safe_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Clean workflow saved as:", safe_path)

