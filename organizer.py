import shutil
from pathlib import Path
from categories import EXTENSION_CATEGORIES
from utils import create_backup, safe_move

class FileOrganizer:
    def __init__(self, include_hidden=False, create_backup_opt=True):
        self.include_hidden = include_hidden
        self.create_backup_opt = create_backup_opt

    def get_file_category(self, file_path: Path):
        """Determina la categoría de un archivo por extensión"""
        extension = file_path.suffix.lower()
        for category, extensions in EXTENSION_CATEGORIES.items():
            if extension in extensions:
                return category
        return "Otros"

    def organize(self, folder_path: Path, progress_callback=None, status_callback=None):
        moved_files = {}
        errors = []

        if self.create_backup_opt:
            create_backup(folder_path)

        files_to_process = [
            f for f in folder_path.iterdir()
            if f.is_file() and (self.include_hidden or not f.name.startswith('.'))
        ]
        total_files = len(files_to_process)

        for i, file_path in enumerate(files_to_process):
            try:
                category = self.get_file_category(file_path)
                dest_folder = folder_path / category
                dest_folder.mkdir(exist_ok=True)

                dest_path = dest_folder / file_path.name
                final_path = safe_move(file_path, dest_path)

                moved_files[category] = moved_files.get(category, 0) + 1

                if progress_callback:
                    progress_callback((i + 1) / total_files * 100)
                if status_callback:
                    status_callback(f"Procesando: {file_path.name}")

            except Exception as e:
                errors.append(f"Error con {file_path.name}: {str(e)}")

        return moved_files, errors
