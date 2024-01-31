#!/usr/bin/env python3


from pathlib import PurePath, Path


def delete_file(path):
    file = PurePath(path)
    return (
        f'file = get_shell.host_computer.File("{file}")\n'
        f'if file then file.delete\n'
    )


def create_file(path):
    file = PurePath(path)
    parent = str(file.parent)
    name = file.name
    return f'get_shell.host_computer.touch("{parent}", "{name}")\n'


def create_folder(path):
    file = PurePath(path)
    parent = str(file.parent)
    name = file.name
    return f'get_shell.host_computer.create_folder("{parent}", "{name}")\n'


def append(path, content):
    file = PurePath(path)
    return (
        f'file = get_shell.host_computer.File("{path}")\n'
        f'old = file.get_content\n'
        f'file.set_content(old + "{content}" + char(10))\n'
    )


if __name__ == "__main__":
    fn = Path(__file__).name.replace(".py", ".src")
    with open(f"scripts/{fn}", "w") as script_file:
        script_file.write(create_folder("/home/guest/Sources/Marinette"))
        script_file.write(create_folder("/home/guest/Sources/Marinette/src"))
        
        script_file.write(delete_file("/home/guest/Sources/Marinette/LICENSE"))
        script_file.write(create_file("/home/guest/Sources/Marinette/LICENSE"))

        with open("LICENSE", "r") as license_file:
            for line in map(lambda line: line.replace("\n", ""), license_file.readlines()):
                script_file.write(append("/home/guest/Sources/Marinette/LICENSE", line))

        for src in Path("src").iterdir():
            script_file.write(create_file(f"/home/guest/Sources/Marinette/src/{src.name}"))
