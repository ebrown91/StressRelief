import dearpygui.dearpygui as dpg

unique_id = dpg.generate_uuid()

def callback():
    print(dpg.get_value(unique_id))

with dpg.window(label="Example"):

    dpg.add_button(label="Press me", callback=callback)
    dpg.add_input_int(label="Input", id=unique_id)

dpg.start_dearpygui()