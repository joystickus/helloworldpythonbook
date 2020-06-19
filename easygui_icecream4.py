import easygui
flavor = easygui.enterbox("What's your favourite ice cream flavor?",
                          default = 'Vanilla')
easygui.msgbox("You picked " + flavor)
