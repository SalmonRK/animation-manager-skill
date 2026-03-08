import json
import os
import sys
import re

# Load environment variables from .env file
def load_env():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

load_env()

# --- DYNAMIC CONFIG ---
ANIM_ROOT = os.environ.get("ANIM_ROOT", "/tmp/animations")

def init_project(project_name, total_scenes, char_name="MariClaw (มาริคลอ)"):
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
            "name": char_name,
            "description": "Describe appearance, age, and clothing style here.",
            "consistency_prompt": "Provide a detailed visual prompt for character consistency here."
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
        print("Usage: python3 init_project.py <name> <scenes> [char_name]")
    else:
        name = sys.argv[1]
        scenes = int(sys.argv[2])
        char = sys.argv[3] if len(sys.argv) > 3 else "MariClaw (มาริคลอ)"
        init_project(name, scenes, char)
