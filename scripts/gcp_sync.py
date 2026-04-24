import os
import subprocess
import sys

"""
BioForge GCP Sync Utility
-------------------------
Este script permite sincronizar los resultados locales de la carpeta outputs/
con el bucket de persistencia en Google Cloud Storage.

Uso:
    python scripts/gcp_sync.py push  -> Sincroniza local a GCP
    python scripts/gcp_sync.py pull  -> Sincroniza GCP a local
"""

DEFAULT_BUCKET = "bioforge-storage"

def run_cmd(cmd):
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando {' '.join(cmd)}: {e}")
        return False

def sync_to_gcp(bucket=DEFAULT_BUCKET):
    print(f"🚀 Sincronizando outputs/ locales hacia gs://{bucket}/outputs/...")
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    
    # -m para paralelo, rsync para solo subir cambios
    cmd = ["gsutil", "-m", "rsync", "-r", "outputs/", f"gs://{bucket}/outputs/"]
    if run_cmd(cmd):
        print("✅ Sincronización exitosa.")

def sync_from_gcp(bucket=DEFAULT_BUCKET):
    print(f"📥 Descargando outputs/ desde gs://{bucket}/outputs/...")
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
        
    cmd = ["gsutil", "-m", "rsync", "-r", f"gs://{bucket}/outputs/", "outputs/"]
    if run_cmd(cmd):
        print("✅ Descarga exitosa.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Se requiere acción [push|pull]")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    if action == "push":
        sync_to_gcp()
    elif action == "pull":
        sync_from_gcp()
    else:
        print(f"Acción desconocida: {action}")
        sys.exit(1)
