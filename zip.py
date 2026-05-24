import zipfile
import os

# ============================================
# CONFIGURATION — Change these paths if needed
# ============================================
PROJECT_DIR = r'C:\AI_Developer\Project_of_ai3\Project_of_ai\tubemind'
OUTPUT_ZIP  = r'C:\AI_Developer\Project_of_ai3\Project_of_ai\tubemind.zip'

# Folders and files to exclude from ZIP
EXCLUDE_DIRS = {
    '__pycache__', '.git', 'venv', 'env',
    '.env', 'node_modules', '.idea', '.vscode'
}
EXCLUDE_EXTS = {'.pyc', '.pyo', '.log', '.sqlite3'}

# ============================================


def create_zip():
    if not os.path.exists(PROJECT_DIR):
        print(f"ERROR: Project folder not found: {PROJECT_DIR}")
        print("Please update PROJECT_DIR in this script.")
        return

    print(f"Creating ZIP from: {PROJECT_DIR}")
    print(f"Output ZIP:        {OUTPUT_ZIP}")
    print("-" * 50)

    file_count = 0

    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(PROJECT_DIR):

            # Remove excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                # Skip excluded extensions
                if any(file.endswith(ext) for ext in EXCLUDE_EXTS):
                    continue

                full_path = os.path.join(root, file)

                # Create archive name with forward slashes (Linux compatible)
                rel_path = os.path.relpath(full_path, PROJECT_DIR)
                arc_name = rel_path.replace('\\', '/')

                zf.write(full_path, arc_name)
                print(f"  Added: {arc_name}")
                file_count += 1

    print("-" * 50)
    print(f"SUCCESS! {file_count} files added to ZIP.")
    print(f"ZIP saved at: {OUTPUT_ZIP}")
    print()
    print("Next steps:")
    print("  1. Upload to S3:")
    print(f"     aws s3 cp {OUTPUT_ZIP} s3://tubemind/tubemind.zip")
    print("  2. Deploy in Elastic Beanstalk")


if __name__ == '__main__':
    create_zip()