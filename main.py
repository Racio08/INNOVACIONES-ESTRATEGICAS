#!/usr/bin/env python3
"""
PROGRAMA DE SIMULACIONES COMERCIALES
Innovaciones Estratégicas 2025

Autor: Sistema de Simulación Comercial
Versión: 1.0.0
Fecha: Diciembre 2025
"""

import sys
import os
from colorama import Fore, Style, init

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ia_generativa import SimuladorIAGenerativa
from analisis_predictivo import SimuladorAnalisisPredictivo
from omnicanal import SimuladorOmnicanal
from sostenibilidad import SimuladorSostenibilidad

init(autoreset=True)


def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('clear' if os.name != 'nt' else 'cls')


def mostrar_banner():
    """Muestra el banner principal del programa"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║        🚀 SIMULADOR DE INNOVACIONES ESTRATÉGICAS 2025 🚀            ║
║                                                                      ║
║              Programa Integral de Simulaciones Comerciales          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)


def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    menu = f"""
{Fore.YELLOW}┌─────────────────────────────────────────────────────────────────────┐
│                        MENÚ PRINCIPAL                               │
└─────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}

{Fore.GREEN}[1]{Style.RESET_ALL} 🤖 IA Generativa para Ventas y Marketing
     → Chatbots inteligentes, generación de contenido, personalización

{Fore.GREEN}[2]{Style.RESET_ALL} 📊 Análisis Predictivo y Machine Learning
     → Predicción de ventas, comportamiento del cliente, pricing dinámico

{Fore.GREEN}[3]{Style.RESET_ALL} 🌐 Estrategia Omnicanal Integrada
     → Integración de canales, Click & Collect, Live Shopping

{Fore.GREEN}[4]{Style.RESET_ALL} ♻️  Sostenibilidad y Comercio Verde
     → Métricas ESG, economía circular, cadena de suministro verde

{Fore.GREEN}[5]{Style.RESET_ALL} 🎯 EJECUTAR TODAS LAS SIMULACIONES
     → Demo completo de todas las innovaciones estratégicas

{Fore.RED}[0]{Style.RESET_ALL} ❌ Salir del programa

{Fore.CYAN}{'─' * 70}{Style.RESET_ALL}
"""
    print(menu)


def ejecutar_simulacion_ia_generativa():
    """Ejecuta el módulo de IA Generativa"""
    limpiar_pantalla()
    simulador = SimuladorIAGenerativa()
    simulador.ejecutar_simulacion_completa()
    input(f"\n{Fore.CYAN}Presiona Enter para volver al menú principal...{Style.RESET_ALL}")


def ejecutar_simulacion_analisis_predictivo():
    """Ejecuta el módulo de Análisis Predictivo"""
    limpiar_pantalla()
    simulador = SimuladorAnalisisPredictivo()
    simulador.ejecutar_simulacion_completa()
    input(f"\n{Fore.CYAN}Presiona Enter para volver al menú principal...{Style.RESET_ALL}")


def ejecutar_simulacion_omnicanal():
    """Ejecuta el módulo Omnicanal"""
    limpiar_pantalla()
    simulador = SimuladorOmnicanal()
    simulador.ejecutar_simulacion_completa()
    input(f"\n{Fore.CYAN}Presiona Enter para volver al menú principal...{Style.RESET_ALL}")


def ejecutar_simulacion_sostenibilidad():
    """Ejecuta el módulo de Sostenibilidad"""
    limpiar_pantalla()
    simulador = SimuladorSostenibilidad()
    simulador.ejecutar_simulacion_completa()
    input(f"\n{Fore.CYAN}Presiona Enter para volver al menú principal...{Style.RESET_ALL}")


def ejecutar_todas_simulaciones():
    """Ejecuta todas las simulaciones en secuencia"""
    limpiar_pantalla()
    
    print(f"\n{Fore.MAGENTA}{'='*70}")
    print(f"{Fore.MAGENTA}EJECUCIÓN COMPLETA: TODAS LAS INNOVACIONES ESTRATÉGICAS 2025")
    print(f"{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}Se ejecutarán los siguientes módulos en orden:{Style.RESET_ALL}")
    print(f"  1. IA Generativa")
    print(f"  2. Análisis Predictivo")
    print(f"  3. Estrategia Omnicanal")
    print(f"  4. Sostenibilidad y Comercio Verde\n")
    
    confirmacion = input(f"{Fore.CYAN}¿Deseas continuar? (S/N): {Style.RESET_ALL}").strip().upper()
    
    if confirmacion != 'S':
        print(f"{Fore.YELLOW}Operación cancelada.{Style.RESET_ALL}")
        return
    
    # Módulo 1: IA Generativa
    limpiar_pantalla()
    print(f"\n{Fore.CYAN}[1/4] Ejecutando módulo: IA Generativa{Style.RESET_ALL}\n")
    simulador_ia = SimuladorIAGenerativa()
    simulador_ia.ejecutar_simulacion_completa()
    input(f"\n{Fore.YELLOW}Presiona Enter para continuar con el siguiente módulo...{Style.RESET_ALL}")
    
    # Módulo 2: Análisis Predictivo
    limpiar_pantalla()
    print(f"\n{Fore.CYAN}[2/4] Ejecutando módulo: Análisis Predictivo{Style.RESET_ALL}\n")
    simulador_predictivo = SimuladorAnalisisPredictivo()
    simulador_predictivo.ejecutar_simulacion_completa()
    input(f"\n{Fore.YELLOW}Presiona Enter para continuar con el siguiente módulo...{Style.RESET_ALL}")
    
    # Módulo 3: Omnicanal
    limpiar_pantalla()
    print(f"\n{Fore.CYAN}[3/4] Ejecutando módulo: Estrategia Omnicanal{Style.RESET_ALL}\n")
    simulador_omnicanal = SimuladorOmnicanal()
    simulador_omnicanal.ejecutar_simulacion_completa()
    input(f"\n{Fore.YELLOW}Presiona Enter para continuar con el siguiente módulo...{Style.RESET_ALL}")
    
    # Módulo 4: Sostenibilidad
    limpiar_pantalla()
    print(f"\n{Fore.CYAN}[4/4] Ejecutando módulo: Sostenibilidad{Style.RESET_ALL}\n")
    simulador_sostenibilidad = SimuladorSostenibilidad()
    simulador_sostenibilidad.ejecutar_simulacion_completa()
    
    # Resumen final
    limpiar_pantalla()
    print(f"\n{Fore.GREEN}{'='*70}")
    print(f"{Fore.GREEN}✓ SIMULACIÓN COMPLETA FINALIZADA")
    print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n")
    
    print(f"{Fore.CYAN}📊 RESUMEN DE INNOVACIONES ESTRATÉGICAS 2025:{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}✓ IA Generativa:{Style.RESET_ALL} Chatbots, contenido automático, personalización")
    print(f"{Fore.GREEN}✓ Análisis Predictivo:{Style.RESET_ALL} Predicción de ventas, comportamiento, inventario")
    print(f"{Fore.GREEN}✓ Omnicanal:{Style.RESET_ALL} Integración de canales, Click & Collect, Live Shopping")
    print(f"{Fore.GREEN}✓ Sostenibilidad:{Style.RESET_ALL} ESG, economía circular, supply chain verde\n")
    
    print(f"{Fore.MAGENTA}🚀 Impacto proyectado de las innovaciones:")
    print(f"  → Incremento en ventas: +25-40%")
    print(f"  → Mejora en eficiencia operativa: +30-50%")
    print(f"  → Reducción de costos: 15-30%")
    print(f"  → Satisfacción del cliente: +35-45%")
    print(f"  → Reducción huella de carbono: -30-50%{Style.RESET_ALL}\n")
    
    input(f"\n{Fore.CYAN}Presiona Enter para volver al menú principal...{Style.RESET_ALL}")


def main():
    """Función principal del programa"""
    try:
        while True:
            limpiar_pantalla()
            mostrar_banner()
            mostrar_menu_principal()
            
            opcion = input(f"{Fore.YELLOW}Selecciona una opción [0-5]: {Style.RESET_ALL}").strip()
            
            if opcion == '1':
                ejecutar_simulacion_ia_generativa()
            elif opcion == '2':
                ejecutar_simulacion_analisis_predictivo()
            elif opcion == '3':
                ejecutar_simulacion_omnicanal()
            elif opcion == '4':
                ejecutar_simulacion_sostenibilidad()
            elif opcion == '5':
                ejecutar_todas_simulaciones()
            elif opcion == '0':
                limpiar_pantalla()
                print(f"\n{Fore.CYAN}{'='*70}")
                print(f"{Fore.CYAN}Gracias por usar el Simulador de Innovaciones Estratégicas 2025")
                print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
                print(f"{Fore.GREEN}¡Hasta pronto!{Style.RESET_ALL}\n")
                sys.exit(0)
            else:
                print(f"\n{Fore.RED}❌ Opción inválida. Por favor, selecciona una opción del 0 al 5.{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
    
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Programa interrumpido por el usuario.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}¡Hasta pronto!{Style.RESET_ALL}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error inesperado: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Por favor, contacta al administrador del sistema.{Style.RESET_ALL}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
