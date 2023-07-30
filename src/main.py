import  flet

from flet import *

def main(page:Page):
    page.title = "Login Page"
    page.bgcolor = "white"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    username = TextField(
        width=500,
        text_align=alignment.center,
        text_size=20,
        label="Username",
    )
    password = TextField(
        width=500,
        text_align=alignment.center,
        text_size=20,
        label="Password",
    )

    def login(e):
        if not username.value :
            print("Login Success")
        else:
            print("Login Failed")
    button = Row(

        [
            Container(
        content=FilledButton(

            "Login",
            on_click=login,
            width=250,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10),
                color="blue"

            ),
        )

    ),
    Container(
        content=FilledButton(
            "Register",
            on_click=login,
            width=250,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10),

            ),
        )

    )
        ]
    )

    def col (align: MainAxisAlignment):
        return Container(
            width=500,
            content=Column(
                [
                    username,
                    password,
                    button
                ],
            ),
        )



    page.add(
        col(MainAxisAlignment.START)
    )


flet.app(target=main)