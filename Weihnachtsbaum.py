#Weihnachtsbaum/Christmastree

def christmas_tree(width, height):
    draw = "**"
    for i in range(1, height + 1):
        christmas_tree_symbol = draw * i
        print(christmas_tree_symbol.center(100))
    c_tree_stump = draw
    print(c_tree_stump.center(100))
        
christmas_tree(10,10)