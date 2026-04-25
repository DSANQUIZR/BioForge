# BioForge — GCP Persistence Layer
# Project: ringed-cell-480121-n3
# Bucket:  gs://bioforge-storage-dsanquiz
# Fecha:   2026-04-24

import os, subprocess, json

PROJECT_ID = "ringed-cell-480121-n3"
BUCKET     = "bioforge-storage-dsanquiz"

def autenticar_colab():
    """Autenticar GCP desde Google Colab"""
    from google.colab import auth
    auth.authenticate_user()
    subprocess.run(['gcloud', 'config', 'set', 'project', PROJECT_ID],
                   capture_output=True)
    print(f"✅ Autenticado — Proyecto: {PROJECT_ID}")

def guardar_a_gcp(archivos, carpeta="sesiones"):
    for archivo in archivos:
        if os.path.exists(archivo):
            dest = f'gs://{BUCKET}/{carpeta}/{os.path.basename(archivo)}'
            r = subprocess.run(['gsutil', 'cp', archivo, dest],
                              capture_output=True, text=True)
            print(f"{'✅' if r.returncode==0 else '❌'} {os.path.basename(archivo)} → GCP")

def cargar_de_gcp(archivos, destino='/content', carpeta="sesiones"):
    for archivo in archivos:
        src = f'gs://{BUCKET}/{carpeta}/{archivo}'
        r = subprocess.run(['gsutil', 'cp', src, f'{destino}/{archivo}'],
                          capture_output=True, text=True)
        print(f"{'✅' if r.returncode==0 else '⚠️ no encontrado'} {archivo} ← GCP")

def restaurar_sesion():
    """Ejecutar al inicio de cada sesión Colab"""
    print("Restaurando sesión desde GCP...")
    cargar_de_gcp([
        'P37840.pdb', 'P52333.pdb', 'P23458.pdb', 'P17643.pdb'
    ], carpeta="estructuras")
    cargar_de_gcp([
        'candidatos_verificados.json'
    ], carpeta="sesiones")

def sincronizar_todo():
    """Sincronizar /content completo a GCP"""
    r = subprocess.run([
        'gsutil', '-m', 'rsync', '-r',
        '/content/', f'gs://{BUCKET}/colab-content/'
    ], capture_output=True, text=True)
    print(f"{'✅' if r.returncode==0 else '❌'} /content sincronizado")

def listar_gcp():
    """Ver archivos en GCP"""
    r = subprocess.run(['gsutil', 'ls', '-r', f'gs://{BUCKET}/'],
                      capture_output=True, text=True)
    print(r.stdout)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "push":   sincronizar_todo()
        elif sys.argv[1] == "pull": restaurar_sesion()
        elif sys.argv[1] == "list": listar_gcp()
    else:
        print(f"Uso: python gcp_sync.py [push|pull|list]")
        print(f"Bucket: gs://{BUCKET}")
