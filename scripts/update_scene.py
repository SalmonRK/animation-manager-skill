import json
import os
import sys
import argparse
import re

# --- DYNAMIC CONFIG ---
ANIM_ROOT = "/tmp/animations"
SKILL_ROOT = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(SKILL_ROOT, "..", "..", ".."))
TOOLS_PATH = os.path.join(WORKSPACE_ROOT, "TOOLS.md")

if os.path.exists(TOOLS_PATH):
    with open(TOOLS_PATH, 'r') as f:
        content = f.read()
        match = re.search(r'Production Root:\s*(.+)', content)
        if match:
            ANIM_ROOT = match.group(1).strip()

def update_scene(project_name, scene_id, key, value):
    root_path = os.path.join(ANIM_ROOT, project_name)
    json_path = os.path.join(root_path, "production.json")
    
    if not os.path.exists(json_path):
        print(f"Error: Project '{project_name}' not found at {json_path}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    for scene in data["scenes"]:
        if scene["scene_id"] == scene_id:
            if key in scene:
                scene[key] = value
            elif key in scene["paths"]:
                scene["paths"][key] = value
            else:
                print(f"Error: Key '{key}' not found in scene.")
                return
            
            with open(json_path, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Updated scene {scene_id} in {project_name}: {key} = {value}")
            return

    print(f"Error: Scene {scene_id} not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("scene_id", type=int)
    parser.add_argument("--key", required=True)
    parser.add_argument("--value", required=True)
    args = parser.parse_args()
    update_scene(args.project, args.scene_id, args.key, args.value)
