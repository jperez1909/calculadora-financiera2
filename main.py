import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Financiera"
    page.padding = 30
    page.add(
        ft.Text("💰 Calculadora Financiera", size=30, weight=ft.FontWeight.BOLD),
        ft.TextField(label="Monto", keyboard_type=ft.KeyboardType.NUMBER),
        ft.TextField(label="Tasa %", keyboard_type=ft.KeyboardType.NUMBER),
        ft.ElevatedButton("Calcular", icon=ft.icons.CALCULATE),
        ft.Text("Resultado")
    )

ft.app(target=main)
