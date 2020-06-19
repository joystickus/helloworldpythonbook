import easygui
flavor = easygui.choicebox("What's your favourite ice cream flavor?",
                           choices = ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + flavor)
