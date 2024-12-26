
# ultimate_pads = [['x^A', '<v>'], ['x^A', '<v>'], ['789', '456', '123', 'x0A']]


numpad = ['789', '456', '123', 'x0A']
keypad = ['x^A', '<v>']

ultimate_pads = [keypad for _ in range(25)] + [numpad]
print(ultimate_pads)