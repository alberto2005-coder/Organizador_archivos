import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import threading
from organizer import FileOrganizer
from categories import EXTENSION_CATEGORIES

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Archivos")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.selected_folder = tk.StringVar()
        self.create_backup = tk.BooleanVar(value=True)
        self.include_hidden = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        # Título
        title_label = tk.Label(self.root, text="🗂️ Organizador Automático de Archivos",
                               font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=20)

        # Selección de carpeta
        folder_frame = tk.LabelFrame(self.root, text="Seleccionar Carpeta", font=('Arial', 12, 'bold'),
                                     bg='#f0f0f0', padx=10, pady=10)
        folder_frame.pack(pady=10, padx=20, fill='x')
        tk.Entry(folder_frame, textvariable=self.selected_folder, state='readonly', width=60).pack(side='left', padx=10, fill='x', expand=True)
        tk.Button(folder_frame, text="📁 Seleccionar Carpeta", command=self.select_folder,
                  bg='#3498db', fg='white').pack(side='right')

        # Opciones
        options_frame = tk.LabelFrame(self.root, text="Opciones de Organización", font=('Arial', 12, 'bold'),
                                      bg='#f0f0f0', padx=10, pady=10)
        options_frame.pack(pady=10, padx=20, fill='x')
        tk.Checkbutton(options_frame, text="Crear copia de seguridad", variable=self.create_backup, bg='#f0f0f0').pack(anchor='w')
        tk.Checkbutton(options_frame, text="Incluir archivos ocultos", variable=self.include_hidden, bg='#f0f0f0').pack(anchor='w')

        # Botones
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20, padx=20, fill='x')
        self.organize_btn = tk.Button(button_frame, text="🚀 Organizar", command=self.start_organization,
                                      bg='#27ae60', fg='white')
        self.organize_btn.pack(side='left', fill='x', expand=True, padx=5)
        tk.Button(button_frame, text="👁️ Vista Previa", command=self.show_preview,
                  bg='#f39c12', fg='white').pack(side='left', fill='x', expand=True, padx=5)
        tk.Button(button_frame, text="🗑️ Limpiar", command=self.clear_selection,
                  bg='#e74c3c', fg='white').pack(side='left', fill='x', expand=True, padx=5)

        # Barra de progreso
        self.progress_var = tk.DoubleVar()
        ttk.Progressbar(self.root, variable=self.progress_var, maximum=100).pack(pady=10, padx=20, fill='x')
        self.status_label = tk.Label(self.root, text="Listo para organizar archivos", bg='#f0f0f0')
        self.status_label.pack()

    def select_folder(self):
        folder = filedialog.askdirectory(title="Selecciona la carpeta a organizar")
        if folder:
            self.selected_folder.set(folder)

    def start_organization(self):
        if not self.selected_folder.get():
            messagebox.showwarning("Advertencia", "Selecciona una carpeta primero")
            return

        if not messagebox.askyesno("Confirmar", "¿Seguro que quieres organizar los archivos?"):
            return

        self.organize_btn.config(state='disabled')
        thread = threading.Thread(target=self.run_organizer)
        thread.daemon = True
        thread.start()

    def run_organizer(self):
        organizer = FileOrganizer(include_hidden=self.include_hidden.get(),
                                  create_backup_opt=self.create_backup.get())
        moved, errors = organizer.organize(Path(self.selected_folder.get()),
                                           progress_callback=self.progress_var.set,
                                           status_callback=lambda t: self.status_label.config(text=t))
        self.show_results(moved, errors)
        self.organize_btn.config(state='normal')
        self.progress_var.set(0)
        self.status_label.config(text="Organización completada")

    def show_results(self, moved_files, errors):
        results_window = tk.Toplevel(self.root)
        results_window.title("Resultados de Organización")
        text_area = scrolledtext.ScrolledText(results_window, font=('Consolas', 10))
        text_area.pack(fill='both', expand=True)

        text_area.insert(tk.END, f"✅ ORGANIZACIÓN COMPLETADA\n\n")
        for category, count in moved_files.items():
            text_area.insert(tk.END, f"• {category}: {count} archivos\n")

        if errors:
            text_area.insert(tk.END, "\n❌ Errores:\n")
            for e in errors:
                text_area.insert(tk.END, f"- {e}\n")

        text_area.config(state='disabled')

    def show_preview(self):
        folder = self.selected_folder.get()
        if not folder:
            messagebox.showwarning("Advertencia", "Selecciona una carpeta primero")
            return
        folder_path = Path(folder)
        files = [f.name for f in folder_path.iterdir() if f.is_file()]
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Vista Previa")
        text_area = scrolledtext.ScrolledText(preview_window, font=('Consolas', 10))
        text_area.pack(fill='both', expand=True)
        text_area.insert(tk.END, "Archivos detectados:\n\n")
        for f in files[:50]:
            text_area.insert(tk.END, f"- {f}\n")
        if len(files) > 50:
            text_area.insert(tk.END, f"... y {len(files)-50} más\n")
        text_area.config(state='disabled')

    def clear_selection(self):
        self.selected_folder.set("")
        self.progress_var.set(0)
        self.status_label.config(text="Listo para organizar archivos")
