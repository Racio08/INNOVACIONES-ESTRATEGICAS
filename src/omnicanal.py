"""
Simulador de Estrategia Omnicanal
Innovación Estratégica 2025
"""
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)


class SimuladorOmnicanal:
    """Simula estrategias omnicanal integradas"""
    
    def __init__(self):
        self.canales = {
            "Tienda Física": {"ventas": 0, "clientes": 0},
            "E-commerce": {"ventas": 0, "clientes": 0},
            "App Móvil": {"ventas": 0, "clientes": 0},
            "Redes Sociales": {"ventas": 0, "clientes": 0},
            "Marketplace": {"ventas": 0, "clientes": 0}
        }
    
    def simular_integracion_canales(self):
        """Simula integración de múltiples canales de venta"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Integración Omnicanal de Ventas")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}Simulando actividad en diferentes canales...\n{Style.RESET_ALL}")
        
        # Simular transacciones en cada canal
        for canal in self.canales:
            time.sleep(0.3)
            ventas = random.randint(50000, 250000)
            clientes = random.randint(100, 800)
            ticket_promedio = ventas // clientes
            
            self.canales[canal]["ventas"] = ventas
            self.canales[canal]["clientes"] = clientes
            
            print(f"{Fore.GREEN}{canal}:")
            print(f"  → Ventas: ${ventas:,}")
            print(f"  → Clientes atendidos: {clientes}")
            print(f"  → Ticket promedio: ${ticket_promedio:,}")
            print(f"  → Tasa de conversión: {random.uniform(2.5, 8.5):.2f}%")
            print()
        
        total_ventas = sum(c["ventas"] for c in self.canales.values())
        total_clientes = sum(c["clientes"] for c in self.canales.values())
        
        print(f"{Fore.MAGENTA}→ Ventas totales omnicanal: ${total_ventas:,}")
        print(f"{Fore.MAGENTA}→ Total clientes únicos: {total_clientes}")
        print(f"{Fore.MAGENTA}→ Sinergia entre canales: +{random.randint(25, 40)}% vs canal único{Style.RESET_ALL}\n")
    
    def simular_experiencia_cliente_360(self):
        """Simula experiencia del cliente en múltiples touchpoints"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Experiencia del Cliente 360°")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        journeys = [
            {
                "nombre": "Journey 1: Investigación → Compra",
                "pasos": [
                    "Búsqueda en Google → Landing Page",
                    "Navegación en E-commerce → Carrito",
                    "Abandono de carrito → Email remarketing",
                    "Click en email → Compra en App Móvil"
                ],
                "conversion": True
            },
            {
                "nombre": "Journey 2: Social → Tienda",
                "pasos": [
                    "Anuncio en Instagram → Perfil de producto",
                    "Comentarios y reviews → Chatbot consulta",
                    "Reserva online → Retiro en tienda física",
                    "Cross-sell en tienda → Compra adicional"
                ],
                "conversion": True
            },
            {
                "nombre": "Journey 3: Loyalty Loop",
                "pasos": [
                    "Notificación push → App descuento",
                    "Compra en app → Puntos fidelidad",
                    "Canje de puntos → Marketplace",
                    "Review positiva → Red social"
                ],
                "conversion": True
            }
        ]
        
        for journey in journeys:
            print(f"{Fore.YELLOW}{journey['nombre']}{Style.RESET_ALL}")
            for i, paso in enumerate(journey['pasos'], 1):
                time.sleep(0.3)
                print(f"  {Fore.GREEN}{i}. {paso}")
            
            if journey['conversion']:
                valor = random.randint(150, 850)
                satisfaccion = random.randint(85, 98)
                print(f"  {Fore.MAGENTA}✓ Conversión exitosa - Valor: ${valor}")
                print(f"  {Fore.MAGENTA}✓ Satisfacción: {satisfaccion}%{Style.RESET_ALL}")
            print()
        
        print(f"{Fore.CYAN}→ Tasa de conversión omnicanal: {random.uniform(12, 18):.1f}%")
        print(f"{Fore.CYAN}→ NPS (Net Promoter Score): {random.randint(65, 82)}{Style.RESET_ALL}\n")
    
    def simular_click_and_collect(self):
        """Simula estrategia Click & Collect (compra online, recoge en tienda)"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Click & Collect - BOPIS (Buy Online Pick-up In Store)")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        ordenes = [
            {"id": "ORD-001", "producto": "Laptop ProBook 15", "valor": 1299, "tienda": "Sucursal Centro"},
            {"id": "ORD-002", "producto": "Smartwatch Series 5", "valor": 399, "tienda": "Sucursal Norte"},
            {"id": "ORD-003", "producto": "Auriculares Elite", "valor": 189, "tienda": "Sucursal Sur"},
            {"id": "ORD-004", "producto": "Tablet Ultra HD", "valor": 599, "tienda": "Sucursal Este"},
        ]
        
        print(f"{Fore.YELLOW}Procesando órdenes Click & Collect...\n{Style.RESET_ALL}")
        
        total_valor = 0
        for orden in ordenes:
            time.sleep(0.4)
            tiempo_preparacion = random.randint(15, 45)
            
            print(f"{Fore.GREEN}Orden {orden['id']}:")
            print(f"  → Producto: {orden['producto']}")
            print(f"  → Valor: ${orden['valor']}")
            print(f"  → Tienda: {orden['tienda']}")
            print(f"  → Tiempo de preparación: {tiempo_preparacion} minutos")
            print(f"  {Fore.MAGENTA}✓ Lista para recoger - Notificación enviada")
            
            # Simular cross-sell en tienda
            if random.random() > 0.6:
                extra = random.randint(50, 200)
                print(f"  {Fore.CYAN}💰 Venta adicional en tienda: ${extra}")
                total_valor += extra
            
            total_valor += orden['valor']
            print()
        
        print(f"{Fore.MAGENTA}→ Total ventas Click & Collect: ${total_valor:,}")
        print(f"{Fore.MAGENTA}→ Tráfico adicional en tienda: +{random.randint(30, 50)}%")
        print(f"{Fore.MAGENTA}→ Cross-sell rate: {random.randint(40, 65)}%{Style.RESET_ALL}\n")
    
    def simular_live_shopping(self):
        """Simula Live Shopping (transmisiones en vivo para ventas)"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}SIMULACIÓN: Live Shopping & Social Commerce 2025")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        eventos = [
            {
                "nombre": "Lanzamiento Smartphone Premium X1",
                "plataforma": "Instagram Live + TikTok",
                "duracion": 45,
                "espectadores": 3500
            },
            {
                "nombre": "Flash Sale Auriculares",
                "plataforma": "YouTube Live",
                "duracion": 30,
                "espectadores": 2200
            },
            {
                "nombre": "Demo Productos Tech",
                "plataforma": "Twitch + Facebook Live",
                "duracion": 60,
                "espectadores": 4100
            }
        ]
        
        print(f"{Fore.YELLOW}Ejecutando eventos de Live Shopping...\n{Style.RESET_ALL}")
        
        total_ventas = 0
        total_espectadores = 0
        
        for evento in eventos:
            time.sleep(0.5)
            ventas_evento = int(evento['espectadores'] * random.uniform(0.15, 0.35) * random.randint(150, 400))
            conversion = (ventas_evento / evento['espectadores']) / random.randint(150, 400) * 100
            
            print(f"{Fore.GREEN}{evento['nombre']}:")
            print(f"  → Plataforma: {evento['plataforma']}")
            print(f"  → Duración: {evento['duracion']} minutos")
            print(f"  → Espectadores: {evento['espectadores']:,}")
            print(f"  → Ventas generadas: ${ventas_evento:,}")
            print(f"  → Tasa de conversión: {random.uniform(15, 35):.1f}%")
            print(f"  {Fore.MAGENTA}✓ Engagement rate: {random.uniform(8, 15):.1f}%")
            print()
            
            total_ventas += ventas_evento
            total_espectadores += evento['espectadores']
        
        print(f"{Fore.CYAN}→ Total ventas Live Shopping: ${total_ventas:,}")
        print(f"{Fore.CYAN}→ Alcance total: {total_espectadores:,} espectadores")
        print(f"{Fore.CYAN}→ ROI vs publicidad tradicional: +{random.randint(200, 350)}%{Style.RESET_ALL}\n")
    
    def ejecutar_simulacion_completa(self):
        """Ejecuta todas las simulaciones omnicanal"""
        print(f"\n{Fore.MAGENTA}{'*'*70}")
        print(f"{Fore.MAGENTA}MÓDULO: ESTRATEGIA OMNICANAL - INNOVACIÓN 2025")
        print(f"{Fore.MAGENTA}{'*'*70}{Style.RESET_ALL}\n")
        
        self.simular_integracion_canales()
        input(f"{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
        
        self.simular_experiencia_cliente_360()
        input(f"{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
        
        self.simular_click_and_collect()
        input(f"{Fore.YELLOW}Presiona Enter para continuar...{Style.RESET_ALL}")
        
        self.simular_live_shopping()
        
        print(f"\n{Fore.GREEN}✓ Simulación Omnicanal completada{Style.RESET_ALL}\n")
