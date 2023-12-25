import os
import subprocess
import argparse


def convert_hevc_to_avc(source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".mp4"):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)

            # Construct the FFmpeg command for conversion
            command = [
                'ffmpeg', '-i', source_file,
                '-c:v', 'libx264', '-c:a', 'copy',
                destination_file
            ]

            # Execute the conversion command
            subprocess.run(command)

            print(f"Converted {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert MP4 files from HEVC to AVC")
    parser.add_argument("source_folder", type=str,
                        help="Path to the source folder containing MP4 files")
    parser.add_argument("destination_folder", type=str,
                        help="Path to the destination folder to save "
                             "converted files")

    args = parser.parse_args()
    convert_hevc_to_avc(args.source_folder, args.destination_folder)


if __name__ == "__main__":
    main()
