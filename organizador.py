"""Organiza los archivos de una carpeta en subcarpetas segun su extension."""

import argparse
import shutil
from pathlib import Path

CATEGORIAS = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
}


def clasificar(archivo: Path) -> str:
    """Determina la categoria de un archivo segun su extension.

    Args:
        archivo: Ruta del archivo a clasificar.

    Returns:
        Nombre de la categoria correspondiente, u "Otros" si la
        extension no esta registrada.
    """
    return CATEGORIAS.get(archivo.suffix.lower(), "Otros")


def organizar_carpeta(carpeta: Path, simulacion: bool = False) -> int:
    """Organiza los archivos de una carpeta en subcarpetas por categoria.

    Args:
        carpeta: Carpeta cuyos archivos se van a organizar.
        simulacion: Si es True, solo muestra que haria sin mover archivos.

    Returns:
        Numero de archivos movidos (o que se moverian, en modo
        simulacion).
    """
    movidos = 0
    for archivo in carpeta.iterdir():
        if archivo.is_dir() or archivo.name.startswith("."):
            continue

        categoria = clasificar(archivo)
        destino_carpeta = carpeta / categoria
        destino = destino_carpeta / archivo.name

        if simulacion:
            print(f"[SIMULACION] {archivo.name} -> {categoria}")
        else:
            destino_carpeta.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(destino))
            print(f"Movido: {archivo.name} -> {categoria}")

        movidos += 1

    return movidos


def main() -> None:
    """Punto de entrada de linea de comandos del organizador."""
    parser = argparse.ArgumentParser(description="Organiza archivos por tipo.")
    parser.add_argument("carpeta", type=Path, help="Carpeta a organizar")
    parser.add_argument(
        "--dry-run", action="store_true", help="Solo simula, no mueve archivos"
    )
    args = parser.parse_args()

    total = organizar_carpeta(args.carpeta, simulacion=args.dry_run)
    print(f"Total de archivos procesados: {total}")


if __name__ == "__main__":
    main()