import os
import shutil


def organize_folder(target_directory):
    if not os.path.exists(target_directory):
        print(f"Error: The directory '{target_directory}' does not exist.")
        return

    os.chdir(target_directory)
    items = os.listdir(".")
    moved_count = 0

    for item in items:
        if os.path.isdir(item):
            continue

        filename, extension = os.path.splitext(item)
        folder_name = extension[1:].lower().strip() if extension else "others"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        source_path = item
        destination_path = os.path.join(folder_name, item)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {item} -> {folder_name}/")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {item}: {e}")

    print(f"\nTask Complete! Successfully organized {moved_count} files.")


if __name__ == "__main__":
    target_folder = "./messy_folder_test"
    print(f"Starting organization for: {target_folder}\n")
    organize_folder(target_folder)
