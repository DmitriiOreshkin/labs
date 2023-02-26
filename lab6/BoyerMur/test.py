from BoyerMur import search

string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

substr = 'Lorem'
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')

substr = ','
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')

substr = 'consectetur adipiscing elit'
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')

substr = 'do'
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')

substr = ' '
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')

substr = 'aliqua.'
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')

substr = 'qwertyqwert'
print(f'"{substr}" встречается в строке на позициях: {search(string, substr)}')
