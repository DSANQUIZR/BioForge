# BioForge: AI-Driven Drug Discovery Pipeline

Pipeline automatizado para el descubrimiento de moléculas terapéuticas enfocadas en enfermedades neurodegenerativas.

## 🚀 Estado del Proyecto (Protocolo de Transparencia)

Este proyecto se rige por un **Protocolo de Verificación Estándar**. A continuación, el estado real y verificado de cada componente:

### Fase 1: Análisis Genómico y Estructural
- **UniProt/AlphaFold**: ✅ **REAL**. Descarga y mapeo funcional desde APIs oficiales.
- **AlphaGenome SDK**: ⚠️ **MODO SIMULACIÓN**. El sistema utiliza actualmente datos de *fallback* (pregrabados) para las variantes de SNCA, APP y HTT debido a la falta de un servidor gRPC local activo.
- **Claude Clinical Reports**: ✅ **REAL**. Integración funcional vía Anthropic API.

### Fase 2: Diseño Molecular (Binder Design)
- **Binder Generation (EvoDiff)**: ✅ **REAL**. Secuencias generadas en sesión de Colab.
- **Scoring (Boltz-2 / ESMFold)**: ⚠️ **RESULTADOS PRELIMINARES**. Los scores actuales (pLDDT ~47, iPTM ~0.08) fueron obtenidos en entornos CPU con pasos mínimos. No representan la afinidad final optimizada.

### Fase 2.5: Optimización Condicionada (Next Step)
- **RFdiffusion Condicionado**: 🎯 **PENDIENTE**. Notebook `BioForge_Fase2_5.ipynb` listo para ejecución en GPU T4.
- **Scoring de Alta Fidelidad**: 🎯 **PENDIENTE**. Requiere GPU para Boltz-2 con parámetros completos.

## 🛠️ Requisitos
- Python 3.10+
- Anthropic API Key (configurada en `.env`)
- Acceso a Google Colab (con T4 GPU habilitada para Fase 2.5)

## 📌 Protocolo de Trabajo
Toda afirmación de éxito en este repositorio debe estar respaldada por:
1. Un log de ejecución crudo en `outputs/`.
2. Una captura de pantalla de la terminal/notebook si se trata de entornos externos.
3. Indicación clara de si se usaron datos reales o simulados.
