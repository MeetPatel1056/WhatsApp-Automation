import zipfile
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def extract_zip(zip_path, extract_to):
    """Extract the contents of a zip file into the specified directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            member_path = Path(extract_to) / member

            if member.endswith('/'):
                # Handle name conflict for directories
                member_path = handle_name_conflict(member_path, is_dir=True)
                if not member_path.exists():
                    member_path.mkdir(parents=True, exist_ok=True)
            elif member.lower().endswith('.zip'):
                if not member_path.parent.exists():
                    member_path.parent.mkdir(parents=True, exist_ok=True)

                with zip_ref.open(member) as nested_zip:
                    nested_zip_path = handle_name_conflict(member_path)
                    with zipfile.ZipFile(nested_zip) as nested_zip_ref:
                        for nested_member in nested_zip_ref.namelist():
                            nested_member_path = Path(extract_to) / nested_member
                            nested_member_path = handle_name_conflict(nested_member_path)

                            if nested_member.endswith('/'):
                                # Handle name conflict for nested directories
                                nested_member_path = handle_name_conflict(nested_member_path, is_dir=True)
                                if not nested_member_path.exists():
                                    nested_member_path.mkdir(parents=True, exist_ok=True)
                            else:
                                if not nested_member_path.parent.exists():
                                    nested_member_path.parent.mkdir(parents=True, exist_ok=True)
                                with nested_member_path.open('wb') as target:
                                    target.write(nested_zip_ref.read(nested_member))
            else:
                member_path = handle_name_conflict(member_path)
                if not member_path.parent.exists():
                    member_path.parent.mkdir(parents=True, exist_ok=True)
                with member_path.open('wb') as target:
                    target.write(zip_ref.read(member))

def handle_name_conflict(file_path, is_dir=False):
    """Handle file or directory name conflicts by renaming if necessary."""
    original_path = file_path
    counter = 1

    while file_path.exists():
        if is_dir:
            file_path = original_path.with_name(f"{original_path.name}_{counter}")
        else:
            file_path = original_path.with_stem(f"{original_path.stem}_{counter}")
        counter += 1

    return file_path

def extract_all_into_one_folder(zip_path, output_dir):
    """Extract all contents of a zip file and nested zip files into a single folder."""
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    extract_zip(zip_path, output_dir_path)

def select_zip_and_extract():
    """Select a zip file and an output directory, then extract the zip."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Select the zip file
    zip_path = filedialog.askopenfilename(title="Select the Zip File", filetypes=[("Zip Files", "*.zip")])
    if not zip_path:
        print("No file selected.")
        return

    # Select the output directory
    output_dir = filedialog.askdirectory(title="Select the Output Directory")
    if not output_dir:
        print("No output directory selected.")
        return

    # Extract the selected zip file
    extract_all_into_one_folder(zip_path, output_dir)
    print("Extraction completed.")

if __name__ == '__main__':
    select_zip_and_extract()
