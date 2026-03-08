# 🎬 Animation Manager Skill

A professional, token-saving agent skill for managing multi-scene AI animation productions. It coordinates between ComfyUI (visuals), TTS (voice), and FFmpeg (editing) using a centralized JSON database.

## ✨ Features
- **Centralized Production:** Manages everything via a `production.json` database.
- **Character Consistency:** Ensures characters look the same across all scenes.
- **Visual Approval Protocol:** Mandatory human-in-the-loop check before expensive video rendering.
- **Token Efficiency:** Sub-agents read specific scene data from files rather than chat history.
- **Asset Templates:** Includes `assets/production_template.json` for rapid project setup.

## 🏗️ Studio Structure
- **Production Root:** Configured via `.env` file (See `SKILL.md` for setup).
- **Global Skill Path:** `~/.openclaw/skills/animation-manager/` (Centralized for all agents).
- **Project Folder Layout:**
    - `storyboard.md`: Creative vision and scene-by-scene script.
    - `production.json`: Central database for prompts, file paths, and production status.
    - `outputs/`: Raw assets (PNG, MP4, MP3).
    - `final/`: Merged master movies.

## 🛠️ Tools (CLI)
Invoke via the `exec` command using the global skill path:

### 1. Initialize Project
```bash
python3 ~/.openclaw/skills/animation-manager/scripts/init_project.py "<project_name>" <total_scenes>
```

### 2. Update Scene Data
```bash
python3 ~/.openclaw/skills/animation-manager/scripts/update_scene.py "<project_name>" <scene_id> --key <key> --value <value>
```

### 3. Export & Render
- **Export List:** `python3 ~/.openclaw/skills/animation-manager/scripts/export_ffmpeg.py "<project_name>"`
- **Master Render:** `python3 ~/.openclaw/skills/animation-manager/scripts/render_final.py "<project_name>"` (Combines all completed scenes).

## 🛡️ Security & Privacy
- **Private Config:** All sensitive paths and IPs are stored in a local `.env` file, which is excluded from version control via `.gitignore`.

---
Developed by **SalmonRK** & **Ava (เอวา)** 🎀
