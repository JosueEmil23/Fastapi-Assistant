# Expense & Budget Tracker API

API REST de seguimiento de gastos, ingresos y presupuestos mensuales construida con **FastAPI**, **SQLAlchemy 2.0** y **Pydantic v2**, con soporte para SQLite en desarrollo y PostgreSQL en producción, además de un asistente conversacional con *tool calling* y modo *fallback* sin necesidad de clave externa.

---

## Arquitectura del proyecto

El proyecto sigue una separación por capas para mantener cada responsabilidad aislada y fácil de probar:

```text
FastAPI-assistant/
├── app/
│   ├── assistant/     # Orquestador con tool calling y modo fallback
│   ├── routers/       # Endpoints REST (accounts, categories, transactions, budgets, assistant)
│   ├── config.py      # Configuración tipada con pydantic-settings (.env)
│   ├── database.py    # Engine, SessionLocal, Base y dependencia get_db()
│   ├── models.py      # Modelos ORM con SQLAlchemy 2.0 (Numeric para importes)
│   └── schemas.py     # Esquemas de entrada/salida con Pydantic v2
├── tests/           # Pruebas automatizadas con pytest
├── .env.example     # Plantilla de variables de entorno
├── .gitignore
├── requirements.txt
└── README.md
