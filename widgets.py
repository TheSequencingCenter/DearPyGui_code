# imports
import dearpygui.dearpygui as dpg

# required functions for Dear PyGui
dpg.create_context()
dpg.create_viewport(title='Widgets', width=1200, height=675) # 16:9 ratio

# window
with dpg.window(label="Main window", width=1000, height=562, show=True, tag="main_window"): # 16:9 ratio
    # dpg.add_combo(customer_list, label="Choose a customer", callback=customer_callback, width=400, default_value=customer_list[0])
    dpg.add_input_text(default_value="add_input_text 1", width=300, tag="input_text")
    dpg.add_input_text(default_value="add_input_text 2", width=300, tag="label")

# THEMES
# global theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core) # orange
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 140, 140), category=dpg.mvThemeCat_Core) # grey
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvInputInt):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 255, 23), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

# # container theme
# with dpg.theme() as container_theme:
#     with dpg.theme_component(dpg.mvAll):
#         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
#         dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    # with dpg.theme_component(dpg.mvInputInt):
    #     dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (100, 150, 100), category=dpg.mvThemeCat_Core)
    #     dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

# # item theme
# with dpg.theme() as item_theme:
#     with dpg.theme_component(dpg.mvAll):
#         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (200, 200, 100), category=dpg.mvThemeCat_Core)
#         dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)
        
# Theme for input_text
with dpg.theme() as theme_input_text:
    with dpg.theme_component(dpg.mvInputText):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)  # orange
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

# Theme for label
with dpg.theme() as theme_label:
    with dpg.theme_component(dpg.mvText):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (140, 140, 255), category=dpg.mvThemeCat_Core)  # blue

# bind themes
dpg.bind_theme(global_theme)
# dpg.bind_item_theme(win1, container_theme)
# dpg.bind_item_theme(t2, item_theme)
dpg.bind_item_theme("input_text", theme_input_text)
dpg.bind_item_theme("label", theme_label)

# style editor
# dpg.show_style_editor()

# required functions for Dear PyGui
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()