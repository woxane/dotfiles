# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

import os 
from datetime import datetime
from libqtile import bar, layout, widget , hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from subprocess import check_output , call
mod = "mod4"
terminal = 'kitty'

# Move a window to the next screen
def window_to_next_screen(qtile, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen) + 1
    if i >= len(qtile.screens):
        i = 0
    group = qtile.screens[i].group.name
    qtile.current_window.togroup(group)
    if switch_screen:
      qtile.focus_screen(i)

def get_time() :
    time_dict = {0 : "🕛" ,
                1  : "🕐" ,
                2 : "🕑" ,
                3 : "🕒" ,
                4 : "🕓" ,
                5 : "🕔" ,
                6 : "🕕" ,
                7 : "🕖" ,
                8 : "🕗" ,
                9 : "🕘" ,
                10 : "🕙" ,
                11 : "🕚" ,
                12 : "🕛" }
    icon = time_dict[int(datetime.now().strftime('%H')) % 12 ] 
    return datetime.now().strftime('%H:%M:%S') +" "+ icon



def get_controller_charge() :
    if os.path.exists('/sys/class/power_supply/sony_controller_battery_dc:af:68:d1:ac:15') : 
        return check_output(['cat' , '/sys/class/power_supply/sony_controller_battery_dc:af:68:d1:ac:15/capacity']).decode().strip() + '%' + '🎮'

    else : 
        return

def MocpControll() : 
    Play = '▶' 
    Pause = '⏸︎'
    Status = check_output(['mocp' , '-Q' , '%state']).decode().strip()
    
    if 'PLAY' == Status : 
        return Pause
    elif 'PAUSE' == Status : 
        return Play

    return 'a' 




def get_callender() :
    return  check_output(["jdate" , "+'%b-%d'"]).decode().strip()[1:-1]
 
def get_current_keyboard_lan() :
    output = check_output(['xkblayout']).decode().strip() # give the current keyboard layout
    if output == 'Eng' :
        return '🇺🇸'
    elif output == 'Per' :
        return '🇮🇷'
    return output


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    ### Switch to next screen
    Key([mod] , 'i' , lazy.function(window_to_next_screen , switch_screen = True)) , 

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),


    # Dmenu 
    Key([mod] , 'f' , lazy.spawn('dmenu_run -c -l 10') , desc = 'run dmenu ') , 
    Key([mod , 'shift'] , 't' , lazy.spawn('./Files/dmenu/dmscripts/todo -c') , desc = 'launch todo list ') , 
    Key([mod] , 'p' , lazy.spawn('passmenu -c -l 10') , desc = 'launch passmenu') ,
    Key([mod] , 'm' , lazy.spawn('./Files/dmenu/dmscripts/dm-man')) , 


    ### opening shortcut ###
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], 't' , lazy.spawn('telegram-desktop') , desc = 'launch telgram'),
    Key([mod], 'q' , lazy.spawn('qutebrowser') , desc = 'launch qutebrowser'),  
    Key([mod] , 'b' , lazy.spawn('brave') , desc = 'launch brave browser') , 
    Key([mod] , 's' , lazy.spawn('proxychains spotify')) ,
    Key([mod] , 'd' , lazy.spawn('dolphin')) , 
    ### Switch between monitors ###
    Key([mod] , 'j' , lazy.next_screen() , desc = 'swtich to next monitor') ,
    


    ### Lock screen ###
    Key([] , 'F8'  , lazy.spawn('betterlockscreen -l') , desc = 'run betterlockscreen -l command for lock screen') , 

        
    ### Volume changer ### 
    Key([] , 'XF86AudioRaiseVolume' , lazy.spawn('amixer set Master 5%+')) ,
    Key([] , 'XF86AudioLowerVolume' , lazy.spawn('amixer set Master 5%-')) ,

    Key([] , 'XF86AudioMute' , lazy.spawn('amixer set Master toggle') , desc = 'mute/unmute') ,


    ### screen shot ###
    Key([] , 'Print' , lazy.spawn('spectacle') , desc = 'launch spectacle') , 

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

def init_group_names() : 
    return [('' , {'layout' : 'max'}) , 
            ('' , {'layout' : 'max'}),
            ('' , {'layout' : 'max'})  , 
            ('' , {'layout' : 'max'}) ,
            ('𝅘𝅥𝅮' , {'layout' : 'max'}) , 
            ('' , {'layout' : 'max'}) , 
            ('' , {'layout' : 'max'}) , 
]


def init_groups() :
    return [Group(name , **kwargs) for name , kwargs in group_names]

if __name__ in ['config' , '__main__'] :
    group_names = init_group_names() 
    groups = init_groups()

for i , (name , kwargs) in enumerate(group_names , 1) :
    keys.append(Key([mod] ,str(i) , lazy.group[name].toscreen()))           # Switch to another group 
    keys.append(Key([mod , 'shift'] , str(i) , lazy.window.togroup(name)))  # Switch current windo to another group



layouts = [
    layout.Columns(border_focus_stack='#3DB9C7' , border_focus = '#CC00CC', margin = 3 , border_width = 2),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
#     layout.Stack(num_stacks=2),
#     layout.Bsp(),
#     layout.Matrix(),
#     layout.MonadTall(),
#     layout.MonadWide(),
#     layout.RatioTile(),
#     layout.Tile(),
#     layout.TreeTab(),
#     layout.VerticalTile(),
#     layout.Zoomy(),
]

widget_defaults = dict(
    font= 'Roboto' , 
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

colors = ['#F0F0F0' , '#282A36' , '#66D2D6' , '#FBC740' , '#BD97CB' , '#FFD4DB'  , '#07BB9C']

def init_widgets() :
    widget_list = [
            widget.Spacer(
                length = 5) , 

            widget.Image(
                filename = '~/.config/qtile/linux_icon/Archlinux-icon-crystal-64.svg.png' , 
                margin = 2) ,

            widget.GroupBox(
                fontsize = 20 ,
                padding = 4 ,
                border_width = 8 , 
                highlight_method = 'text' , 
                inactive = colors[4] , 
                active = colors[2] , 
                this_current_screen_border  = colors[3]
                ),

            widget.Spacer( 
                lenght = bar.STRETCH) , 

            widget.GenPollText(
                func = get_time , 
                padding = 5 , 
                update_interval = 1 ,
                foreground = colors[3] , 
                ),

            widget.GenPollText(
                func = get_callender , 
                update_interval = 1 , 
                foreground = colors[4] , 
                mouse_callbacks = {'Button1' : lazy.spawn('notify-send sa')}) ,

            widget.TextBox(
                fontsize = 20 , 
                text = ' ' , 
                foreground = colors[4] , 
                padding = 7) ,


            widget.Spacer( 
                lenght = bar.STRETCH) , 
            
#            widget.TextBox(
#                fontsize = 17 , 
#                padding = 5 , 
#                text = '🖼',
#                foreground = colors[3], 
#                mouse_callbacks = {'Button1' : lazy.spawn("notify-send a")})  , 
            widget.GenPollText(
                func = MocpControll ,
                fontsize = 18 ,
                foreground = colors[4] , 
                padding = 5  ,
                update_interval = 1 ,
                mouse_callbacks = {'Button1' : lazy.spawn('mocp -P')} ,) , 


            widget.GenPollText(
                func = get_controller_charge , 
                update_interval = 0.1, 
                foreground = colors[3]) , 

            widget.Battery(
                show_short_text = False ,
                foreground = colors[2] ,
                full_char =  '🔋'  , 
                charge_char = '🔌', 
                discharge_char = '🥢',
                update_interval = 1 ,
                padding = 5 , 
                format = '{char} {percent:2.0%} ' ) , 

            widget.TextBox(
                    fontsize = 20 , 
                    padding = 7 , 
                    text = '墳' ,
                    mouse_callbacks = {'Button1' : lazy.spawn('pavucontrol')} ,
                    foreground = colors[4]) ,

            widget.Volume(
                    fmt = '{}' ,
                    foreground = colors[4]) , 

            widget.GenPollText(
                    func = get_current_keyboard_lan , 
                    update_interval=0.1 ,
                    padding = 10 ),

            widget.Systray(),

            widget.TextBox(
                    text = ' ' ,  
                    foreground = colors[3] ,
                    fontsize = 20 , 
                    padding = 5 , 
                    mouse_callbacks = {'Button1' : lazy.spawn('kitty -e bpytop')}), 

            widget.CPU(
                    format = '{load_percent}% ' , 
                    foreground = colors[3] , 
                    mouse_callbacks = {'Button1' : lazy.spawn('kitty-e bpytop')}) ,

            widget.TextBox(
                    fontsize = 20 , 
                    text = '﬙', 
                    foreground = colors[2],
                    padding = 5 ,
                    mouse_callbacks = {'Button1' : lazy.spawn('kitty -e bpytop')}), 

            widget.Memory(
                    format = '{MemPercent}%', 
                    foreground = colors[2] ,
                    mouse_callbacks = {'Button1' : lazy.spawn('kitty -e bpytop')}), 

            widget.Image(
                    filename = '~/.config/qtile/shutdown_icon/turn-off.png' ,
                    mouse_callbacks = {'Button1' : lazy.shutdown()} , 
                    foreground = colors[0] ) ]

    return widget_list



            


screens = [Screen( top=bar.Bar(init_widgets() , background = colors[1] ,size = 30 , margin = [5,10,5,10] ))]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='spectacle'),  #spectacle
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once() :
    home = os.path.expanduser('~') 
    call([home + '/.config/qtile/autostart'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Asuna"
