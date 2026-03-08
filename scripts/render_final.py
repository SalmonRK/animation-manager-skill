import json
import os
import sys
import subprocess

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

def render_final(project_name):
    root_path = os.path.join(ANIM_ROOT, project_name)
    json_path = os.path.join(root_path, "production.json")
    list_path = os.path.join(root_path, "outputs", "filelist.txt")
    output_video = os.path.join(root_path, "final", f"{project_name}_Final.mp4")
    
    if not os.path.exists(json_path):
        print(f"Error: Project '{project_name}' not found.")
        return

    # Ensure list is up to date
    with open(json_path, "r") as f:
        data = json.load(f)

    with open(list_path, "w") as f:
        for scene in data["scenes"]:
            video_path = scene["paths"]["video_clip"]
            if os.path.exists(video_path):
                # Use absolute path for FFmpeg
                f.write(f"file '{os.path.abspath(video_path)}'\n")
            else:
                print(f"Warning: Scene {scene['scene_id']} clip missing.")

    # FFmpeg Command
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_path,
        "-c", "copy", output_video
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Success! Final video rendered at: {output_video}")
        
        # Update production.json
        data["project_info"]["status"] = "completed"
        data["final_video_path"] = output_video
        with open(json_path, "w") as f:
            json.dump(data, f, indent=2)
            
    except subprocess.CalledProcessError as e:
        print(f"Error during FFmpeg render: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 render_final.py <name>")
    else:
        render_final(sys.argv[1])
