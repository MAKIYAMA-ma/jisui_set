import os
import zipfile
import shutil
from PIL import Image


def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def convert_webp_to_jpg(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.webp'):
                webp_path = os.path.join(root, file)
                jpg_path = os.path.splitext(webp_path)[0] + '.jpg'
                with Image.open(webp_path) as img:
                    img.convert('RGB').save(jpg_path, 'JPEG')
                os.remove(webp_path)


def zip_directory(directory, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))


def process_zip_in_directory(input_path):
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                extract_to = os.path.splitext(zip_path)[0]
                unzip_file(zip_path, extract_to)
                convert_webp_to_jpg(extract_to)
                os.remove(zip_path)
                zip_directory(extract_to, zip_path)
                shutil.rmtree(extract_to)


def process_zip_recursively(input_path):
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                extract_to = os.path.splitext(zip_path)[0]
                unzip_file(zip_path, extract_to)
                convert_webp_to_jpg(extract_to)
                os.remove(zip_path)
                zip_directory(extract_to, zip_path)
                shutil.rmtree(extract_to)
            if file.endswith('.webp'):
                webp_path = os.path.join(root, file)
                jpg_path = os.path.splitext(webp_path)[0] + '.jpg'
                with Image.open(webp_path) as img:
                    img.convert('RGB').save(jpg_path, 'JPEG')
                os.remove(webp_path)


if __name__ == "__main__":
    """
    Change webp files to jpeg format.
    If webp files are in zip files, they are also target to changing format.

    Parameters:

    Returns:

    Example:
    """

    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_directory> [<path_to_directory 2> ...]")
        sys.exit(1)

    for input_directory in sys.argv[1:]:
        process_zip_recursively(input_directory)

    print("Processing completed.")
