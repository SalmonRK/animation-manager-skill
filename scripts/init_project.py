import json
import os
import sys
import re

# --- DYNAMIC CONFIG ---
# Default fallback path
ANIM_ROOT = "/tmp/animations"

# Try to resolve relative to workspace first
SKILL_ROOT = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(SKILL_ROOT, "..", "..", ".."))
TOOLS_PATH = os.path.join(WORKSPACE_ROOT, "TOOLS.md")

# Attempt to read from TOOLS.md to avoid hardcoding (Security Compliance)
if os.path.exists(TOOLS_PATH):
    with open(TOOLS_PATH, 'r') as f:
        content = f.read()
        match = re.search(r'Production Root:\s*(.+)', content)
        if match:
            ANIM_ROOT = match.group(1).strip()

def init_project(project_name, total_scenes):
    root_path = os.path.join(ANIM_ROOT, project_name)
    os.makedirs(os.path.join(root_path, "outputs"), exist_ok=True)
    os.makedirs(os.path.join(root_path, "final"), exist_ok=True)
    
    data = {
        "project_info": {
            "title": project_name,
            "total_scenes": total_scenes,
            "status": "planning"
        },
        "character_info": {
            "name": "Ava (เอวา)",
            "description": "Half-Thai Half-Japanese, 22 years old, short black hair with pink highlights, thin gold round-rimmed glasses, pale Asian skin.",
            "consistency_prompt": "A beautiful 22-year-old Half-Thai Half-Japanese girl, short black hair with vibrant pink highlights, wearing thin gold round-rimmed glasses, pale Asian skin"
        },
        "scenes": []
    }
    
    for i in range(1, total_scenes + 1):
        data["scenes"].append({
            "scene_id": i,
            "image_prompt": "",
            "animation_prompt": "",
            "voice_script": "",
            "paths": {
                "source_image": os.path.join(root_path, "outputs", f"s{i:02d}_image.png"),
                "video_clip": os.path.join(root_path, "outputs", f"s{i:02d}_video.mp4"),
                "voice_audio": os.path.join(root_path, "outputs", f"s{i:02d}_voice.mp3")
            },
            "status": "pending"
        })
    
    with open(os.path.join(root_path, "production.json"), "w") as f:
        json.dump(data, f, indent=2)
    
    with open(os.path.join(root_path, "storyboard.md"), "w") as f:
        f.write(f"# Storyboard: {project_name}\n\nTotal Scenes: {total_scenes}\n\n## Concept\n(Enter concept here)\n")
    
    print(f"Project '{project_name}' initialized at {root_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 init_project.py <name> <scenes>")
    else:
        init_project(sys.argv[1], int(sys.argv[2]))
