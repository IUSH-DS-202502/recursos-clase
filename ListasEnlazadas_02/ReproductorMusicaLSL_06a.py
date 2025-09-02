from ClaseLSL_03 import LSL

import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path
import time

# Oculta el mensaje de bienvenida de Pygame para una interfaz de línea de comandos más limpia.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class ListaReproduccion(LSL):
    """
    Clase que extiende una Lista Simplemente Enlazada (LSL) para gestionar una lista de reproducción de música.
    Cada nodo en la lista contiene la ruta a un archivo de canción.
    """
    def __init__(self) -> None:
        """Inicializa una lista de reproducción vacía."""
        super().__init__()

    def recorre(self):
        """
        Imprime los nombres de las canciones en la lista de reproducción.
        Muestra solo el nombre del archivo sin la extensión para una mejor legibilidad.
        """
        iterador = self.primerNodo()
        if iterador is None:
            print("La lista de reproducción está vacía.")
            return
        
        while iterador != None:
            # Usa pathlib.Path para extraer el nombre del archivo sin la extensión.
            print(Path(iterador.retornaDato()).stem)
            iterador = iterador.retornaLiga()



class ReproductorMusica():
    """
    Clase principal que encapsula la lógica de un reproductor de música de línea de comandos.
    Gestiona la lista de reproducción, el estado de la reproducción (play, pausa, stop) y la interacción con el usuario.
    """
    def __init__(self) -> None:
        """Inicializa el reproductor de música."""
        self.lista_reproduccion = ListaReproduccion() # La cola de canciones por reproducir.
        self.pausado = False                          # Flag para controlar el estado de pausa.
        self.cancion_actual = None                    # Almacena la ruta de la canción que se está reproduciendo o lista para reproducir.

    def mostrar_menu(self):
        """Imprime las opciones del menú principal en la consola."""
        time.sleep(2) # Pequeña pausa para no saturar la consola.
        print("\n--- Reproductor de Música de Línea de Comandos ---")
        print("1. Agregar Canción a la Lista de Reproducción")
        print("2. Reproducir")
        print("3. Pausar")
        print("4. Detener")
        print("5. Siguiente Canción")
        print("6. Mostrar Lista de Reproducción")
        print("7. Mostrar nombre de la canción actual")
        print("8. Salir")
        print("--------------------------------------------------")

    def cargar_musica(self):
        """
        Abre un diálogo de selección de archivo para que el usuario elija una canción.
        La canción seleccionada se agrega al final de la lista de reproducción.
        """
        # Utiliza tkinter para mostrar un diálogo de selección de archivo nativo.
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3"), ("Archivos WAV", "*.wav")])
        
        if not nombre_archivo:
            print("No se seleccionó ningún archivo.")
            return
        
        # Se inserta la ruta del archivo en la lista simplemente enlazada.
        self.lista_reproduccion.insertar(nombre_archivo)

        print(f"Canción '{Path(nombre_archivo).stem}' agregada a la lista de reproducción.")
        return

    def reproducir_musica(self):
        """
        Carga y reproduce una canción. Si la música está en pausa, la reanuda.
        Si no hay una canción cargada, toma la primera de la lista de reproducción.
        """

        # Si ya hay música sonando, no hace nada.
        if pygame.mixer.music.get_busy():
            print("Ya hay música reproduciéndose actualmente, intente cambiar de canción, pausar o detener la reproducción.")
            return
        # Si la música está en pausa, la reanuda.
        if self.pausado:
            pygame.mixer.music.unpause()
            self.pausado = False
            print("Reanudado.")
            return
        # Si la lista de reproducción está vacía, no hay nada que reproducir.
        if self.lista_reproduccion.esVacia():
            print("Por favor, cargue un archivo primero (Opción 1).")
            return
        # Si no hay una canción "actual", toma la primera de la lista.
        if self.cancion_actual is None:
            # Obtiene la ruta de la primera canción en la lista.
            nombre_archivo = self.lista_reproduccion.primerNodo().retornaDato()
            # Carga la canción en el reproductor de pygame.
            pygame.mixer.music.load(nombre_archivo)
            # Establece la canción como la actual.
            self.cancion_actual = nombre_archivo
            # Elimina la canción de la lista de espera.
            self.lista_reproduccion.borrar(nombre_archivo)
            
        # Inicia la reproducción.
        pygame.mixer.music.play()

        print(f"Reproduciendo: {Path(self.cancion_actual).stem}")

    def pausar_musica(self):
        """Pausa la reproducción de la canción actual."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.pausado = True
            print("En pausa.")
        else:
            print("No hay música reproduciéndose actualmente.")

    def detener_musica(self):
        """Detiene por completo la reproducción de la canción actual."""
        pygame.mixer.music.stop()
        self.pausado = False
        print("Detenido.")

    def siguiente_cancion(self):
        """
        Detiene la canción actual y reproduce la siguiente en la lista de reproducción.
        """
        self.detener_musica()
        # Al poner cancion_actual en None, forzamos a reproducir_musica() a tomar la siguiente de la lista.
        self.cancion_actual = None
        self.reproducir_musica()

    def mostrar_lista_reproduccion(self):
        """Muestra las canciones que están en la cola de reproducción."""
        print("Lista de Reproducción:")
        self.lista_reproduccion.recorre()

    def mostrar_cancion_actual(self):
        """Muestra el nombre de la canción que se está reproduciendo actualmente."""
        if self.cancion_actual and not self.pausado:
            print(f"Canción actual: {Path(self.cancion_actual).stem}")
        else:
            print("No hay ninguna canción sonando en este momento.")


    def iniciar_app(self):
        """
        Bucle principal de la aplicación. Muestra el menú y procesa la entrada del usuario
        hasta que se elige la opción de salir.
        """
        
        while True:
            self.mostrar_menu()
            eleccion = input("Ingrese su elección: ")
            
            if eleccion == '1':
                self.cargar_musica()
            elif eleccion == '2':
                self.reproducir_musica()
            elif eleccion == '3':
                self.pausar_musica()
            elif eleccion == '4':
                self.detener_musica()
            elif eleccion == '5':
                self.siguiente_cancion()
            elif eleccion == '6':
                self.mostrar_lista_reproduccion()
            elif eleccion == '7':
                self.mostrar_cancion_actual()
            elif eleccion == '8':
                print("Saliendo del reproductor de música. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    # Inicializa el mezclador de audio de Pygame. Es necesario para reproducir sonidos.
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"No se pudo inicializar el mezclador: {e}")
        exit()

    # Creamos una instancia raíz de Tkinter para poder usar el diálogo de selección de archivos.
    root = tk.Tk()
    # Ocultamos la ventana principal de Tkinter, ya que solo necesitamos el diálogo.
    root.withdraw() 

    # Crea una instancia del reproductor y comienza la aplicación.
    reproductor = ReproductorMusica()
    reproductor.iniciar_app()

    # Cierra la instancia de Tkinter al finalizar el programa.
    root.destroy()
