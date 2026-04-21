# Script de extracción de candidatos HLB optimizado
# Basado en el formato verificado de ProteinMPNN en Colab

fa_path = '/content/mpnn_hlb/seqs/C6XHC5_domain.fa'

def parse_mpnn_results(fasta_file):
    with open(fasta_file) as f:
        lines = f.read().strip().split('\n')

    scores_hlb = {}
    seqs_hlb = {}
    current_sample = None

    for line in lines:
        if line.startswith('>') and 'sample' in line:
            # Extraer Sample ID y Score
            try:
                s_id = line.split('sample=')[1].split(',')[0]
                sc = float(line.split('score=')[1].split(',')[0])
                current_sample = s_id
                scores_hlb[s_id] = sc
            except (IndexError, ValueError) as e:
                print(f"⚠️ Error procesando cabecera: {line}")
                current_sample = None
        elif not line.startswith('>') and current_sample:
            # Capturar la secuencia relacionada al último sample ID leído
            seqs_hlb[current_sample] = line.strip()
    
    return seqs_hlb, scores_hlb

if __name__ == "__main__":
    # Este bloque es para testeo o ejecución directa en Colab
    if os.path.exists(fa_path):
        seqs, scores = parse_mpnn_results(fa_path)
        print(f"✅ Extracción completada: {len(seqs)} muestras.")
    else:
        print(f"❌ Archivo no encontrado: {fa_path}")
