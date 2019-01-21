import pathlib

def count_sloc(dir_path):
    sloc = 0
    for path in dir_path.iterdir():
        print(path)
        if path.name.startswith("."):
            continue
        if path.is_dir():
            sloc += count_sloc(path)
            continue
        if path.suffix != ".py":
            continue
        with path.open() as file:
            try:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        sloc += 1
            except UnicodeDecodeError:
                print("korean?",path)
                return sloc
    return sloc

root_path = pathlib.Path(".")
print(f"{count_sloc(root_path)} lines of python code")