import flet as ft
from db import main_db


def main_page(page: ft.Page):
    page.title = 'To Do List'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()

    def view_task(task_id, task_text, task_date): 
        task_field = ft.TextField(value=task_text, expand=True, read_only=True)
        date_label = ft.Text(value=task_date, size=11, color=ft.Colors.GREY)

        def save_edit(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_edit)

        def enable_edit(_):
            task_field.read_only = not task_field.read_only
            page.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def remove_task(_):
            main_db.delete_task(task_id)
            task_list.controls = [
                row for row in task_list.controls
                if row != task_row
            ]
            page.update()

        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE,
            icon_color=ft.Colors.RED,
            on_click=remove_task 
        )

        task_row = ft.Row([
            ft.Column([task_field, date_label], expand=True),
            edit_button,
            save_button,
            delete_button,
        ])
        return task_row

    def add_task_flet(_):
        if task_input.value:
            task_text = task_input.value.strip()
            task_id, task_date = main_db.add_task(task=task_text)
            task_input.value = None
            task_list.controls.append(
                view_task(task_id=task_id, task_text=task_text, task_date=task_date)
            )
            page.update()

    task_input = ft.TextField(label='Введите задачу', on_submit=add_task_flet)
    add_button = ft.Button("ADD", icon=ft.Icons.ADD, on_click=add_task_flet)

    page.add(ft.Row([task_input, add_button]), task_list)


if __name__ == '__main__':
    main_db.init_db()
    ft.run(main_page)