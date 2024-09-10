# Load the video file

from distutils.util import strtobool
import enum
import json
from pathlib import Path
import subprocess
from concurrent.futures import ThreadPoolExecutor


def extract_clip(input_file, nb, output_title, start_time, end_time):
    ext = input_file.suffix
    dt, doc = input_file.stem.split('_', 1)
    doc, c = doc.rsplit(' ', 1)
    doc: Path = input_file.parent / doc
    doc.mkdir(parents=True, exist_ok=True)
    output_file = doc / f"{dt}_{nb:03}_{output_title} {c}{ext}"
    temp_file = input_file.with_stem(f"{output_title}.sub")

    # First pass: fast seeking
    command1 = [
        'ffmpeg',
        '-i', input_file,
        '-ss', start_time,
        '-to', end_time,
        '-c', 'copy',
        temp_file
    ]

    # Second pass: precise cutting
    command2 = [
        'ffmpeg',
        '-i', str(temp_file),
        '-c', 'copy',
        str(output_file),
        "-y"
    ]

    try:
        subprocess.run(command1, check=True)
        subprocess.run(command2, check=True)
        temp_file.unlink()  # Clean up temporary file
        print(f"Clip extracted successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


with open("/home/mohapc/Documents/Projets/Python/.Speed/ft30zcMlFao.json", "r") as f:
    infos = json.load(f)

datas = infos[0]["chapters"]
infos = [dt.values() for dt in datas]
infos = [(i, t, str(s), str(e)) for i, (s, t, e) in enumerate(infos, start=1)]


input_file = Path(
    "/home/mohapc/Videos/Youtube/freecodecamp/20230117_Learn Tailwind CSS – Course for Beginners (ft30zcMlFao).mp4"
)

# extract_clip(input_file, output_file, start_time, end_time)

with ThreadPoolExecutor(10) as executor:
    executor.map(
        lambda args: extract_clip(input_file, *args),
        infos
    )
