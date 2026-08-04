import os
import django
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files import File

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotter.settings')
django.setup()

def migrate_media_files():
    media_root = settings.MEDIA_ROOT
    if not os.path.exists(media_root):
        print(f"Media root directory does not exist: {media_root}")
        return

    print(f"Scanning media directory: {media_root}")
    uploaded_count = 0
    skipped_count = 0
    failed_count = 0

    for root, dirs, files in os.walk(media_root):
        for file in files:
            # Skip hidden files and macOS metadata files
            if file.startswith('.') or file == 'Thumbs.db':
                continue

            local_path = os.path.join(root, file)
            # Compute relative path under MEDIA_ROOT
            relative_path = os.path.relpath(local_path, media_root)
            # Standardize paths to forward slashes for Cloudinary storage
            cloudinary_path = relative_path.replace('\\', '/')

            try:
                # Check if file already exists in Cloudinary
                if default_storage.exists(cloudinary_path):
                    print(f"[-] Already exists: {cloudinary_path}")
                    skipped_count += 1
                else:
                    print(f"[+] Uploading: {cloudinary_path} ...")
                    with open(local_path, 'rb') as local_file:
                        default_storage.save(cloudinary_path, File(local_file))
                    print(f"[OK] Uploaded: {cloudinary_path}")
                    uploaded_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to upload {cloudinary_path}: {e}")
                failed_count += 1

    print("\n--- Migration Summary ---")
    print(f"Uploaded: {uploaded_count}")
    print(f"Already existed: {skipped_count}")
    print(f"Failed: {failed_count}")
    print("-------------------------")

if __name__ == '__main__':
    migrate_media_files()
