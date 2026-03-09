import json
import os
import re
import unicodedata

root = "/Users/mariagrandury/Projects/somosnlp/lm-evaluation-harness"
json_path = os.path.join(root, "lm_eval/tasks/include_es/Spanish.json")
tasks_dir = os.path.join(root, "lm_eval/tasks/include_es")
include_file = os.path.join(tasks_dir, "include_es.yaml")


def slug_dash(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "default"


def slug_underscore(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s or "default"


with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

countries = sorted({rec.get("country", "unknown") for rec in data})

# Create per-country YAML files
for country in countries:
    cfg = slug_dash(country)
    task_id = f"include_es_{slug_underscore(country)}"
    out_path = os.path.join(tasks_dir, f"{task_id}.yaml")
    content = (
        "include: _include_es_yaml\n" f"dataset_name: {cfg}\n" f"task: {task_id}\n"
    )
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(content)

# Update include_es.yaml task list (append missing)
with open(include_file, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

try:
    start = next(i for i, line in enumerate(lines) if line.strip() == "task:")
except StopIteration:
    raise SystemExit("No 'task:' section found in include_es.yaml")

end = start + 1
while end < len(lines) and lines[end].startswith("  - "):
    end += 1

existing = {
    line.strip().split(" ", 1)[1]
    for line in lines[start + 1 : end]
    if line.strip().startswith("- ")
}

new_tasks = []
for country in countries:
    task_id = f"include_es_{slug_underscore(country)}"
    if task_id not in existing:
        new_tasks.append(f"  - {task_id}")

if new_tasks:
    lines[start + 1 : end] = lines[start + 1 : end] + new_tasks
    with open(include_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
