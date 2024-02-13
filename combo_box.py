
import dearpygui.dearpygui as dpg

def combo_callback(sender, app_data, user_data):
    print(f"Selected: {app_data}")

dpg.create_context()

with dpg.window(label="Example Window"):
    # Create a Combo box
    dpg.add_combo(["Item 1", "Item 2", "Item 3"], label="Choose an Item", default_value="Item 1", callback=combo_callback)

dpg.create_viewport(title='Combo Box Example', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

