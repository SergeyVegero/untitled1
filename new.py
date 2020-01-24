a, b, c = "hello", 'world', 'one'
print(c, b, a)
glb_var = "global"
def var_function():
    lcl_var = "local"
    print(lcl_var)
    var_function()
    print(glb_var)
    