import dearpygui.dearpygui as dpg

# required functions for Dear PyGui
dpg.create_context()
dpg.create_viewport(title='Group', width=1200, height=675) # 16:9 ratio

# Create a new window
with dpg.window(label="My Window"):
    # Add a group container
    with dpg.group(label="My Group"):
        # Add a button inside the group
        dpg.add_button(label="My Button")
        # Add a text input inside the group
        dpg.add_input_text(label="My Input", default_value="Type something here...")

# Set the primary window
window_id = dpg.add_window(label="My Window")
dpg.set_primary_window(window_id, True)

# required functions for Dear PyGui
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()