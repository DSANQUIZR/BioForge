# BioForge: AI-Driven Drug Discovery Pipeline

Pipeline automatizado para el descubrimiento de moléculas terapéuticas enfocadas en enfermedades neurodegenerativas.

## 🚀 Estado del Proyecto (Protocolo de Transparencia)

Este proyecto se rige por un **Protocolo de Verificación Estándar**. A continuación, el estado real y verificado de cada componente:

### Fase 1: Análisis Genómico y Estructural
- **UniProt/AlphaFold**: ✅ **REAL**. Descarga y mapeo funcional desde APIs oficiales.
- **AlphaGenome SDK**: ⚠️ **MODO SIMULACIÓN**. El sistema utiliza actualmente datos de *fallback* (pregrabados) para las variantes de SNCA, APP y HTT debido a la falta de un servidor gRPC local activo.
- **Claude Clinical Reports**: ✅ **REAL**. Integración funcional vía Anthropic API.

### Fase 2: Diseño Molecular (Binder Design)
- **Binder Generation (EvoDiff)**: ✅ **REAL**. Diseño inicial completado.
- **Scoring (Boltz-2 / ESMFold)**: ✅ **REAL**. Validación completada en GPU Tesla T4.

### Fase 4: De-inmunización y Validación Estructural
- **PyRosetta Design**: ✅ **COMPLETADA**. Refinamiento en anclas MHC-I.
- **Scoring de Variantes (Boltz-2)**: ✅ **REAL**. Validación final de candidatos mutados.

#### Estado Actual de BioForge:
| Enfermedad | Mejor Candidato | ipTM | Inmunogenicidad (MHC-I) | Estado |
|---|---|---|---|---|
| **Vitiligo (JAK1)** | **JAK1_NEW_3_mut** | **0.861** | 🟢 BAJA | 🏆 **NUEVO RÉCORD** |
| **Vitiligo (JAK3)** | **JAK3_OPT_2** | **0.848** | 🟡 MODERADA | 🏆 Récord original |
| **Parkinson** | **PARK_010_3** | **0.811** | 🟡 PENDIENTE | 🏆 Récord Parkinson |
| Vitiligo (JAK3) | JAK3_OPT_2_mut | 0.760 | 🟢 BAJA | ✅ Variante Segura |

> [!IMPORTANT]
> **Hito JAK1/JAK3**: La variante `JAK1_NEW_3_mut` estableció un nuevo récord de afinidad (**0.861**) tras la de-inmunización. Para JAK3, se conservan ambas versiones según se priorice afinidad absoluta o seguridad inmunológica.

> [!IMPORTANT]
> **Lección Vitiligo**: El diseño de una molécula trispecífica fusionada fue descartado tras obtener un **ipTM máximo de 0.380**. La estrategia final validada es la **terapia combinada de 3 péptidos independientes** atacando JAK3, JAK1 y TYRP1 simultáneamente.

> [!NOTE]
> BioForge utiliza una **Matriz de Optimización**: blancos *convergentes* (JAK3/TYRP1) requieren bajar temperatura, mientras que blancos *diversos* (JAK1/Parkinson) requieren rotación de seed y scoring exhaustivo de todos los candidatos.


## 🛠️ Requisitos e Infraestructura
- **Python 3.10+**
- **Anthropic API Key**: Configurada en `.env` para reportes clínicos.
- **Compute**: Google Colab (GPU T4) / Google Cloud Platform (VM A100 para HLB).
- **Persistencia GCP**: Sincronización automática con `gs://bioforge-storage`.

### Sincronización con GCP
Para asegurar la persistencia de los resultados (`outputs/`) entre sesiones de Colab, utilizar el script de sincronización:
```bash
# Para subir resultados al final de la sesión:
python scripts/gcp_sync.py push

# Para recuperar resultados al inicio de una sesión:
python scripts/gcp_sync.py pull
```

## 📌 Protocolo de Trabajo
Toda afirmación de éxito en este repositorio debe estar respaldada por:
1. Un log de ejecución crudo en `outputs/`.
2. Una captura de pantalla de la terminal/notebook si se trata de entornos externos.
3. Indicación clara de si se usaron datos reales o simulados.
