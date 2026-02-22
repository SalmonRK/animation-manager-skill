# Animation Manager Skill 🎬✨

A professional skill for managing multi-scene AI animation productions. It coordinates between ComfyUI (visuals), TTS (voice), and FFmpeg (editing) using a centralized JSON database.

## 🏗️ Studio Structure
- **Production Root:** `/Users/salmonrk/Ai-Art/AvaClaw/Animations/`
- **Project Structure:**
    - `storyboard.md`: Human-readable script and scene descriptions.
    - `production.json`: Machine-readable database for character info, prompts, paths, and status.
    - `outputs/`: Raw assets (PNG, MP4, MP3).
    - `final/`: Merged master movie.

## 👥 Character Consistency
Each `production.json` includes a `character_info` block. Sub-agents MUST use the `consistency_prompt` provided in this block as the base for all image generation to ensure Ava looks the same in every scene.

## 🛠️ Tools (CLI)
### 1. Initialize Project
`python3 skills/animation-manager/scripts/init_project.py "<project_name>" <total_scenes>`
- Creates the folder structure and a blank `production.json`.

### 2. Update Scene Data
`python3 skills/animation-manager/scripts/update_scene.py "<project_name>" <scene_id> --key <key> --value <value>`
- Updates specific scene info (e.g., prompt, path, status).

### 3. Export for FFmpeg
`python3 skills/animation-manager/scripts/export_ffmpeg.py "<project_name>"`
- Generates a file list for the `ffmpeg concat` command.

## 🚀 Production Workflow (Standard Protocol)
To ensure high quality and token efficiency, follow this 3-step process for every scene:

1. **Phase 1: Concept & Storyboard:** Define the plot and voice scripts in `storyboard.md` and `production.json`.
2. **Phase 2: Visual Approval (MANDATORY):** 
    - Generate images using ComfyUI first.
    - Present images to the user for review.
    - DO NOT proceed to video generation until the user explicitly approves the visuals.
3. **Phase 3: Animation & Post-Production:** 
    - Once approved, run `ltx2_video.py` for each scene.
    - Use the **Project-Specific Cron System** (temporary triggers in `CRON.md`) to monitor background rendering every 2-3 minutes.
    - Cleanup Cron triggers immediately after completion to save tokens.
