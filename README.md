# NinjaZipPy

A lightweight Python utility to zip and unzip .7z archives from the terminal. 🐍

This project is a migration of the bit7z C++ repository into Python, using LLM-assisted development.

-----

## ✨ Features

  - 📦 Compress files or folders into .7z archives.
  - 📂 Extract .7z archives into folders.
  - ⚡ Simple command-line interface (CLI).
  - 🐍 Implemented in pure Python using `py7zr`.

-----

## 📥 Installation

Clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/Mechdeta/ninjazypy.git
cd ninjazypy
pip install -e .
```

-----

## 🚀 Usage

Once installed, you can use `ninjazypy` directly from your terminal.

### Zip a Folder

```bash
ninjazypy zip <input_folder> <output_archive.7z>
```

**Example:**

```bash
ninjazypy zip my_documents archive.7z
```

### Unzip an Archive

```bash
ninjazypy unzip <input_archive.7z> <output_folder>
```

**Example:**

```bash
ninjazypy unzip archive.7z extracted_files
```

-----

## 📂 Project Structure

```
ninjazypy/
│
├── __init__.py
├── core.py         # Core logic for zipping and unzipping
└── cli.py          # Command-line interface logic
```

-----

## 🛠️ Design Choices

  - **Library**: Uses the popular and reliable `py7zr` library for all .7z archive handling.
  - **Modularity**: Functionality is split into `core.py` for the main logic and `cli.py` for the user-facing CLI, making the code easier to maintain and understand.
  - **Packaging**: Set up as a proper Python package with `pyproject.toml`, allowing for easy installation via `pip`.

-----

## ⚠️ Limitations

  - **Basic Functionality**: Only core zip and unzip features are implemented. It does not include the full feature set of the original C++ `bit7z` library.
  - **Testing**: Primarily tested on Windows, but it is expected to work on Unix-based systems (Linux, macOS) as well.
  - **Tests**: The original C++ unit tests were not migrated to Python.
