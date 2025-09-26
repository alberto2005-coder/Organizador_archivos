import shutil
from pathlib import Path

def create_backup(folder_path: Path):
    """Crea una carpeta de backup si no existe"""
    backup_path = folder_path / "backup_original"
    if not backup_path.exists():
        backup_path.mkdir()
    return backup_path

def safe_move(src: Path, dest: Path):
    """Mueve un archivo evitando colisiones de nombres"""
    counter = 1
    dest_path = dest
    while dest_path.exists():
        dest_path = dest.with_stem(f"{dest.stem}_{counter}")
        counter += 1
    shutil.move(str(src), str(dest_path))
    return dest_path
