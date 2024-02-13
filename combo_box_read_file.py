import dearpygui.dearpygui as dpg

def combo_callback(sender, app_data, user_data):
    print(f"Selected: {app_data}")

def read_items_from_file(file_path):
    with open(file_path, 'r') as file:
        items = [line.strip() for line in file.readlines()]
    return items

dpg.create_context()

# File path to your items file
file_path = 'combo_box_items.txt'
items_list = read_items_from_file(file_path)

with dpg.window(label="Example Window"):
    # Create a Combo box with items read from file
    dpg.add_combo(items_list, label="Choose an Item", callback=combo_callback)

dpg.create_viewport(title='Combo Box Example', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

