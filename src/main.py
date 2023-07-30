import  flet

from flet import *

def main(page:Page):
    page.title = "Hello World"
    page.vertical_alignment = alignment.center
    page.bgcolor = "white"

    txt_number = TextField(value="0" , text_align="center" , width=100)

    def minus(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()
    def plus(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
    Row(
        [
            IconButton(icon="Remove" , on_click=minus),
            txt_number,
            IconButton(icon="Add" , on_click=plus)
        ]
    ))


flet.app(target=main)