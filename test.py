# Read Datas
from pathlib import Path


with open("/home/mohapc/Documents/Projets/Python/Algos/tmps.txt", "r") as f:
    datas = f.read().split("\n")

datas.append("5:00:00 - fin")
infos = [dt.split(" - ", 1) for dt in datas]
infos = [
    (s, e, t)
    for (s, t), (e, _) in zip(infos[:-1], infos[1:])
]
print(*infos, sep='\n')

# parent_path = Path("/home/mohapc/Videos/Youtube/TraversyMedia")
# for f in parent_path.glob("*)"):
#     f.rename(f.with_name(f"{f.name}.mp4"))
