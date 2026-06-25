# n8n Workflow Cost & Risk Analyzer

## 0. Propósito del proyecto

Este proyecto nace de una investigación previa de oportunidades en comunidades públicas de software B2B/open-source. La señal más fuerte detectada fue que muchos usuarios de **n8n self-hosted** aceptan pagar por software, soporte o features, pero rechazan modelos donde pagan su propia infraestructura y además quedan limitados por ejecuciones/workflows.

El objetivo inicial NO es crear un sustituto de n8n, ni alojar instancias de clientes, ni construir un SaaS complejo desde el día 1.

El objetivo inicial es construir una herramienta local/offline que analice exports JSON de workflows de n8n y genere un informe útil para una auditoría de coste, riesgo y arquitectura.

Producto inicial:

```text
n8n Workflow Cost & Risk Analyzer
```

Promesa:

```text
Sube/exporta tus workflows de n8n y recibe un informe con riesgos de coste, loops, polling, nodos caros, complejidad operativa y recomendaciones de optimización.
```

## 1. Qué problema resuelve

Los usuarios self-hosted tienen dudas como:

- ¿Qué workflows me están generando más riesgo de coste?
- ¿Estoy usando polling cuando debería usar webhooks?
- ¿Tengo loops o chains que pueden disparar miles de ejecuciones?
- ¿Qué workflows usan APIs caras o IA en bucle?
- ¿Me conviene seguir self-hosted, mover algo a cloud, pagar plan o migrar parte a scripts?
- ¿Qué parte de mi automatización es crítica y qué parte es ruido?

La herramienta debe convertir exports JSON de n8n en un informe accionable.

## 2. Qué NO es este proyecto todavía

No construir en esta fase:

- hosting gestionado de n8n;
- plataforma multi-tenant;
- login/usuarios/billing;
- monitorización en tiempo real;
- conexión directa a credenciales de cliente;
- sustituto de n8n;
- marketplace de expertos;
- scraping de nuevas fuentes;
- integraciones externas innecesarias.

Primero se construye un analizador local y testeable.

## 3. MVP v0.1

Entrada:

```text
Carpeta con exports JSON de workflows de n8n
```

Comando esperado:

```bash
python -m n8n_cost_analyzer.cli analyze ./examples/workflows --output report.md
```

Salida:

```text
report.md
```

El informe debe incluir:

1. resumen ejecutivo;
2. inventario de workflows;
3. tipos de nodos y triggers;
4. riesgos de coste;
5. riesgos operativos;
6. workflows más complejos;
7. recomendaciones;
8. score global;
9. apéndice técnico.

## 4. Arquitectura inicial

Estructura recomendada:

```text
n8n-cost-analyzer/
├── README.md
├── pyproject.toml
├── src/
│   └── n8n_cost_analyzer/
│       ├── __init__.py
│       ├── cli.py
│       ├── models.py
│       ├── parser.py
│       ├── rules.py
│       ├── scoring.py
│       ├── recommendations.py
│       ├── report.py
│       └── cost_model.py
├── tests/
│   ├── fixtures/
│   │   ├── simple_webhook_workflow.json
│   │   ├── polling_workflow.json
│   │   ├── loop_http_workflow.json
│   │   ├── ai_workflow.json
│   │   └── invalid_workflow.json
│   ├── test_parser.py
│   ├── test_rules.py
│   ├── test_scoring.py
│   ├── test_report.py
│   └── test_cli.py
└── examples/
    └── workflows/
```

## 5. Módulos

### 5.1 `models.py`

Definir dataclasses puras:

- `N8nWorkflow`
- `N8nNode`
- `WorkflowInventory`
- `RiskFinding`
- `WorkflowRiskReport`
- `AnalysisResult`
- `CostAssumption`

Evitar dependencias externas al principio.

### 5.2 `parser.py`

Responsabilidades:

- leer un JSON de workflow;
- tolerar exports individuales y listas;
- extraer id, name, active, nodes, connections, settings;
- normalizar tipos de nodos;
- no fallar si faltan campos opcionales;
- producir modelos internos.

### 5.3 `rules.py`

Motor de reglas determinista.

Reglas iniciales:

- schedule/polling frecuente;
- HTTP Request dentro de loops;
- SplitInBatches + HTTP Request;
- OpenAI/LLM/AI nodes;
- workflow muy grande;
- workflow sin error handling;
- webhook chains;
- retries agresivos;
- llamadas a APIs externas;
- nodos de base de datos en loops;
- triggers duplicados o múltiples triggers.

Cada regla produce un `RiskFinding` con:

- `rule_id`;
- `severity`: low / medium / high / critical;
- `category`: cost / operational / complexity / reliability / security;
- `workflow_name`;
- `node_names`;
- `message`;
- `recommendation`.

### 5.4 `scoring.py`

Convertir findings en scores:

- `cost_risk_score`: 0–100;
- `operational_risk_score`: 0–100;
- `complexity_score`: 0–100;
- `overall_risk_score`: 0–100.

Mayor score = mayor riesgo.

### 5.5 `recommendations.py`

Generar recomendaciones deterministas:

- cambiar polling por webhooks;
- añadir guardrails a loops;
- añadir rate limits;
- separar workflows críticos;
- estimar coste de nodos IA;
- añadir error workflow;
- revisar triggers frecuentes;
- reducir fan-out;
- añadir alertas de uso.

### 5.6 `report.py`

Generar Markdown.

Secciones mínimas:

```text
# n8n Workflow Cost & Risk Report

## Executive Summary
## Workflow Inventory
## Top Risks
## Cost Risk Findings
## Operational Risk Findings
## Complexity Findings
## Recommendations
## Workflow-Level Details
## Assumptions
## Appendix
```

### 5.7 `cli.py`

CLI mínima:

```bash
python -m n8n_cost_analyzer.cli analyze PATH --output report.md
```

Flags útiles:

```text
--format markdown
--fail-on-critical
--include-low
--cost-model cost_model.yaml
```

## 6. Reglas iniciales concretas

### Rule: frequent schedule trigger

Detectar nodos cuyo tipo o nombre indique schedule/cron/interval y frecuencia menor o igual a 5 minutos.

Resultado:

```text
High cost risk: frequent polling can create high execution volume. Consider webhook/event-based trigger.
```

### Rule: loop + HTTP Request

Si hay nodos tipo SplitInBatches, Loop, Item Lists, Merge o similares combinados con HTTP Request, marcar riesgo.

### Rule: AI/LLM node

Detectar node types o names que incluyan:

```text
openai, ai, llm, anthropic, chatgpt, gpt, model
```

Marcar coste variable.

### Rule: no error workflow

Si workflow settings no contiene error workflow/error handling y hay nodos críticos, marcar riesgo operativo.

### Rule: large workflow

Más de 50 nodos: medium/high complexity.

Más de 100 nodos: critical complexity.

### Rule: possible webhook chain

Si un workflow tiene Webhook y HTTP Request a una URL interna/n8n/webhook, marcar chain risk.

## 7. Tests mínimos

El proyecto debe avanzar test-first.

### Parser

- parsea workflow válido;
- extrae nodos;
- maneja campos opcionales ausentes;
- rechaza JSON inválido con error claro;
- parsea carpeta con múltiples workflows.

### Rules

- detecta polling frecuente;
- detecta loop + HTTP Request;
- detecta AI nodes;
- detecta workflow grande;
- no genera falsos positivos en workflow simple.

### Scoring

- high findings suben score;
- workflow simple tiene score bajo;
- critical findings dominan overall score.

### Report

- genera Markdown no vacío;
- contiene resumen;
- contiene recomendaciones;
- contiene nombres de workflows.

### CLI

- exit 0 con input válido;
- escribe output;
- exit != 0 con input inexistente;
- `--fail-on-critical` falla si hay critical findings.

## 8. Fases de desarrollo

### Fase 0 — Bootstrap

- Crear estructura de proyecto.
- Crear pyproject mínimo.
- Crear fixtures.
- Crear modelos.
- Tests iniciales.

### Fase 1 — Parser

- Implementar parser JSON.
- Tests verdes.

### Fase 2 — Rule engine

- Implementar 5 reglas iniciales.
- Tests verdes.

### Fase 3 — Scoring

- Implementar scoring básico.
- Tests verdes.

### Fase 4 — Report Markdown

- Generar informe útil.
- Tests verdes.

### Fase 5 — CLI

- Ejecutar desde terminal.
- Tests verdes.

### Fase 6 — Ejemplo real

- Crear `examples/workflows` con fixtures.
- Ejecutar CLI.
- Generar `examples/report.md`.

### Fase 7 — Productización ligera

Solo después de que v0.1 funcione:

- añadir `cost_model.yaml`;
- añadir estimaciones de coste;
- añadir export JSON;
- añadir UI simple opcional.

## 9. Definition of Done v0.1

v0.1 está completa cuando:

- se puede analizar una carpeta con workflows JSON;
- se genera `report.md`;
- hay al menos 5 reglas de riesgo;
- hay scoring por workflow;
- hay recomendaciones accionables;
- todos los tests pasan;
- ruff/pyright limpios si están configurados;
- README actualizado.

## 10. Principios

- Offline first.
- No credenciales.
- No llamadas de red.
- No dependencias pesadas.
- No SaaS prematuro.
- Tests antes de ampliar funcionalidad.
- Reglas explicables.
- Output útil para auditoría humana.

## 11. Roadmap posterior

### v0.2

- Cost model configurable.
- Estimación aproximada de ejecuciones.
- Detección más precisa de triggers.
- Report JSON además de Markdown.

### v0.3

- Streamlit o pequeña UI web local.
- Upload ZIP.
- Descarga de informe.

### v0.4

- Comparativa n8n self-hosted vs n8n cloud vs Zapier/Make.
- Plantillas de recomendaciones por segmento.

### v1.0

- SaaS o producto self-service solo si hay clientes/pagos previos por auditorías.

## 12. Comando de validación recomendado

```bash
python -m compileall src tests
pytest -q
ruff check src tests
pyright src tests
```

Si no existe pyright o ruff, no bloquear al principio; priorizar pytest.
