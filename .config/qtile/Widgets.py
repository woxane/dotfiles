from datetime import datetime
from libqtile import widget , bar
from libqtile.lazy import lazy 
from subprocess import check_output 
from qtile_extras.widget import UPowerWidget 
def Widgets() :
    
    ## Arrays
    Colors = ['#F0F0F0' , '#282A36' , '#66D2D6' , '#FBC740' , '#BD97CB' , '#FFD4DB'  , '#07BB9C' , 'D8C4B6' , '9EB384']

    
    ## Funcitons 
    def GetTime() :
        return datetime.now().strftime('%H:%M') 

    def GetCallender() :
        return  check_output(["jdate" , "+'%h-%b-%d'"]).decode().strip()[1:-1] 


    def KeyboardLan() :
        output = check_output(['xkblayout-state' , 'print' , '%s']).decode() # give the current keyboard layout
        return output

    WidgetList = [

            widget.Spacer(length = 5) , 

            widget.Image(filename = '~/.config/qtile/Icon/ArchLinux.png' , margin = 2) ,

            widget.GroupBox(
                font = 'JetBrains Mono' , 
                fontsize = 16 ,
                padding = 1 ,
                border_width = 8, 
                highlight_method = 'text' , 
                inactive = Colors[7] , 
                active = Colors[7] , 
                this_current_screen_border  = Colors[8]
                ),
            
            widget.Moc(
                max_chars = 40 , 
                play_color = Colors[7] , 
                noplay_color = Colors[8] , 
                ) , 

            widget.Spacer( 
                lenght = bar.STRETCH) , 

            widget.GenPollText(
                func = GetTime, 
                padding = 5 ,
                fontsize = 14 , 
                update_interval = 60 ,
                foreground = Colors[7] , 
                ),




            widget.Spacer( 
                lenght = bar.STRETCH) , 
            
#            widget.TextBox(
#                fontsize = 17 , 
#                padding = 5 , 
#                text = '🖼',
#                foreground = Colors[3], 
#                mouse_callbacks = {'Button1' : lazy.spawn("notify-send a")})  , 
            widget.Systray(),

            UPowerWidget(
                border_charge_colour = Colors[8] , 
                ), 


            widget.TextBox(
                    fontsize = 17 , 
                    padding = 1 , 
                    text = ' 墳' ,
                    mouse_callbacks = {'Button1' : lazy.spawn('pavucontrol')} ,
                    foreground = Colors[7]) ,

            widget.Volume(
                    fmt = '{} ' ,
                    foreground = Colors[7]) , 

            widget.GenPollText(
                    func = KeyboardLan , 
                    foreground = Colors[7],
                    fontsize = 14 , 
                    update_interval=0.1 ,
                    padding = 5 ,
                    # Sometimes that my keyboard gets disconected the keyboard setting get reset
                    mouse_callbacks = {'Button1' : lazy.spawn('setxkbmap -option grp:alt_shift_toggle -layout us,ir')}
                    ),


            widget.TextBox(
                    text = ' ' ,  
                    foreground = Colors[7] ,
                    fontsize = 17 , 
                    padding = 0 , 
                    mouse_callbacks = {'Button1' : lazy.spawn('alacritty bpytop')}), 

            widget.CPU(
                    format = '{load_percent:.0f}% ' , 
                    foreground = Colors[7] , 
                    mouse_callbacks = {'Button1' : lazy.spawn('alacritty bpytop')}) ,

            widget.TextBox(
                    fontsize = 17 , 
                    text = '﬙', 
                    foreground = Colors[7],
                    padding = 0 ,
                    mouse_callbacks = {'Button1' : lazy.spawn('alacritty bpytop')}), 

            widget.Memory( 
                    format = '{MemPercent:.0f}%  ', 
                    foreground = Colors[7] ,
                    mouse_callbacks = {'Button1' : lazy.spawn('alacritty bpytop')}), 

            widget.Image(filename = '~/.config/qtile/Icon/Power-Key.png' ,mouse_callbacks = {'Button1' : lazy.shutdown()} , foreground = Colors[0])  , 
            

            ]
    
    return WidgetList
    
