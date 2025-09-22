import py7zr
import os

def zip(src, dest):
    """Compress a file/folder into a .7z archive."""
    with py7zr.SevenZipFile(dest, 'w') as archive:
        if os.path.isdir(src):
            archive.writeall(src, arcname='.')
        else:
            archive.write(src, arcname=os.path.basename(src))

def unzip(archive, dest):
    """Extract a .7z archive into a folder."""
    with py7zr.SevenZipFile(archive, 'r') as archive_file:
        archive_file.extractall(path=dest)
