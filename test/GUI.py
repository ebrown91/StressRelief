import dearpygui.dearpygui as dpg


def combo_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")


with dpg.window(label="Tutorial") as window:
    # When creating items within the scope of the context
    # manager, they are automatically "parented" by the
    # container created in the initial call. So, "window"
    # will be the parent for all of these items.

    button1 = dpg.add_button(label="Press Me!")
    input_txt1 = dpg.add_input_text(
        label = "Heat Number"
        #user_data = ()
    )
        with

    combo1 = dpg.add_combo(
        label = "Tubular OD",
        items =['2.375', '2.875'],
        drag_callback = combo_callback,
        user_data= "weeee"
    )


    slider_int = dpg.add_slider_int(label="Slide to the left!",width=100)
    dpg.add_same_line(spacing=10)
    slider_float = dpg.add_slider_float(label="Slide to the right!",width=100)

    # An item's unique identifier (id) is returned when
    # creating items.
    print(f"Printing item id's: {window}, {button1}, {slider_int}, {slider_float}")

# If you want to add an item to an existing container, you
# can specify which by passing the container's id as the
# "parent" parameter.
button2=dpg.add_button(label="Don't forget me!", parent=window)

dpg.start_dearpygui()