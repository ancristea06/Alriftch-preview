# simulador_combate.py
class Carta:
    def __init__(self, id, nombre, clase, ataque, salud, rango, alcance, coste_habilidad, habilidad):
        self.id = id
        self.nombre = nombre
        self.clase = clase
        self.ataque = ataque
        self.salud = salud
        self.salud_max = salud
        self.rango = rango  # "Cuerpo" o "Distancia"
        self.alcance = alcance
        self.coste_habilidad = coste_habilidad
        self.habilidad = habilidad
        self.linea = 1  # 1, 2 o 3
        self.columna = 1  # 1, 2 o 3
        
    def puede_atacar(self, objetivo_linea):
        """Determina si puede atacar a una línea específica"""
        if self.rango == "Cuerpo":
            return self.linea == 1 and objetivo_linea == 1
        elif self.rango == "Distancia":
            return self.linea <= self.alcance
        return False
    
    def atacar(self, objetivo):
        """Realiza un ataque a otra carta"""
        if self.puede_atacar(objetivo.linea):
            print(f"{self.nombre} ataca a {objetivo.nombre}")
            objetivo.salud -= self.ataque
            self.salud -= objetivo.ataque
            
            # Verificar muertes
            if objetivo.salud <= 0:
                print(f"  {objetivo.nombre} MUERE")
                return True
            if self.salud <= 0:
                print(f"  {self.nombre} MUERE")
                return True
        else:
            print(f"{self.nombre} NO puede atacar a {objetivo.nombre} (rango/alcance)")
        return False

class Jugador:
    def __init__(self, nombre, vida=25):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.maná = 1
        self.maná_max = 1
        self.campo = [[None, None, None],  # Línea 1
                      [None, None, None],  # Línea 2  
                      [None, None, None]]  # Línea 3
        
    def colocar_carta(self, carta, linea, columna):
        """Coloca una carta en el campo"""
        if 1 <= linea <= 3 and 1 <= columna <= 3:
            if self.campo[linea-1][columna-1] is None:
                carta.linea = linea
                carta.columna = columna
                self.campo[linea-1][columna-1] = carta
                print(f"{self.nombre} coloca {carta.nombre} en L{linea}C{columna}")
                return True
        return False
    
    def obtener_carta_en(self, linea, columna):
        """Obtiene carta en posición específica"""
        if 1 <= linea <= 3 and 1 <= columna <= 3:
            return self.campo[linea-1][columna-1]
        return None

def simular_combate_basico():
    """Simula un combate simple entre dos cartas"""
    print("=== SIMULADOR DE COMBATE BÁSICO ===")
    
    # Crear cartas de prueba
    lancero = Carta("G001", "Lancero", "Guerrero", 2, 4, "Cuerpo", 1, 0, "-")
    arquero = Carta("G002", "Arquero", "Guerrero", 3, 2, "Distancia", 3, 1, "-")
    escudero = Carta("T001", "Escudero", "Tanque", 1, 5, "Cuerpo", 1, 0, "-")
    
    # Crear jugadores
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    
    # Colocar cartas
    jugador1.colocar_carta(lancero, 1, 1)  # Lancero en L1C1
    jugador2.colocar_carta(escudero, 1, 1)  # Escudero en L1C1
    jugador2.colocar_carta(arquero, 3, 2)   # Arquero en L3C2
    
    print("\n--- Combate 1: Lancero vs Escudero ---")
    resultado = lancero.atacar(escudero)
    
    print(f"\nEstado después del combate:")
    print(f"  Lancero: {lancero.salud}/{lancero.salud_max} salud")
    print(f"  Escudero: {escudero.salud}/{escudero.salud_max} salud")
    
    print("\n--- Prueba de alcance ---")
    print(f"Arquero en L{arquero.linea} puede atacar L1: {arquero.puede_atacar(1)}")
    
    return jugador1, jugador2

if __name__ == "__main__":
    jugador1, jugador2 = simular_combate_basico()
    print("\n✅ Simulación completada")