import os
import zipfile
import sys
from send2trash import send2trash  # Windowsのゴミ箱対応


def zip_leaf_directories(directory_path):
    if not os.path.exists(directory_path):
        print(f"指定されたディレクトリが存在しません: {directory_path}")
        return

    for root, dirs, files in os.walk(directory_path, topdown=False):
        if dirs:  # If the directory has subdirectories, skip
            continue

        if files:  # If there are files but no subdirectories, zip it
            zip_path = f"{root}.zip"
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=root)
                    zipf.write(file_path, arcname)

            # Move original directory to trash using send2trash
            try:
                send2trash(root)
            except Exception as e:
                print(f"ディレクトリの移動中にエラーが発生しました: {root}, エラー: {e}")

            print(f"圧縮完了: {zip_path}")


def main():
    """
    Concrete directories to zip recursively.
    Base directories will be moved to Trash.

    Parameters:

    Returns:

    Example:
    """

    if len(sys.argv) < 2:
        print("使用方法: python script.py <ディレクトリパス1> [<ディレクトリパス2> ...]")
        sys.exit(1)

    for directory in sys.argv[1:]:
        zip_leaf_directories(directory)


if __name__ == "__main__":
    main()
