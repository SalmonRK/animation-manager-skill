import json
import os
import sys

def export_ffmpeg(project_name):
    root_path = f"/Users/salmonrk/Ai-Art/AvaClaw/Animations/{project_name}"
    json_path = f"{root_path}/production.json"
    list_path = f"{root_path}/outputs/filelist.txt"
    
    if not os.path.exists(json_path):
        print(f"Error: Project '{project_name}' not found.")
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
