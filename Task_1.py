import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Copy and sort files by extension")
    parser.add_argument('source_dir', type=str, help="Source directory path")
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help="Destination directory path (default is 'dist')")
    return parser.parse_args()

def copy_files_recursively(source, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1][1:]
            dest_dir = os.path.join(dest, file_ext)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.copy(file_path, dest_dir)
        for dir in dirs:
            copy_files_recursively(os.path.join(root, dir), dest)

def main():
    args = parse_args()
    copy_files_recursively(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()
