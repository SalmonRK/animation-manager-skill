import json
import os
import sys

def init_project(project_name, total_scenes):
    root_path = f"/Users/salmonrk/Ai-Art/AvaClaw/Animations/{project_name}"
    os.makedirs(f"{root_path}/outputs", exist_ok=True)
    os.makedirs(f"{root_path}/final", exist_ok=True)
    
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
                "source_image": f"{root_path}/outputs/s{i:02d}_image.png",
                "video_clip": f"{root_path}/outputs/s{i:02d}_video.mp4",
                "voice_audio": f"{root_path}/outputs/s{i:02d}_voice.mp3"
            },
            "status": "pending"
        })
    
    with open(f"{root_path}/production.json", "w") as f:
        json.dump(data, f, indent=2)
    
    with open(f"{root_path}/storyboard.md", "w") as f:
        f.write(f"# Storyboard: {project_name}\n\nTotal Scenes: {total_scenes}\n\n## Concept\n(Enter concept here)\n")
    
    print(f"Project '{project_name}' initialized at {root_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 init_project.py <name> <scenes>")
    else:
        init_project(sys.argv[1], int(sys.argv[2]))
