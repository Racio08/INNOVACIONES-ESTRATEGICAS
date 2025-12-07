#!/usr/bin/env python3
"""
Aplicación Web - Simulador de Innovaciones Estratégicas 2025
"""
from flask import Flask, render_template, jsonify
import sys
import os
import random

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ia_generativa import SimuladorIAGenerativa
from analisis_predictivo import SimuladorAnalisisPredictivo
from omnicanal import SimuladorOmnicanal
from sostenibilidad import SimuladorSostenibilidad

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal - Innovaciones 2025"""
    return render_template('completo.html')

@app.route('/simulador')
def simulador():
    """Página de simulador interactivo"""
    return render_template('index.html')

@app.route('/api/ia-generativa')
def api_ia_generativa():
    """API para IA Generativa"""
    data = {
        "titulo": "IA Generativa para Ventas y Marketing",
        "balanced_scorecard": {
            "financiera": {
                "nombre": "Perspectiva Financiera",
                "metricas": [
                    {"indicador": "ROI de IA Generativa", "valor": f"{random.randint(350, 500)}%", "variacion": f"+{random.randint(100, 180)}%"},
                    {"indicador": "Reducción de Costos Marketing", "valor": f"${random.randint(150, 250)}K", "variacion": f"-{random.randint(35, 50)}%"},
                    {"indicador": "Incremento de Ventas", "valor": f"+{random.randint(25, 40)}%", "variacion": f"+{random.randint(15, 25)}%"},
                    {"indicador": "Margen de Contribución", "valor": f"{random.randint(45, 65)}%", "variacion": f"+{random.randint(12, 18)}%"}
                ],
                "icono": "💰"
            },
            "clientes": {
                "nombre": "Perspectiva de Clientes",
                "metricas": [
                    {"indicador": "Satisfacción del Cliente (NPS)", "valor": random.randint(75, 90), "variacion": f"+{random.randint(15, 25)} pts"},
                    {"indicador": "Tasa de Conversión", "valor": f"{random.randint(35, 48)}%", "variacion": f"+{random.randint(18, 28)}%"},
                    {"indicador": "Tasa de Retención", "valor": f"{random.randint(80, 92)}%", "variacion": f"+{random.randint(10, 20)}%"},
                    {"indicador": "Personalización de Ofertas", "valor": f"{random.randint(85, 95)}%", "variacion": f"+{random.randint(40, 60)}%"}
                ],
                "icono": "👥"
            },
            "procesos_internos": {
                "nombre": "Perspectiva de Procesos Internos",
                "metricas": [
                    {"indicador": "Tiempo de Respuesta", "valor": f"{random.randint(5, 15)} seg", "variacion": f"-{random.randint(70, 85)}%"},
                    {"indicador": "Consultas Automatizadas", "valor": f"{random.randint(80, 95)}%", "variacion": f"+{random.randint(65, 80)}%"},
                    {"indicador": "Contenido Generado/Día", "valor": random.randint(50, 120), "variacion": f"+{random.randint(300, 500)}%"},
                    {"indicador": "Calidad de Contenido (Score)", "valor": f"{random.randint(85, 95)}/100", "variacion": f"+{random.randint(20, 30)} pts"}
                ],
                "icono": "⚙️"
            },
            "aprendizaje": {
                "nombre": "Perspectiva de Aprendizaje y Crecimiento",
                "metricas": [
                    {"indicador": "Empleados Capacitados en IA", "valor": f"{random.randint(75, 95)}%", "variacion": f"+{random.randint(60, 85)}%"},
                    {"indicador": "Horas de Capacitación", "valor": f"{random.randint(40, 80)}h/año", "variacion": f"+{random.randint(150, 250)}%"},
                    {"indicador": "Modelos IA Implementados", "valor": random.randint(5, 8), "variacion": f"+{random.randint(3, 5)} nuevos"},
                    {"indicador": "Satisfacción del Equipo", "valor": f"{random.randint(82, 92)}%", "variacion": f"+{random.randint(15, 25)}%"}
                ],
                "icono": "📚"
            }
        },
        "chatbot": {
            "consultas_procesadas": random.randint(1000, 5000),
            "tasa_satisfaccion": random.randint(85, 99),
            "tasa_conversion": random.randint(30, 45),
            "ahorro_tiempo": random.randint(60, 80)
        },
        "contenido": {
            "piezas_generadas": random.randint(500, 1500),
            "engagement_promedio": random.randint(65, 95),
            "ahorro_tiempo": random.randint(70, 85),
            "ctr_promedio": round(random.uniform(2.5, 8.5), 2)
        },
        "personalizacion": {
            "ofertas_enviadas": random.randint(2000, 8000),
            "tasa_apertura": random.randint(45, 75),
            "incremento_ventas": random.randint(25, 40),
            "roi": random.randint(300, 500)
        },
        "ejemplos": [
            {
                "tipo": "Chatbot Response",
                "texto": f"Basándome en su perfil, le recomiendo el Smartphone Premium X1 con un descuento del {random.randint(10, 25)}%"
            },
            {
                "tipo": "Email Marketing",
                "texto": "Subject: ¡Oferta Exclusiva Solo Para Ti! 🎁 - Generado automáticamente con engagement predicho del 89%"
            },
            {
                "tipo": "Contenido Social",
                "texto": "Nuevo post Instagram con 850 palabras, 15 hashtags optimizados, CTR estimado: 6.8%"
            }
        ]
    }
    return jsonify(data)

@app.route('/api/analisis-predictivo')
def api_analisis_predictivo():
    """API para Análisis Predictivo"""
    ventas_historicas = [random.randint(50000, 150000) for _ in range(12)]
    tendencia = random.uniform(1.05, 1.15)
    predicciones = [int(ventas_historicas[-1] * (tendencia ** (i+1)) * random.uniform(0.95, 1.05)) for i in range(6)]
    
    data = {
        "titulo": "Análisis Predictivo con Machine Learning",
        "balanced_scorecard": {
            "financiera": {
                "nombre": "Perspectiva Financiera",
                "metricas": [
                    {"indicador": "Ahorro en Gestión de Inventario", "valor": f"${random.randint(180, 320)}K", "variacion": f"-{random.randint(20, 35)}%"},
                    {"indicador": "Reducción de Pérdidas por Churn", "valor": f"${random.randint(450, 750)}K", "variacion": f"-{random.randint(40, 55)}%"},
                    {"indicador": "Optimización de Precios (Ingresos)", "valor": f"+${random.randint(200, 400)}K", "variacion": f"+{random.randint(12, 22)}%"},
                    {"indicador": "ROI de Analytics", "valor": f"{random.randint(280, 420)}%", "variacion": f"+{random.randint(150, 250)}%"}
                ],
                "icono": "💰"
            },
            "clientes": {
                "nombre": "Perspectiva de Clientes",
                "metricas": [
                    {"indicador": "Tasa de Retención Mejorada", "valor": f"{random.randint(85, 94)}%", "variacion": f"+{random.randint(25, 40)}%"},
                    {"indicador": "Precisión en Predicción de Churn", "valor": f"{random.randint(88, 96)}%", "variacion": f"+{random.randint(45, 65)}%"},
                    {"indicador": "Clientes en Riesgo Recuperados", "valor": f"{random.randint(60, 78)}%", "variacion": f"+{random.randint(50, 70)}%"},
                    {"indicador": "Satisfacción por Disponibilidad", "valor": f"{random.randint(82, 93)}%", "variacion": f"+{random.randint(18, 28)}%"}
                ],
                "icono": "👥"
            },
            "procesos_internos": {
                "nombre": "Perspectiva de Procesos Internos",
                "metricas": [
                    {"indicador": "Precisión de Forecasting", "valor": f"{random.randint(90, 97)}%", "variacion": f"+{random.randint(30, 45)}%"},
                    {"indicador": "Tiempo de Análisis", "valor": f"{random.randint(2, 5)} horas", "variacion": f"-{random.randint(80, 92)}%"},
                    {"indicador": "Modelos ML Activos", "valor": random.randint(6, 10), "variacion": f"+{random.randint(5, 8)} nuevos"},
                    {"indicador": "Automatización de Decisiones", "valor": f"{random.randint(70, 88)}%", "variacion": f"+{random.randint(55, 75)}%"}
                ],
                "icono": "⚙️"
            },
            "aprendizaje": {
                "nombre": "Perspectiva de Aprendizaje y Crecimiento",
                "metricas": [
                    {"indicador": "Analistas Certificados en ML", "valor": f"{random.randint(70, 90)}%", "variacion": f"+{random.randint(55, 80)}%"},
                    {"indicador": "Proyectos de Data Science", "valor": random.randint(8, 15), "variacion": f"+{random.randint(6, 12)} nuevos"},
                    {"indicador": "Calidad de Datos (Score)", "valor": f"{random.randint(85, 96)}/100", "variacion": f"+{random.randint(25, 40)} pts"},
                    {"indicador": "Cultura Data-Driven", "valor": f"{random.randint(78, 92)}%", "variacion": f"+{random.randint(40, 60)}%"}
                ],
                "icono": "📚"
            }
        },
        "prediccion_ventas": {
            "ventas_historicas": ventas_historicas,
            "predicciones": predicciones,
            "meses_historicos": ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
            "meses_futuros": ['Ene+1', 'Feb+1', 'Mar+1', 'Abr+1', 'May+1', 'Jun+1'],
            "crecimiento_esperado": round(((predicciones[-1] - ventas_historicas[-1]) / ventas_historicas[-1]) * 100, 1),
            "precision_modelo": random.randint(88, 96)
        },
        "comportamiento_cliente": {
            "segmentos": [
                {"nombre": "Compradores Frecuentes", "clientes": 450, "riesgo_churn": 12, "accion": "Mantener estrategia"},
                {"nombre": "Clientes Premium", "clientes": 180, "riesgo_churn": 8, "accion": "Programa VIP"},
                {"nombre": "Nuevos Clientes", "clientes": 320, "riesgo_churn": 35, "accion": "Programa fidelización"},
                {"nombre": "Clientes Inactivos", "clientes": 210, "riesgo_churn": 68, "accion": "Campaña urgente"}
            ],
            "valor_salvado": random.randint(400000, 800000)
        },
        "inventario": {
            "productos_optimizados": 5,
            "ahorro_estimado": random.randint(50000, 150000),
            "reduccion_costos": random.randint(15, 25)
        },
        "pricing": {
            "incremento_ingresos": random.randint(150000, 350000),
            "productos_optimizados": 4,
            "margen_mejora": random.randint(8, 15)
        }
    }
    return jsonify(data)

@app.route('/api/omnicanal')
def api_omnicanal():
    """API para Estrategia Omnicanal"""
    canales = {
        "Tienda Física": {"ventas": random.randint(150000, 250000), "clientes": random.randint(300, 800)},
        "E-commerce": {"ventas": random.randint(180000, 280000), "clientes": random.randint(400, 900)},
        "App Móvil": {"ventas": random.randint(120000, 220000), "clientes": random.randint(250, 700)},
        "Redes Sociales": {"ventas": random.randint(80000, 180000), "clientes": random.randint(200, 600)},
        "Marketplace": {"ventas": random.randint(100000, 200000), "clientes": random.randint(220, 650)}
    }
    
    data = {
        "titulo": "Estrategia Omnicanal Integrada",
        "balanced_scorecard": {
            "financiera": {
                "nombre": "Perspectiva Financiera",
                "metricas": [
                    {"indicador": "Ventas Totales Integradas", "valor": f"${random.randint(800, 1200)}K", "variacion": f"+{random.randint(30, 45)}%"},
                    {"indicador": "Sinergia entre Canales", "valor": f"+${random.randint(200, 350)}K", "variacion": f"+{random.randint(35, 50)}%"},
                    {"indicador": "Ticket Promedio Cross-canal", "valor": f"${random.randint(180, 280)}", "variacion": f"+{random.randint(25, 40)}%"},
                    {"indicador": "ROI de Integración Omnicanal", "valor": f"{random.randint(320, 480)}%", "variacion": f"+{random.randint(200, 300)}%"}
                ],
                "icono": "💰"
            },
            "clientes": {
                "nombre": "Perspectiva de Clientes",
                "metricas": [
                    {"indicador": "NPS Experiencia Omnicanal", "valor": random.randint(72, 88), "variacion": f"+{random.randint(22, 35)} pts"},
                    {"indicador": "Customer Journey Exitosos", "valor": f"{random.randint(78, 92)}%", "variacion": f"+{random.randint(40, 60)}%"},
                    {"indicador": "Clientes Multi-canal", "valor": f"{random.randint(55, 75)}%", "variacion": f"+{random.randint(35, 55)}%"},
                    {"indicador": "Tasa de Conversión Integrada", "valor": f"{random.randint(14, 20)}%", "variacion": f"+{random.randint(45, 65)}%"}
                ],
                "icono": "👥"
            },
            "procesos_internos": {
                "nombre": "Perspectiva de Procesos Internos",
                "metricas": [
                    {"indicador": "Integración de Sistemas", "valor": f"{random.randint(88, 98)}%", "variacion": f"+{random.randint(60, 85)}%"},
                    {"indicador": "Tiempo de Fulfillment", "valor": f"{random.randint(18, 36)} horas", "variacion": f"-{random.randint(35, 50)}%"},
                    {"indicador": "Sincronización de Inventario", "valor": f"{random.randint(92, 99)}%", "variacion": f"+{random.randint(40, 60)}%"},
                    {"indicador": "Touchpoints Optimizados", "valor": f"{random.randint(12, 18)}", "variacion": f"+{random.randint(8, 12)} nuevos"}
                ],
                "icono": "⚙️"
            },
            "aprendizaje": {
                "nombre": "Perspectiva de Aprendizaje y Crecimiento",
                "metricas": [
                    {"indicador": "Personal Multi-capacitado", "valor": f"{random.randint(75, 92)}%", "variacion": f"+{random.randint(50, 75)}%"},
                    {"indicador": "Competencias Digitales", "valor": f"{random.randint(80, 94)}/100", "variacion": f"+{random.randint(35, 50)} pts"},
                    {"indicador": "Innovaciones Implementadas", "valor": random.randint(6, 12), "variacion": f"+{random.randint(5, 10)} nuevas"},
                    {"indicador": "Cultura Customer-Centric", "valor": f"{random.randint(82, 95)}%", "variacion": f"+{random.randint(30, 45)}%"}
                ],
                "icono": "📚"
            }
        },
        "canales": canales,
        "totales": {
            "ventas": sum(c["ventas"] for c in canales.values()),
            "clientes": sum(c["clientes"] for c in canales.values()),
            "sinergia": random.randint(25, 40)
        },
        "experiencia_360": {
            "journeys_exitosos": random.randint(1200, 2500),
            "tasa_conversion": round(random.uniform(12, 18), 1),
            "nps": random.randint(65, 82),
            "touchpoints_promedio": round(random.uniform(3.5, 6.2), 1)
        },
        "click_collect": {
            "ordenes": random.randint(150, 350),
            "valor_total": random.randint(180000, 350000),
            "trafico_adicional": random.randint(30, 50),
            "cross_sell_rate": random.randint(40, 65)
        },
        "live_shopping": {
            "eventos": 3,
            "espectadores_total": random.randint(8000, 12000),
            "ventas_total": random.randint(250000, 450000),
            "roi": random.randint(200, 350)
        }
    }
    return jsonify(data)

@app.route('/api/sostenibilidad')
def api_sostenibilidad():
    """API para Sostenibilidad"""
    data = {
        "titulo": "Sostenibilidad y Comercio Verde",
        "balanced_scorecard": {
            "financiera": {
                "nombre": "Perspectiva Financiera",
                "metricas": [
                    {"indicador": "Ahorro en Cadena Verde", "valor": f"${random.randint(220, 380)}K", "variacion": f"-{random.randint(28, 42)}%"},
                    {"indicador": "Ingresos Línea Sostenible", "valor": f"+${random.randint(350, 550)}K", "variacion": f"+{random.randint(45, 70)}%"},
                    {"indicador": "Premium Price Productos Eco", "valor": f"+{random.randint(12, 22)}%", "variacion": f"+{random.randint(8, 15)}%"},
                    {"indicador": "ROI Inversión Verde", "valor": f"{random.randint(250, 380)}%", "variacion": f"+{random.randint(180, 280)}%"}
                ],
                "icono": "💰"
            },
            "clientes": {
                "nombre": "Perspectiva de Clientes",
                "metricas": [
                    {"indicador": "Consumidores Conscientes", "valor": f"{random.randint(42, 58)}%", "variacion": f"+{random.randint(30, 45)}%"},
                    {"indicador": "Lealtad Productos Eco", "valor": f"{random.randint(78, 92)}%", "variacion": f"+{random.randint(35, 50)}%"},
                    {"indicador": "NPS Iniciativas Sostenibles", "valor": random.randint(75, 90), "variacion": f"+{random.randint(25, 38)} pts"},
                    {"indicador": "Preferencia de Marca Verde", "valor": f"{random.randint(65, 82)}%", "variacion": f"+{random.randint(40, 60)}%"}
                ],
                "icono": "👥"
            },
            "procesos_internos": {
                "nombre": "Perspectiva de Procesos Internos",
                "metricas": [
                    {"indicador": "Reducción Emisiones CO2", "valor": f"-{random.randint(35, 52)}%", "variacion": f"-{random.randint(25, 40)}%"},
                    {"indicador": "Energía Renovable", "valor": f"{random.randint(55, 80)}%", "variacion": f"+{random.randint(40, 65)}%"},
                    {"indicador": "Economía Circular (Tasa)", "valor": f"{random.randint(48, 68)}%", "variacion": f"+{random.randint(35, 55)}%"},
                    {"indicador": "Certificaciones Sostenibles", "valor": random.randint(6, 10), "variacion": f"+{random.randint(4, 7)} nuevas"}
                ],
                "icono": "⚙️"
            },
            "aprendizaje": {
                "nombre": "Perspectiva de Aprendizaje y Crecimiento",
                "metricas": [
                    {"indicador": "Cultura de Sostenibilidad", "valor": f"{random.randint(80, 94)}%", "variacion": f"+{random.randint(50, 75)}%"},
                    {"indicador": "Capacitación en ESG", "valor": f"{random.randint(65, 88)}%", "variacion": f"+{random.randint(45, 70)}%"},
                    {"indicador": "Proyectos de Innovación Verde", "valor": random.randint(8, 14), "variacion": f"+{random.randint(6, 11)} nuevos"},
                    {"indicador": "Compromiso del Equipo", "valor": f"{random.randint(85, 96)}/100", "variacion": f"+{random.randint(30, 45)} pts"}
                ],
                "icono": "📚"
            }
        },
        "esg": {
            "environmental": {
                "reduccion_co2": random.randint(15, 35),
                "energia_renovable": random.randint(40, 75),
                "residuos_reciclados": random.randint(60, 85),
                "score": random.randint(75, 92)
            },
            "social": {
                "satisfaccion_empleados": random.randint(80, 95),
                "diversidad": random.randint(45, 65),
                "capacitacion_horas": random.randint(40, 80),
                "score": random.randint(70, 88)
            },
            "governance": {
                "transparencia": random.randint(85, 98),
                "compliance": random.randint(90, 100),
                "score": random.randint(82, 96)
            },
            "score_total": random.randint(75, 90)
        },
        "economia_circular": {
            "productos_recuperados": random.randint(7000, 10000),
            "valor_recuperado": random.randint(180000, 280000),
            "reduccion_desperdicio": random.randint(40, 60),
            "programas_activos": 4
        },
        "supply_chain_verde": {
            "reduccion_emisiones": random.randint(35, 50),
            "ahorro_anual": random.randint(150000, 350000),
            "roi_meses": random.randint(18, 36),
            "iniciativas": 4
        },
        "consumidor_consciente": {
            "segmento_porcentaje": random.randint(35, 50),
            "premium_price": random.randint(10, 20),
            "incremento_lealtad": random.randint(30, 45)
        }
    }
    return jsonify(data)

@app.route('/api/resumen-completo')
def api_resumen_completo():
    """API para resumen de todas las innovaciones"""
    data = {
        "titulo": "Resumen Ejecutivo - Innovaciones Estratégicas 2025",
        "impacto_global": {
            "incremento_ventas": f"+{random.randint(25, 40)}%",
            "mejora_eficiencia": f"+{random.randint(30, 50)}%",
            "reduccion_costos": f"{random.randint(15, 30)}%",
            "satisfaccion_cliente": f"+{random.randint(35, 45)}%",
            "reduccion_co2": f"-{random.randint(30, 50)}%"
        },
        "roi_proyectado": {
            "anio_1": random.randint(200, 350),
            "anio_2": random.randint(400, 650),
            "anio_3": random.randint(700, 1100)
        },
        "modulos_implementados": [
            {
                "nombre": "IA Generativa",
                "icono": "🤖",
                "beneficios": ["Automatización 80%", "Conversión +35%", "ROI 400%"]
            },
            {
                "nombre": "Análisis Predictivo",
                "icono": "📊",
                "beneficios": ["Precisión 92%", "Ahorro $200K", "Churn -45%"]
            },
            {
                "nombre": "Omnicanal",
                "icono": "🌐",
                "beneficios": ["Sinergia +35%", "NPS 75", "Cross-sell 60%"]
            },
            {
                "nombre": "Sostenibilidad",
                "icono": "♻️",
                "beneficios": ["ESG Score 85", "CO2 -40%", "Lealtad +40%"]
            }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n🚀 Servidor iniciado en http://localhost:{port}")
    print(f"📱 Abre tu navegador en: http://localhost:{port}\n")
    app.run(host='0.0.0.0', port=port, debug=True)
