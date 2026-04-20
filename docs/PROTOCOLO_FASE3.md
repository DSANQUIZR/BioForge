# BioForge — Protocolo Fase 3: Pipeline de Diseño Molecular

## Objetivo
Generar candidatos moleculares con ipTM > 0.6 (viable) o > 0.8 (alta confianza)
contra un blanco proteico de interés terapéutico.

## Paso a paso verificado

### Paso 1 — Identificar el blanco
- Herramienta: UniProt API
- Input: nombre de enfermedad
- Output: UniProt ID de la proteína principal

### Paso 2 — Descargar estructura 3D
- Herramienta: AlphaFold EBI API
- Input: UniProt ID
- Output: archivo .pdb de la proteína completa

### Paso 3 — Extraer dominio funcional
- Herramienta: BioPython PDB
- Input: .pdb completo + rango de residuos del dominio activo
- Output: .pdb del dominio reducido
- Nota: usar literatura para identificar residuos correctos

### Paso 4 — Diseño de secuencias candidatas
- Herramienta: ProteinMPNN
- Parámetros estándar:
  - num_seq_per_target: 10
  - sampling_temp: 0.10 (exploración inicial)
  - seed: cualquiera, documentar para reproducibilidad
- Output: archivo .fa con 10 secuencias + scores

### Paso 5 — Selección de candidatos
- Criterio: seleccionar top 3 por score más bajo (menor = mejor en ProteinMPNN)
- Nota: score ProteinMPNN ≠ afinidad real, solo indica calidad de diseño estructural

### Paso 6 — Scoring de afinidad con Boltz-2
- Herramienta: Boltz-2 GPU
- Parámetros estándar:
  - accelerator: gpu (obligatorio, CPU es 10x más lento y Colab reinicia)
  - recycling_steps: 3
  - sampling_steps: 200
  - diffusion_samples: 1
  - use_msa_server: True
- Input: YAML con secuencia del sitio activo (cadena A) + candidato (cadena B)
- Output: confidence_*.json con scores ipTM, ptm, confidence_score

### Paso 7 — Interpretación de scores
| ipTM | Interpretación |
|------|---------------|
| < 0.4 | Interacción débil — descartar |
| 0.4-0.6 | Moderado — requiere optimización |
| 0.6-0.8 | Viable — candidato para síntesis |
| > 0.8 | Alta confianza — candidato pre-clínico |

### Paso 8 — Optimización iterativa (Matriz de Decisiones)
No todos los blancos responden igual a la temperatura. Aplicar el siguiente flujo:

1. **Intento 1 (Base)**: `temp=0.10` / `seed=42`.
2. **Intento 2 (Refinamiento)**: `temp=0.05` / `seed=42`.
   - **Si ipTM aumenta (>5%)**: El espacio es *convergente*. Probar `temp=0.02` para exprimir afinidad.
   - **Si ipTM NO mejora**: El espacio es *diverso*. Proceder al Intento 3.
3. **Intento 3 (Diversidad)**: `temp=0.10` / `seed=99` (o seed aleatorio).
   - El cambio de seed en espacios diversos es más efectivo que bajar la temperatura.

## Lecciones Críticas: Temperatura vs Seed
| Proteína | Comportamiento | Estrategia Óptima | Mejora lograda |
|----------|----------------|-------------------|----------------|
| JAK3 | Convergente | `temp=0.05` | +8% ipTM |
| JAK1 | Diverso | `seed=99` | +10% ipTM |
| TYRP1 | Convergente | `temp=0.05` | +11% ipTM |
| **Parkinson NAC**| **Diverso** | **Scorear todos** | **+10% ipTM** |

## Resultados verificados BioForge (Abril 2026)

| Enfermedad | Blanco | Temp | Candidato | ipTM | Estado |
|-----------|--------|------|-----------|------|--------|
| Parkinson | SNCA NAC | 0.10 | PARK_010_3 | 0.811 | 🏆 Récord Parkinson |
| Vitiligo | JAK1 | 0.10 | JAK1_NEW_3 | 0.744 | ✅ Nuevo Récord JAK1 |
| Vitiligo | TYRP1 | 0.05 | TYRP1_OPT_8 | 0.626 | ✅ Ahora Viable |
| Vitiligo | JAK3 | 0.05 | JAK3_OPT_2 | 0.848 | 🏆 Récord Absoluto |

## Infraestructura requerida
- Google Colab con GPU T4 (gratuito, límite ~4-6 horas/día)
- Boltz-2: pip install boltz
- ProteinMPNN: git clone github.com/dauparas/ProteinMPNN
- BioPython: pip install biopython
- Costo operativo: $0 (tier gratuito suficiente para Fases 1-3)

## Notas importantes
- Siempre verificar GPU con torch.cuda.is_available() antes de correr Boltz-2
- Instalar dependencias y verificar GPU en la misma sesión para evitar reinicios
- Los resultados de Colab se pierden al reiniciar — descargar JSON inmediatamente
- Verificar siempre en GitHub directamente, no confiar en reportes del agente
