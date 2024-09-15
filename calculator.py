import customtkinter as ctk
import darkdetect
import settings
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class Calculator(ctk.CTk):
    def __init__(self, is_dark):

        #setup
        super().__init__(fg_color = (settings.WHITE, settings.BLACK))

        ctk.set_appearance_mode(f'{"dark" if is_dark else "dark"}')
        print(darkdetect.isDark())
        self.geometry(f'{settings.APP_SIZE[0]}x{settings.APP_SIZE[1]}+1920+0')
        self.resizable(False, False)
        self.title('')
        self.title_bar_color(is_dark)

        # Grid
        self.rowconfigure(list(range(settings.MAIN_ROWS)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(settings.MAIN_COLUMNS)), weight = 1, uniform = 'a')
        
        self.mainloop()

    def title_bar_color(self, is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo._id())
            DWMWA_ATTRIBUTE = 35
            COLOR = settings.TITLE_BAR_HEX_COLORS['dark'] if is_dark else settings.TITLE_BAR_HEX_COLORS['dark']
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass



if __name__ == '__main__':
    Calculator(darkdetect.isDark())