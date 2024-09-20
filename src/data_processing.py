import pandas as pd
import chardet

def process_chunk(chunk):
    # lógica para procesar cada chunk
    return chunk

def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']
    except Exception as e:
        print(f"Error al detectar la codificación del archivo: {e}")
        return None

def get_data_from_csv(file_path, chunk_size=10000):
    try:
        encoding = detect_encoding(file_path)
        if encoding is None:
            raise ValueError("No se pudo detectar la codificación del archivo.")

        chunks = []
        for chunk in pd.read_csv(file_path, chunksize=chunk_size, encoding=encoding):
            processed_chunk = process_chunk(chunk)
            chunks.append(processed_chunk)

        data = pd.concat(chunks, ignore_index=True)
        return data
    except pd.errors.EmptyDataError:
        print("El archivo CSV está vacío.")
    except pd.errors.ParserError:
        print("Error al analizar el archivo CSV.")
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    return None
