from db import BASE, engine, session
from models import Student, Book, Author
from navigation_menu import navigation_menu
import actions
import sys

navigation_stack = [] # stack
current_menu = navigation_menu

def diplay_options(menu):
        
        print("Select an option by typing the number:")
        for key in menu.keys():
                print("%s: %s" % (key, menu[key]["request"]))
        
        if len(navigation_stack) > 0:
                print("\n0: Go back\n00: Main Menu")
                
        return input()

# Instead of using the selection, lets push the menu to the stack
def application():
        global navigation_menu, navigation_stack, current_menu
        
        if(current_menu.get("options")):
                current_menu = current_menu.get("options")
         
        if current_menu.get("fields"):
                print("Setting fields")
                fields = current_menu["fields"]
                field_count=0
                data={}
                while field_count < len(fields):
                        field = fields[field_count]
                        instruction = field["instruction"]
                        data[field["field"]] = input( f"{instruction}: " )
                        if(field.get("func")):
                                data[field["field"]] = field["func"](data[field["field"]])
                        field_count += 1
                
                # Call the action for this data
                action = current_menu["action"]
                getattr(actions, action)(data)
                # actions[action](data)
                
                # Go back
                navigation_stack.pop(-1)
                
        else:
                user_selection = diplay_options(current_menu)
                
                # Check if is going back
                if user_selection == "0": navigation_stack.pop(-1)
                # Check if it goin to main menu
                elif user_selection == "00": navigation_stack = []
                # Go to the next option
                else: navigation_stack.append( current_menu[int(user_selection)] )
                # current_menu = current_menu.get(navigation_stack[-1])
                
        if len(navigation_stack) > 0:
                current_menu = navigation_stack[-1]
        else: current_menu = navigation_menu
                
if __name__ == "__main__":
    while True:
            application()