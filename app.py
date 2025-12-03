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
    """Página principal"""
    return render_template('index.html')

@app.route('/api/ia-generativa')
def api_ia_generativa():
    """API para IA Generativa"""
    data = {
        "titulo": "IA Generativa para Ventas y Marketing",
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
