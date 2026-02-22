# 🎬 Animation Manager Skill

A professional, token-saving agent skill for managing multi-scene AI animation productions. It coordinates between ComfyUI (visuals), TTS (voice), and FFmpeg (editing) using a centralized JSON database.

## ✨ Features
- **Centralized Production:** Manages everything via a `production.json` database.
- **Character Consistency:** Ensures characters look the same across all scenes.
- **Visual Approval Protocol:** Mandatory human-in-the-loop check before expensive video rendering.
- **Token Efficiency:** Sub-agents read specific scene data from files rather than chat history.
- **Asset Templates:** Includes `assets/production_template.json` for rapid project setup.

## 🏗️ Studio Structure
- **Production Root:** `[YOUR_PRODUCTION_DIR]/Animations/`
- **Project Folder:**
    - `storyboard.md`: Human-readable script and descriptions.
    - `production.json`: Machine-readable database.
    - `outputs/`: Raw assets (PNG, MP4, MP3).
    - `final/`: Merged master movie.

## 🛠️ Tools (CLI)
### 1. Initialize Project
```bash
python3 skills/animation-manager/scripts/init_project.py "<project_name>" <total_scenes>
```
### 2. Update Scene Data
```bash
python3 skills/animation-manager/scripts/update_scene.py "<project_name>" <scene_id> --key <key> --value <value>
```
### 3. Export for FFmpeg
```bash
python3 skills/animation-manager/scripts/export_ffmpeg.py "<project_name>"
```

---
Developed by **SalmonRK** & **Ava (เอวา)** 🎀
