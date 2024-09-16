class Window(
    title: str,
    layout: Any | None = None,
    default_element_size: Any | None = None,
    default_button_element_size: Any = (None, None),
    auto_size_text: Any | None = None,
    auto_size_buttons: Any | None = None,
    location: Any = (None, None),
    relative_location: Any = (None, None),
    auto_save_location: bool = False,
    size: Any = (None, None),
    element_padding: Any | None = None,
    margins: Any = (None, None),
    button_color: Any | None = None,
    font: Any | None = None,
    progress_bar_color: Any = (None, None),
    background_color: Any | None = None,
    border_depth: Any | None = None,
    auto_close: bool = False,
    auto_close_duration: int = DEFAULT_AUTOCLOSE_TIME,
    icon: Any | None = None,
    force_toplevel: bool = False,
    alpha_channel: Any | None = None,
    return_keyboard_events: bool = False,
    use_default_focus: bool = True,
    text_justification: Any | None = None,
    no_titlebar: bool = False,
    grab_anywhere: bool = False,
    grab_anywhere_using_control: bool = True,
    keep_on_top: Any | None = None,
    resizable: bool = False,
    disable_close: bool = False,
    disable_minimize: bool = False,
    right_click_menu: Any | None = None,
    transparent_color: Any | None = None,
    debugger_enabled: bool = False,
    right_click_menu_background_color: Any | None = None,
    right_click_menu_text_color: Any | None = None,
    right_click_menu_disabled_text_color: Any | None = None,
    right_click_menu_selected_colors: Any = (None, None),
    right_click_menu_font: Any | None = None,
    right_click_menu_tearoff: bool = False,
    finalize: bool = False,
    element_justification: str = 'left',
    ttk_theme: Any | None = None,
    use_ttk_buttons: Any | None = None,
    modal: bool = False,
    enable_close_attempted_event: bool = False,
    enable_window_config_events: bool = False,
    repeating_timer_ms: Any | None = None,
    titlebar_background_color: Any | None = None,
    titlebar_text_color: Any | None = None,
    titlebar_font: Any | None = None,
    titlebar_icon: Any | None = None,
    use_custom_titlebar: Any | None = None,
    scaling: Any | None = None,
    sbar_trough_color: Any | None = None,
    sbar_background_color: Any | None = None,
    sbar_arrow_color: Any | None = None,
    sbar_width: Any | None = None,
    sbar_arrow_width: Any | None = None,
    sbar_frame_color: Any | None = None,
    sbar_relief: Any | None = None,
    watermark: Any | None = None,
    print_event_values: Any | None = None,
    metadata: Any | None = None
)
Parameters
title : (str)
The title that will be displayed in the Titlebar and on the Taskbar

layout : List[List[Element]] | Tuple[Tuple[Element]]
The layout for the window. Can also be specified in the Layout method

default_element_size : (int, int) - (width, height)
size in characters (wide) and rows (high) for all elements in this window

default_button_element_size : (int, int)
(width, height) size in characters (wide) and rows (high) for all Button elements in this window

auto_size_text : (bool)
True if Elements in Window should be sized to exactly fir the length of text

auto_size_buttons : (bool)
True if Buttons in this Window should be sized to exactly fit the text on this.

location : (int, int) or (None, None) or None
(x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen. None will not set any location meaning the OS will decide

relative_location : (int, int)
(x,y) location relative to the default location of the window, in pixels. Normally the window centers. This location is relative to the location the window would be created. Note they can be negative.

auto_save_location : (bool)
If True the windows location will be automatically saved to a settings file and will be reloaded next time the program is run. Save happens when window close is detected

size : (int, int)
(width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user. Try not to set this value. You risk, the contents being cut off, etc. Let the layout determine the window size instead

element_padding : (int, int) or ((int, int),(int,int)) or int
Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)), or an int. If an int, then it's converted into a tuple (int, int)

margins : (int, int)
(left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown.

button_color : (str, str) | str
Default button colors for all buttons in the window

font : (str or (str, int[, str]) or None)
specifies the font family, size, etc. Tuple or Single string format 'name size styles'. Styles: italic * roman bold normal underline overstrike

progress_bar_color : (str, str)
(bar color, background color) Sets the default colors for all progress bars in the window

background_color : (str)
color of background

border_depth : (int)
Default border depth (width) for all elements in the window

auto_close : (bool)
If True, the window will automatically close itself

auto_close_duration : (int)
Number of seconds to wait before closing the window

icon : (str | bytes)
Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO. Most portable is to use a Base64 of a PNG file. This works universally across all OS's

force_toplevel : (bool)
If True will cause this window to skip the normal use of a hidden master window

alpha_channel : (float)
Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.

return_keyboard_events : (bool)
if True key presses on the keyboard will be returned as Events from Read calls

use_default_focus : (bool)
If True will use the default focus algorithm to set the focus to the "Correct" element

text_justification : 'left' | 'right' | 'center'
Default text justification for all Text Elements in window

no_titlebar : (bool)
If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar

grab_anywhere : (bool)
If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems

grab_anywhere_using_control : (bool)
If True can use CONTROL key + left mouse mouse to click and drag to move the window. DEFAULT is TRUE. Unlike normal grab anywhere, it works on all elements.

keep_on_top : (bool)
If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm

resizable : (bool)
If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.

disable_close : (bool)
If True, the X button in the top right corner of the window will no work. Use with caution and always give a way out toyour users

disable_minimize : (bool)
if True the user won't be able to minimize window. Good for taking over entire screen and staying that way.

right_click_menu : List[List[ List[str] | str ]]
A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.

transparent_color : (str)
Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.

debugger_enabled : (bool)
If True then the internal debugger will be enabled. Also controllable via the global settings. If global settings is true then will be enabled for all windows

right_click_menu_background_color : (str)
Background color for right click menus

right_click_menu_text_color : (str)
Text color for right click menus

right_click_menu_disabled_text_color : (str)
Text color for disabled right click menu items

right_click_menu_selected_colors : (str, str) | str | Tuple
Text AND background colors for a selected item. Can be a Tuple OR a color string. simplified-button-color-string "foreground on background". Can be a single color if want to set only the background. Normally a tuple, but can be a simplified-dual-color-string "foreground on background". Can be a single color if want to set only the background.

right_click_menu_font : (str or (str, int[, str]) or None)
Font for right click menus

right_click_menu_tearoff : bool
If True then all right click menus can be torn off

finalize : (bool)
If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code

element_justification : (str)
All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values

ttk_theme : (str)
Set the tkinter ttk "theme" of the window. Default = DEFAULT_TTK_THEME. Sets all ttk widgets to this theme as their default

use_ttk_buttons : (bool)
Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons. None = use ttk buttons only if on a Mac

modal : (bool)
If True then this window will be the only window a user can interact with until it is closed

enable_close_attempted_event : (bool)
If True then the window will not close when "X" clicked. Instead an event WINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read

enable_window_config_events : (bool)
If True then window configuration events (resizing or moving the window) will return WINDOW_CONFIG_EVENT from window.read. Note you will get several when Window is created.

repeating_timer_ms : (int)
Causes a repeating timer to start when Window is created. The default EVENT_TIMER will be used for the timer event. Setting will cause window to be Finalized

titlebar_background_color : (str | None)
If custom titlebar indicated by use_custom_titlebar, then use this as background color

titlebar_text_color : (str | None)
If custom titlebar indicated by use_custom_titlebar, then use this as text color

titlebar_font : (str or (str, int[, str]) or None)
If custom titlebar indicated by use_custom_titlebar, then use this as title font

titlebar_icon : (bytes | str)
If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)

use_custom_titlebar : bool
If True, then a custom titlebar will be used instead of the normal titlebar

scaling : float
Apply scaling to the elements in the window. Can be set on a global basis using set_options

sbar_trough_color : (str)
Scrollbar color of the trough

sbar_background_color : (str)
Scrollbar color of the background of the arrow buttons at the ends AND the color of the "thumb" (the thing you grab and slide). Switches to arrow color when mouse is over

sbar_arrow_color : (str)
Scrollbar color of the arrow at the ends of the scrollbar (it looks like a button). Switches to background color when mouse is over

sbar_width : (int)
Scrollbar width in pixels

sbar_arrow_width : (int)
Scrollbar width of the arrow on the scrollbar. It will potentially impact the overall width of the scrollbar

sbar_frame_color : (str)
Scrollbar Color of frame around scrollbar (available only on some ttk themes)

sbar_relief : (str)
Scrollbar relief that will be used for the "thumb" of the scrollbar (the thing you grab that slides). Should be a constant that is defined at starting with "" - RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID

watermark : bool
If True, then turns on watermarking temporarily for ALL windows created from this point forward. See global settings doc for more info

print_event_values : bool
If True then the event and values will be automatically printed when you call the window's read method. GREAT for debugging! Global setting also available to control this.

metadata : (Any)
User metadata that can be set to ANYTHING

Window