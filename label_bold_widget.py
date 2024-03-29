import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Example Window"):
     with dpg.group(font=bold_font):
        dpg.add_text("This is bold text.")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
