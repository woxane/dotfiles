from libqtile.config import Key
from libqtile.lazy import lazy
def key() : 
    ## Arrays 

    mod = 'mod4'
    terminal = 'kitty'

    ## Functions 
    def window_to_next_screen(qtile, switch_screen=False):
        i = qtile.screens.index(qtile.current_screen) + 1
        if i >= len(qtile.screens):
            i = 0
        group = qtile.screens[i].group.name
        qtile.current_window.togroup(group)
        if switch_screen:
          qtile.focus_screen(i)

    Keys = [
            ## Switchs 

            # Window Switch 
            Key([mod], "h", lazy.layout.left()),
            Key([mod], "l", lazy.layout.right()),
            Key([mod], "j", lazy.layout.down()),
            Key([mod], "k", lazy.layout.up()),
            Key([mod], "space", lazy.layout.next()), 

            # Screen Switch
            Key([mod] , 'i' , lazy.function(window_to_next_screen , switch_screen = True)),

            # Monitor Switch 
            Key([mod] , 'j' , lazy.next_screen()),

            ###############################################################################

            ## Window Controls

            # Window Move 
            Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
            Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
            Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
            Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

            # Window Grow
            Key([mod, "control"], "h", lazy.layout.grow_left()),
            Key([mod, "control"], "l", lazy.layout.grow_right()),
            Key([mod, "control"], "j", lazy.layout.grow_down()),
            Key([mod, "control"], "k", lazy.layout.grow_up()),
            Key([mod], "n", lazy.layout.normalize()),

            # Window Toggle 
            Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

            # Window Disable Float
            Key([mod] , 'x' , lazy.window.toggle_floating()),
            
            ###############################################################################

            ## Layouts 

            # Layout Toggle 
            Key([mod], "Tab", lazy.next_layout()),

            ###############################################################################

            ## Volume 

            # Volume Change 

            Key([] , 'XF86AudioRaiseVolume' , lazy.spawn('amixer set Master 5%+')) ,
            Key([] , 'XF86AudioLowerVolume' , lazy.spawn('amixer set Master 5%-')) ,
            Key([] , 'XF86AudioMute' , lazy.spawn('amixer set Master toggle')) ,

            ###############################################################################
            
            ## Shortcuts

            Key([mod], "Return", lazy.spawn(terminal)),
            Key([] , 'Print' , lazy.spawn('spectacle')),
            Key([mod] , 'f' , lazy.spawn('/home/woxane/.config/rofi/launchers/type-6/launcher.sh')),
            Key([mod], 'r' , lazy.reload_config()),
            
            ###############################################################################

            ## Groups 

            Key([mod] , '1' , lazy.group[''].toscreen()),
            Key([mod , 'shift'] , '1' , lazy.window.togroup('')),
            Key([mod] , '2' , lazy.group[''].toscreen()),
            Key([mod , 'shift'] , '2' , lazy.window.togroup('')),
            Key([mod] , '3' , lazy.group[''].toscreen()),
            Key([mod , 'shift'] , '3' , lazy.window.togroup('')),
            Key([mod] , '4' , lazy.group[''].toscreen()),
            Key([mod , 'shift'] , '4' , lazy.window.togroup('')),
            Key([mod] , '5' , lazy.group['𝅘𝅥𝅮'].toscreen()),
            Key([mod , 'shift'] , '5' , lazy.window.togroup('𝅘𝅥𝅮')),
            Key([mod] , '6' , lazy.group[' '].toscreen()),
            Key([mod , 'shift'] , '6' , lazy.window.togroup(' ')),
            Key([mod] , '7' , lazy.group[''].toscreen()),
            Key([mod , 'shift'] , '7' , lazy.window.togroup('')) , 

            ###############################################################################
   
            ## Mocp 

            Key([] , 'XF86AUdioPlay' , lazy.spawn('mocp -U')),
            Key([] , 'XF86AUdioPause' , lazy.spawn('mocp -P')), # Headphones button comes with XF86AUdioPause BUT
            Key([] , 'XF86AUdioStop' , lazy.spawn('mocp -P')),  # For Keyboard comes with XF86AUdioStop .  
            Key([] , 'XF86AUdioPrev' , lazy.spawn('mocp -r')),
            Key([] , 'XF86AUdioNext' , lazy.spawn('mocp -f')),

            ###############################################################################

            ## Others 
            Key([mod], "w", lazy.window.kill(), desc="Kill focused window"), 

            ]


    return Keys
