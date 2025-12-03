"""
Simulador de Análisis Predictivo para Ventas
Innovación Estratégica 2025
"""
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from colorama import Fore, Style, init

init(autoreset=True)


class SimuladorAnalisisPredictivo:
    """Simula análisis predictivo para optimización comercial"""
    
    def __init__(self):
        self.meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                      'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    def simular_prediccion_ventas(self):
        """Simula predicción de ventas con ML"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Predicción de Ventas con Machine Learning")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        # Generar datos históricos simulados
        print(f"{Fore.YELLOW}Analizando datos históricos de ventas...{Style.RESET_ALL}")
        ventas_historicas = [random.randint(50000, 150000) for _ in range(12)]
        
        print(f"\n{Fore.GREEN}Ventas Históricas (últimos 12 meses):")
        for i, venta in enumerate(ventas_historicas):
            print(f"  {self.meses[i]}: ${venta:,}")
        
        # Predicción próximos 6 meses
        print(f"\n{Fore.YELLOW}Generando predicciones con modelo ML...{Style.RESET_ALL}")
        tendencia = random.uniform(1.05, 1.15)  # Crecimiento 5-15%
        predicciones = []
        
        for i in range(6):
            base = ventas_historicas[-1]
            prediccion = int(base * (tendencia ** (i+1)) * random.uniform(0.95, 1.05))
            predicciones.append(prediccion)
        
        print(f"\n{Fore.GREEN}Predicciones Próximos 6 Meses:")
        meses_futuros = ['Ene+1', 'Feb+1', 'Mar+1', 'Abr+1', 'May+1', 'Jun+1']
        for i, pred in enumerate(predicciones):
            confianza = random.randint(85, 95)
            print(f"  {meses_futuros[i]}: ${pred:,} (Confianza: {confianza}%)")
        
        crecimiento_esperado = ((predicciones[-1] - ventas_historicas[-1]) / ventas_historicas[-1]) * 100
        print(f"\n{Fore.MAGENTA}→ Crecimiento esperado: {crecimiento_esperado:.1f}%")
        print(f"{Fore.MAGENTA}→ Precisión del modelo: {random.randint(88, 96)}%{Style.RESET_ALL}\n")
    
    def simular_comportamiento_cliente(self):
        """Simula análisis predictivo de comportamiento del cliente"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Análisis Predictivo de Comportamiento del Cliente")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        segmentos = [
            {"nombre": "Compradores Frecuentes", "clientes": 450, "riesgo_churn": 12},
            {"nombre": "Clientes Premium", "clientes": 180, "riesgo_churn": 8},
            {"nombre": "Nuevos Clientes", "clientes": 320, "riesgo_churn": 35},
            {"nombre": "Clientes Inactivos", "clientes": 210, "riesgo_churn": 68},
        ]
        
        print(f"{Fore.YELLOW}Analizando segmentos de clientes...\n{Style.RESET_ALL}")
        
        total_en_riesgo = 0
        for segmento in segmentos:
            en_riesgo = int(segmento['clientes'] * segmento['riesgo_churn'] / 100)
            total_en_riesgo += en_riesgo
            
            print(f"{Fore.GREEN}{segmento['nombre']}:")
            print(f"  → Total clientes: {segmento['clientes']}")
            print(f"  → Riesgo de abandono: {segmento['riesgo_churn']}%")
            print(f"  → Clientes en riesgo: {en_riesgo}")
            
            # Recomendación
            if segmento['riesgo_churn'] > 50:
                print(f"  {Fore.RED}⚠ ACCIÓN URGENTE: Campaña de retención inmediata")
            elif segmento['riesgo_churn'] > 30:
                print(f"  {Fore.YELLOW}⚠ Implementar programa de fidelización")
            else:
                print(f"  {Fore.CYAN}✓ Mantener estrategia actual")
            print()
        
        valor_salvado = total_en_riesgo * random.randint(800, 1500)
        print(f"{Fore.MAGENTA}→ Total clientes en riesgo: {total_en_riesgo}")
        print(f"{Fore.MAGENTA}→ Valor potencial a salvar: ${valor_salvado:,}{Style.RESET_ALL}\n")
    
    def simular_optimizacion_inventario(self):
        """Simula optimización de inventario con análisis predictivo"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Optimización de Inventario con IA")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        productos = [
            {"nombre": "Producto A", "stock_actual": 450, "demanda_predicha": 520},
            {"nombre": "Producto B", "stock_actual": 890, "demanda_predicha": 780},
            {"nombre": "Producto C", "stock_actual": 120, "demanda_predicha": 340},
            {"nombre": "Producto D", "stock_actual": 650, "demanda_predicha": 620},
            {"nombre": "Producto E", "stock_actual": 280, "demanda_predicha": 150},
        ]
        
        print(f"{Fore.YELLOW}Analizando niveles de inventario vs demanda predicha...\n{Style.RESET_ALL}")
        
        ahorro_total = 0
        for prod in productos:
            diferencia = prod['demanda_predicha'] - prod['stock_actual']
            porcentaje = (diferencia / prod['stock_actual']) * 100
            
            print(f"{Fore.GREEN}{prod['nombre']}:")
            print(f"  → Stock actual: {prod['stock_actual']} unidades")
            print(f"  → Demanda predicha: {prod['demanda_predicha']} unidades")
            
            if diferencia > 0:
                print(f"  {Fore.RED}⚠ FALTANTE: {diferencia} unidades ({porcentaje:.1f}%)")
                print(f"  {Fore.YELLOW}→ Recomendación: Ordenar {diferencia + 50} unidades inmediatamente")
            elif diferencia < -100:
                exceso = abs(diferencia)
                print(f"  {Fore.YELLOW}⚠ EXCESO: {exceso} unidades ({abs(porcentaje):.1f}%)")
                print(f"  {Fore.CYAN}→ Recomendación: Aplicar promoción o redistribuir")
                ahorro_total += exceso * random.randint(15, 30)
            else:
                print(f"  {Fore.GREEN}✓ ÓPTIMO: Inventario balanceado")
            print()
        
        print(f"{Fore.MAGENTA}→ Ahorro estimado por optimización: ${ahorro_total:,}")
        print(f"{Fore.MAGENTA}→ Reducción de costos de almacenamiento: {random.randint(15, 25)}%{Style.RESET_ALL}\n")
    
    def simular_analisis_precio_dinamico(self):
        """Simula análisis de precios dinámicos"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Pricing Dinámico con IA")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        productos = ["Premium X1", "Standard S2", "Budget B3", "Elite E4"]
        
        print(f"{Fore.YELLOW}Optimizando precios basado en demanda y competencia...\n{Style.RESET_ALL}")
        
        ingresos_adicionales = 0
        for producto in productos:
            precio_actual = random.randint(200, 800)
            demanda_actual = random.randint(100, 500)
            competencia = random.uniform(0.9, 1.15)
            
            # Precio óptimo calculado
            precio_optimo = int(precio_actual * random.uniform(1.05, 1.18))
            aumento = ((precio_optimo - precio_actual) / precio_actual) * 100
            
            print(f"{Fore.GREEN}{producto}:")
            print(f"  → Precio actual: ${precio_actual}")
            print(f"  → Precio óptimo sugerido: ${precio_optimo} (+{aumento:.1f}%)")
            print(f"  → Demanda estimada: {int(demanda_actual * random.uniform(0.95, 1.08))} unidades")
            print(f"  → Elasticidad precio: {random.uniform(0.5, 1.5):.2f}")
            
            ingreso_extra = (precio_optimo - precio_actual) * demanda_actual
            ingresos_adicionales += ingreso_extra
            print(f"  {Fore.MAGENTA}→ Ingreso adicional estimado: ${ingreso_extra:,}\n")
        
        print(f"{Fore.CYAN}Total ingresos adicionales proyectados: ${ingresos_adicionales:,}{Style.RESET_ALL}\n")
    
    def ejecutar_simulacion_completa(self):
        """Ejecuta todas las simulaciones de análisis predictivo"""
        print(f"\n{Fore.MAGENTA}{'*'*70}")
        print(f"{Fore.MAGENTA}MÓDULO: ANÁLISIS PREDICTIVO - INNOVACIÓN 2025")
        print(f"{Fore.MAGENTA}{'*'*70}{Style.RESET_ALL}\n")
        
        self.simular_prediccion_ventas()
        input(f"{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
        
        self.simular_comportamiento_cliente()
        input(f"{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
        
        self.simular_optimizacion_inventario()
        input(f"{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
        
        self.simular_analisis_precio_dinamico()
        
        print(f"\n{Fore.GREEN}✓ Simulación de Análisis Predictivo completada{Style.RESET_ALL}\n")
