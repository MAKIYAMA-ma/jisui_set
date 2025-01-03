import os
import zipfile
import sys


def zip_subdirectories(directory_path):
    if not os.path.exists(directory_path):
        print(f"指定されたディレクトリが存在しません: {directory_path}")
        return

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            zip_path = os.path.join(directory_path, f"{item}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=item_path)
                        zipf.write(file_path, arcname)
            print(f"圧縮完了: {zip_path}")


def main():
    if len(sys.argv) < 2:
        print("使用方法: python script.py <ディレクトリパス1> [<ディレクトリパス2> ...]")
        sys.exit(1)

    for directory in sys.argv[1:]:
        zip_subdirectories(directory)


if __name__ == "__main__":
    main()
