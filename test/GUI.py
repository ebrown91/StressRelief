import dearpygui.dearpygui as dpg
from Database import *
from callbacks import *

class Gui:

    def __init__(self):
        self.name = "Stress Relief Database"
        self.width = 800
        self.height = 800
        self.id = dpg.generate_uuid()

        #self.data_collector = DataCollector()
        self.db = Database()
        #self.db_viewer = DBViewerPopup()

        self.b_test_mode = True
        self.b_connected = False
        #self.connected_devices = list()

        self.test_mode_id = dpg.generate_uuid()
        self.db_name_id = dpg.generate_uuid()
        self.open_connection_id = dpg.generate_uuid()
        self.file_path_id = dpg.generate_uuid()
        self.control_group_id = dpg.generate_uuid()
        self.connected_devices_id = dpg.generate_uuid()

    def launch(self):
        dpg.setup_viewport()
        dpg.set_viewport_title(self.name)

        with dpg.window(width=self.width, height=self.height, id=self.id) as main_window:

            with dpg.group(label="input_group", horizontal=True, id=self.control_group_id):
                dpg.add_input_text(label="Database", default_value="BenConnectTESTING", id=self.db_name_id, width=200, user_data="input", callback=open_db_callback, on_enter=True)

        dpg.set_primary_window(main_window, True)

    def _init_db(self):
        db_name = dpg.get_value(self.db_name_id)

        if db_name == "test":
            db_name = ":memory:"

        self.db.open(db_name)


        #dpg.add_combo(
         #   label="Material",
          #  items=item,
           # callback=checkme,
        #)

    #with dpg.window(label="Stress Relief Test") as window:
    # When creating items within the scope of the context
    # manager, they are automatically "parented" by the
    # container created in the initial call. So, "window"
    # will be the parent for all of these items.

##couldn't resolve passing a function to items
        #combo1 = dpg.add_combo(
         #   label = "Tubular OD",
          #  items =pass_list,#Database.size_lookup,
           # callback = checkme,
            #default_value='Select an OD'
        #)

        #test_input1 = dpg.add_input_text(user_data="input", callback=size_callback, on_enter=True)
        #button1 = dpg.add_button(label="Find", callback=checkme, parent=window)
            #label = "Tubular OD",
            #user_data = "input_data",
            #callback = checkme("input_data")
        #)

        # An item's unique identifier (id) is returned when
        # creating items.
        # print(f"Printing item id's: {window}, {button1}, {slider_int}, {slider_float}")

# If you want to add an item to an existing container, you
# can specify which by passing the container's id as the
# "parent" parameter.
    #button2=dpg.add_button(label="Show Data", parent=window)


