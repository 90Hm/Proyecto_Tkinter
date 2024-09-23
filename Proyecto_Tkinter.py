import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.events = []
        self.create_widgets()

    def create_widgets(self):
        # Frame para la lista de eventos
        frame_list = tk.Frame(self.root)
        frame_list.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(frame_list, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        frame_entry = tk.Frame(self.root)
        frame_entry.pack(pady=10)

        tk.Label(frame_entry, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(frame_entry)
        self.date_entry.grid(row=0, column=1)

        tk.Label(frame_entry, text="Hora:").grid(row=1, column=0)
        self.time_entry = tk.Entry(frame_entry)
        self.time_entry.grid(row=1, column=1)

        tk.Label(frame_entry, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_entry)
        self.desc_entry.grid(row=2, column=1)

        # Botones para acciones
        tk.Button(frame_entry, text="Agregar Evento", command=self.add_event).grid(row=3, column=0)
        tk.Button(frame_entry, text="Eliminar Evento Seleccionado", command=self.delete_event).grid(row=3, column=1)
        tk.Button(frame_entry, text="Salir", command=self.root.quit).grid(row=3, column=2)

    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.events.append((fecha, hora, descripcion))
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
