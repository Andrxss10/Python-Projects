from abc import ABC, abstractmethod

# ---- Componente ----
class FileSystemComponent(ABC):
    @abstractmethod
    def show_name(self, indent=0):
        pass


# ---- Hoja ----
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_name(self, indent=0):
        print(" " * indent + f"- {self.name}")


# ---- Composite ----
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_name(self, indent=0):
        print(" " * indent + f"[{self.name}]")
        for child in self.children:
            child.show_name(indent + 2)


# ---- Cliente ----
if __name__ == "__main__":
    # Creamos archivos
    file1 = File("archivo1.txt")
    file2 = File("archivo2.pdf")
    file3 = File("imagen.png")

    # Creamos carpetas
    folder1 = Folder("Documentos")
    folder2 = Folder("Imágenes")

    # Construimos el árbol
    folder1.add(file1)
    folder1.add(file2)

    folder2.add(file3)

    root = Folder("Root")
    root.add(folder1)
    root.add(folder2)

    # Mostramos toda la estructura
    root.show_name()
