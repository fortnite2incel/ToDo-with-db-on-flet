import flet as ft
from db import main_db


def main_page(page: ft.Page):
    page.title = 'To Do List'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()

    filter_type = 'all'

    def load_tasks():
        task_list.controls.clear()
        for task_id, task, task_date, completed in main_db.get_tasks(filter_type):
            task_list.controls.append(
                view_task(task_id=task_id, task_text=task,task_date=task_date, completed=completed)
            )
        page.update()

    def view_task(task_id, task_text, task_date, completed=None): 
        task_field = ft.TextField(value=task_text, expand=True, read_only=True)
        date_label = ft.Text(value=task_date or '', size=11, color=ft.Colors.GREY)

        checkbox = ft.Checkbox(
            value=bool(completed), 
            on_change=lambda e: toggle_task(task_id=task_id, is_completed=e.control.value)
            )

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
            main_db.delete_task_by_id(task_id)
            task_list.controls.remove(task_row)
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
            checkbox
        ])
        return task_row

    def toggle_task(task_id, is_completed):
        main_db.update_task(task_id=task_id, completed=int(is_completed))
        page.update()

    def add_task_flet(_):
        if task_input.value:
            task_text = task_input.value.strip()
            task_id, task_date = main_db.add_task(task=task_text)
            task_input.value = None
            task_list.controls.append(
                view_task(task_id=task_id, task_text=task_text, task_date=task_date)
            )
            page.update()

    task_input = ft.TextField(label='Введите задачу', on_submit=add_task_flet, expand=True)
    
    def set_filter(f):
        nonlocal filter_type
        filter_type = f
        load_tasks()

    def clear_completed(_):
        main_db.clear_completed()
        load_tasks()
    
    add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_flet)

    filter_buttons = ft.Row([
        ft.ElevatedButton('Все задачи', on_click=lambda e: set_filter('all')),
        ft.ElevatedButton('В работе', on_click=lambda e: set_filter('uncompleted')),
        ft.ElevatedButton('Готово ✅', on_click=lambda e: set_filter('completed')), 
        ft.ElevatedButton(
            'Очистить выполненные 🗑',
            on_click=clear_completed,
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.RED_400,
        ),
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)


    page.add(
        ft.Row([task_input, add_button]),
        filter_buttons,
        task_list
    )
 
    load_tasks()

if __name__ == '__main__':
    main_db.init_db()
    ft.run(main_page)