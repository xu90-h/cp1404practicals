
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """handle a convert into kilometers, on call or Button pressed"""
        try:
            #convert input value to float type
            miles = float(value)
            kilometers = miles * MILES_TO_KM
            # Display the kilometers in the output label
            self.root.ids.output_label.text = str(kilometers)
        except ValueError:
            # Handle invalid inputs
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, value, increment):
        """Increase the input value by increment"""
        try:
            #get value from input
            current_value = float(value)
            # Increase value by increment
            current_value += increment
            # return value to input
            self.root.ids.input_miles.text = str(current_value)
        except ValueError:
            # if input invalid, assume input is 0 and changes accordingly
            current_value = '0.0'
            current_value = float(current_value) + increment
            # return value to input
            self.root.ids.input_miles.text = str(current_value)


    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()