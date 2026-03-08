# Animation Manager Skill 🎬✨

A professional skill for managing multi-scene AI animation productions. It coordinates between ComfyUI (visuals), TTS (voice), and FFmpeg (editing) using a centralized JSON database.

## 🏗️ Studio Structure
- **Production Root:** Configured via `.env` (Private)
- **Asset Storage:**
    - ComfyUI Assets: `/Users/salmonrk/.openclaw/media/comfy/`
    - General Media: `/Users/salmonrk/.openclaw/media/`
- **Project Folder Layout:**
    - `storyboard.md`: Human-readable script.
    - `production.json`: Central database (prompts, paths, status).
    - `outputs/`: Raw assets or symlinks (PNG, MP4, MP3).
    - `final/`: Merged master movies.

## 👥 Character Consistency
Each `production.json` includes a `character_info` block. Sub-agents MUST use the `consistency_prompt` provided in this block as the base for all image generation to ensure character appearance remains stable across scenes.

## 🚀 Production Workflow & Token Efficiency
To ensure high quality and token efficiency, follow this 3-step process for every scene:

### 1. Project Initialization & Template Usage
- Start by creating a new project folder using the structure in `assets/production_template.json`.
- **Token Tip:** Do not read the entire `production.json` into the main chat context. Use `grep`, `tail`, or specific line offsets to fetch only the active scene's data.

### 2. Scene Management & Updates
- **Read Pattern:** When working on a specific scene, only load that scene's object from the JSON.
- **Write Pattern:** Update `production.json` immediately after any asset is generated or status changes. This ensures sub-agents always have the latest state without needing a full chat history replay.
- **Modification:** To edit a scene, read its current entry, propose changes, and apply them using `update_scene.py` or surgical `edit` calls.

### 3. Production Phases
- **Phase 1: Concept & Storyboard:** Define scripts and prompts in `production.json`.
- **Phase 2: Visual Approval (MANDATORY):** Generate images first. Present to user. DO NOT proceed to video until approved.
- **Phase 3: Sub-agent Orchestration:** Spawn a sub-agent for long-running tasks like `ltx2_video`. The sub-agent will:
    1. Read the specific scene data.
    2. Execute the animation.
    3. Update `production.json` with the new file path.
    4. Return a concise success/failure message.

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
