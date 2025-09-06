global_var = "I am a global variable"

class Demo:
    def show_variables(self):
        local_var = "I am a local variable"
        print("Inside method:")
        print(local_var)           
        print(global_var)          

demo_obj = Demo()
demo_obj.show_variables()
print("Outside class:")
print(global_var)                 