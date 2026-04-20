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

### Fase 3: Optimización Condicionada (Breakthrough)
- **RFdiffusion + ProteinMPNN**: ✅ **COMPLETADA**.
- **Hito Parkinson**: 🏆 **PARK_010_3 logrando ipTM 0.811**. Candidato de alta confianza (>0.8).
- **Hito Vitiligo**: 🏆 **JAK3_OPT_2 logrando ipTM 0.848**. Candidato de alta confianza (>0.8).

#### Estado Actual de BioForge:
| Enfermedad | Mejor Candidato | ipTM | Estado |
|---|---|---|---|
| **Vitiligo** | **JAK3_OPT_2** | **0.848** | 🏆 Récord Absoluto |
| **Parkinson** | **PARK_010_3** | **0.811** | 🏆 Récord Parkinson |
| Vitiligo (JAK1) | JAK1_NEW_3 | 0.744 | ✅ Viable |
| Vitiligo (TYRP1) | TYRP1_OPT_8 | 0.626 | ✅ Viable |

> [!NOTE]
> BioForge utiliza ahora una **Matriz de Optimización**: blancos *convergentes* (JAK3/TYRP1) requieren bajar temperatura, mientras que blancos *diversos* (JAK1) requieren rotación de seed.


## 🛠️ Requisitos
- Python 3.10+
- Anthropic API Key (configurada en `.env`)
- Acceso a Google Colab (con T4 GPU habilitada para Fase 2.5)

## 📌 Protocolo de Trabajo
Toda afirmación de éxito en este repositorio debe estar respaldada por:
1. Un log de ejecución crudo en `outputs/`.
2. Una captura de pantalla de la terminal/notebook si se trata de entornos externos.
3. Indicación clara de si se usaron datos reales o simulados.
