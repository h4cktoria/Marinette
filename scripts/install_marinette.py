#!/usr/bin/env python3


from pathlib import PurePath, Path


def gh_init():
    return (
        "s=get_shell\n"
        "hc=s.host_computer\n"
        "gf=function(p);return hc.File(p);end function\n"
        "df=function(p);f=gf(p);if f then f.delete;end function\n"
        "cf=function(p,n);hc.touch(p,n);end function\n"
        "cfl=function(p,n);hc.create_folder(p,n);end function\n"
        "app=function(p,c);f=gf(p);o=f.get_content;f.set_content(o+c+char(10));end function\n"
    )


def delete_file(path):
    file = PurePath(path)
    return f'df("{file}")\n'


def create_file(path):
    file = PurePath(path)
    parent = str(file.parent)
    name = file.name
    return f'cf("{parent}","{name}")\n'


def create_folder(path):
    file = PurePath(path)
    parent = str(file.parent)
    name = file.name
    return f'cfl("{parent}","{name}")\n'


def append(path, content):
    file = PurePath(path)
    return f'app("{path}","{content}")\n'


def create_project_structure_recursively(project_fd, installer_fd, game_path):
    dirs = list(project_fd.iterdir())
    dirs.sort()
    for path in dirs:
        if path.is_dir() and path.name in blacklist:
            continue
        new_path = str(PurePath(game_path) / path.name)
        if path.is_dir():
            installer_fd.write(create_folder(new_path))
            create_project_structure_recursively(path, installer_fd, new_path)
            continue
        installer_fd.write(create_file(new_path))


def write_text_files(project_fd, installer_fd, game_path):
    files = list(project_fd.iterdir())
    files.sort()
    for path in files:
        if path.is_dir():
            continue
        if "LICENSE" in path.name or "README" in path.name:
            installer_fd.write(delete_file(f"/home/guest/Sources/Marinette/{path.name}"))
            installer_fd.write(create_file(f"/home/guest/Sources/Marinette/{path.name}"))
            with open(path.absolute(), "r") as path_fd:
                lines = path_fd.readlines()
                lines = map(lambda line: line.replace("\n", ""), lines)
                lines = map(lambda line: line.replace("\"", "\"\""), lines)
                for line in lines:
                    installer_fd.write(append(f"/home/guest/Sources/Marinette/{path.name}", line))


import src_make_localization
import src_make_themeing


blacklist = ["etc", "locales", "scripts", "themes", "vols"]
filename = Path(__file__).name.replace(".py", ".src")
with open(f"scripts/{filename}", "w") as installer:
    installer.write(gh_init())
    installer.write(create_folder("/home"))
    installer.write(create_folder("/home/guest/Sources"))
    installer.write(create_folder("/home/guest/Sources/Marinette"))

    root = Path(".")
    create_project_structure_recursively(root, installer, "/home/guest/Sources/Marinette")
    write_text_files(root, installer, "/home/guest/Sources/Marinette")
