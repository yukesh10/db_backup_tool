import gzip
import shutil
import os

def compress_backup(backup_file):
    compressed_file = f"{backup_file}.gz"
    with open(backup_file, 'rb') as f_in:
        with gzip.open(compressed_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(backup_file)