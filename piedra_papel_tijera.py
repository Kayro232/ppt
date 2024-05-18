import flet as  ft 
import random
import time
#variables para ganar,perdiste y empate
valor = 0
valor2 = 0
valor3 = 0
def main(page):
    global valor
    global valor2
    global valor3
    page.title = "piedra papel o tijera"
    page.window_width = 700
    page.window_height = 800
    page.theme_mode= "LIGTH"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.theme_mode = "dark"
    page.window_full_screen = True
    page.update()
    #creando imagenes
    imagenes = {
      "tijera": ft.Image(src="https://cdn-icons-png.flaticon.com/512/3976/3976545.png",scale=0.900),
      "piedra": ft.Image(src="https://cdn-icons-png.flaticon.com/512/5461/5461550.png"),
      "papel": ft.Image(src="https://cdn-icons-png.flaticon.com/512/5832/5832307.png")
    }
    #creando funciones
    def Tijera(e):
     global valor
     #cambiando el color del container
     desactivar()
     conten1.bgcolor = ft.colors.YELLOW_100
     page.update()
     time.sleep(2)
     conten1.bgcolor=ft.colors.YELLOW
     page.update()  
     tijera =random.randint(1,3)
     texto.value= f"el both esta eligiendo..."
     page.update()
     time.sleep(2)
     if tijera == 1:
       texto.value= f"el both escogio papel"
       page.update()
       time.sleep(1)
       page.update()
       texto.value= f"GANASTE"
       valor+=1
       ganadas.value = f"GANADAS:{valor}"
       activar()
     elif tijera == 2:
       global valor2
       texto.value = f"el both escogio piedra"
       page.update()
       time.sleep(1)
       texto.value= f"PERDISTE"
       valor2+=1
       perdidas.value = f"PERDIDAS:{valor2}"
       page.update()
       activar()
     elif tijera == 3:
       global valor3
       texto.value = f"el both escogio tijera"
       page.update()
       time.sleep(1)
       texto.value= f"ES UN EMPATE"
       valor3+=1
       empatadas.value= f"EMPATADAS:{valor3}"
       page.update()
       activar()
     page.update()
    def Piedra(e):
     desactivar()
     conten2.bgcolor = ft.colors.PURPLE_100
     page.update()
     time.sleep(2)
     conten2.bgcolor=ft.colors.PURPLE
     page.update()
     piedra =random.randint(1,3)
     texto.value= f"el both esta eligiendo..."
     page.update()
     time.sleep(2)
     page.update()
     if piedra == 1:
       global valor
       texto.value= f"el both escogio tijera"
       page.update()
       time.sleep(1)
       page.update()
       texto.value= f"GANASTE"
       valor+=1
       ganadas.value = f"GANADAS:{valor}"
       activar()
     elif piedra == 2:
       global valor2
       texto.value = f"el both escogio papel"
       page.update()
       time.sleep(1)
       texto.value= f"PERDISTE"
       valor2+=1
       perdidas.value = f"PERDIDAS:{valor2}"
       page.update()
       activar()
     elif piedra == 3:
       global valor3
       texto.value = f"el both escogio piedra"
       page.update()
       time.sleep(1)
       texto.value= f"ES UN EMPATE"
       valor3+=1
       empatadas.value = f"EMPATADAS:{valor3}"
       page.update()
       activar()
     page.update()
    def Papel(e):
     desactivar()
     conten3.bgcolor = ft.colors.RED_100
     page.update()
     time.sleep(2)
     conten3.bgcolor=ft.colors.RED
     page.update()
     #creando ganaste,perdiste o empataste
     papel =random.randint(1,3)
     texto.value= f"el both esta eligiendo..."
     page.update()
     time.sleep(2)
     page.update()
     if papel == 1:
       global valor
       texto.value= f"el both escogio piedra"
       page.update()
       time.sleep(1)
       page.update()
       texto.value="GANASTE"
       valor+=1
       ganadas.value = f"GANADAS:{valor}"
       page.update()
       activar()
     elif papel == 2:
       global valor2
       texto.value = f"el both escogio tijera"
       page.update()
       time.sleep(1)
       texto.value= f"PERDISTE"
       valor2+=1
       perdidas.value = f"PERDIDAS:{valor2}"
       page.update() 
       activar()
     elif papel == 3:
       global valor3
       texto.value = f"el both escogio papel"
       page.update()
       time.sleep(1)
       texto.value= f"ES UN EMPATE"
       valor3+=1
       empatadas.value = f"EMPATADAS:{valor3}"
       page.update() 
       activar()
     page.update()
    #desactivando los botones
    def desactivar():
      intocable = True
      conten1.disabled = intocable
      conten2.disabled = intocable
      conten3.disabled = intocable
    def activar():
      Intocable = False
      conten1.disabled = Intocable
      conten2.disabled = Intocable
      conten3.disabled = Intocable
    #creando los containers y variables
    empatadas = ft.Text(value=f"EMPATADAS:{valor3}",size=20)
    perdidas = ft.Text(value=f"PERDIDAS:{valor2}",size=20)
    ganadas = ft.Text(value=f"GANADAS:{valor}",size=20)
    texto = ft.Text("selecione piedra,papel o tijera",size= 20,color=ft.colors.WHITE)
    pantalla_arriba= ft.Container(ft.Column(controls=[ganadas,perdidas,empatadas]),width=200,height=100,margin=15)
    pantalla_negra = ft.Container(content=texto,bgcolor=ft.colors.BLACK,width=600,height=400,alignment=ft.alignment.center,border_radius=24,margin=15)
    conten1 = ft.Container(shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.YELLOW,width=110,height=200,content=imagenes.get("tijera"),on_click=Tijera)
    conten2 = ft.Container(shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.PURPLE,width=110,height=200,content=imagenes.get("piedra"),on_click=Piedra)
    conten3 = ft.Container(shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.RED,width=110,height=200,content=imagenes.get("papel"),on_click=Papel)
    #posicion
    lado = ft.Row(spacing=20,alignment=ft.MainAxisAlignment.CENTER,controls=[
        conten1,
        conten2,
        conten3,  
    ])
    page.add(pantalla_arriba,pantalla_negra,lado)
ft.app(target=main)