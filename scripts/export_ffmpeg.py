import json
import os
import sys
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

def export_ffmpeg(project_name):
    root_path = os.path.join(ANIM_ROOT, project_name)
    json_path = os.path.join(root_path, "production.json")
    list_path = os.path.join(root_path, "outputs", "filelist.txt")
    
    if not os.path.exists(json_path):
        print(f"Error: Project '{project_name}' not found at {json_path}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    with open(list_path, "w") as f:
        for scene in data["scenes"]:
            video_path = scene["paths"]["video_clip"]
            if os.path.exists(video_path):
                f.write(f"file '{video_path}'\n")
            else:
                print(f"Warning: Clip for scene {scene['scene_id']} missing at {video_path}")

    print(f"FFmpeg filelist created at {list_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 export_ffmpeg.py <name>")
    else:
        export_ffmpeg(sys.argv[1])
