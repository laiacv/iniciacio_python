---
name: latex-redlines-protocol
description: Rules and protocols for working with LaTeX files and interaction REDLINES. Use when modifying any file in the workspace, especially LaTeX documents, to ensure strict adherence to safety, research-first, and validation protocols.
---

# Project-Specific LaTeX & Style Protocol

This skill ensures that all interactions and modifications follow a strict set of safety and quality rules designed for the **"La comunicació a través dels sentits"** research project.

## 🔴 REDLINES & Core Protocols
These rules have absolute precedence and must be followed for every task.

### 1. Strict Modification Policy
- **DO NOT MODIFY ANYTHING** that has not been explicitly requested. This includes both style and content.
- **The Preamble is untouchable**, unless an explicit modification is requested.
- **REDLINE:** NEVER ENTER the `avans_3rTrim` folder unless explicitly requested.

### 2. Prior Validation (TO DO Protocol)
- Before applying changes (especially structural or significant content changes), generate a task list (**TO DO**).
- This list must be **validated by the user** before executing any action.

## 🎨 Visual Identity & Formatting Rules
To maintain the "bonic, plain i agradable" style, follow these specific definitions:

### 1. Color Palette (Mandatory)
- **MidnightBlue:** Main chapters (`\chapter`), header lines, and primary accents.
- **RoyalBlue:** Level 2 sections (`\section`).
- **TealBlue:** Level 3 subsections (`\subsection`).
- **CadetBlue:** Level 4 subsubsections (`\subsubsection`).
- **MidnightBlue / TealBlue:** Used for `hyperref` links.

### 2. Typography & Hierarchy
- **Font:** Sans-serif (Helvetica/Arial-like) via `\renewcommand{\familydefault}{\sfdefault}`.
- **Numbering:** Disabled for all levels (`\setcounter{secnumdepth}{0}`).
- **Spacing:** 1.5 line spacing (`\onehalfspacing`) and 2.5cm margins.

### 3. Headers & Footers (`fancyhdr`)
- **Left Header:** `Laia Cabrera Vallejos | Institut Escola Sant Pol de Mar` (Gray, small).
- **Right Header:** Current chapter title in `MidnightBlue`.
- **Footer:** Centered page number.
- **Rule:** The header must be forced on ALL pages, including chapter starts.

### 4. Code Blocks (`listings`)
- Use `codebackground` (light gray/yellowish) for background.
- Keywords in `codeblue` bold, comments in `codegray`.
- Frame: `single`, line numbers: `left`, font: `\ttfamily\footnotesize`.

## ✍️ Writing & Content Guidelines
- **Tone:** Academic, professional, yet clear and accessible.
- **Language:** Catalan (main) with proper `babel` configuration.
- **Consistency:** Ensure any new content fits the existing narrative and logical flow of the research.

## 🔄 Workflow
1. **Analyze:** Read existing files and the `GEMINI.md` project status.
2. **Plan (TO DO):** Propose changes in a TO DO list, specifying which colors/elements will be used.
3. **Wait:** Do not proceed until the user approves the TO DO list.
4. **Execute:** Apply the approved changes surgically.
5. **Validate:** Check for compilation errors and visual consistency.
