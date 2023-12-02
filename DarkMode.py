# dark_mode.py

class DarkMode:
    def __init__(self):
        self.current_mode = "light"

    def toggle_mode(self):
        if self.current_mode == "light":
            self.current_mode = "dark"
        else:
            self.current_mode = "light"

    def get_colors(self):
        if self.current_mode == "dark":
            return (0, 0, 0), (255, 255, 255)
        else:
            return (255, 255, 255), (0, 0, 0)
