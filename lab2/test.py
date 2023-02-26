from avl_map import AVLMap


map = AVLMap()


print("Добавим элемент 'hello' c ключом 1:")
map.set(1, 'hello')
print(f"После добавления элемента:")
map.inspect()

print()
print()

print("Добавим элемент 'a' c ключом 2:")
map.set(2, 'a')
print(f"После добавления элемента:")
map.inspect()

print()
print()

print("Добавим элемент 12334 c ключом 3:")
map.set(3, 12334)
print(f"После добавления элемента:")
map.inspect()

print()
print()

print("Добавим элемент False c ключом 4:")
map.set(4, False)
print(f"После добавления элемента:")
map.inspect()

print()
print()

print("Добавим элемент True c ключом 5:")
map.set(5, True)
print(f"После добавления элемента:")
map.inspect()

print()
print()

print("Добавим элемент 4.65 c ключом 6:")
map.set(6, 4.65)
print(f"После добавления элемента:")
map.inspect()

print()
print()

print("Изменим значение элемента по ключу 4 c False на True 6:")
map.change(4, True)
print(f"После изменения элемента:")
map.inspect()

print()
print()

print("Достанем значение элемента с ключом 3:")
print(f'map[3]={map.get(3)}')

print()


print("И изменим его на 'hello, world':")
map.change(3, 'hello, world')
print(f'map[3]={map.get(3)}')

print()

print("Удалим все эелементы:")
map.delete()
print(f"После удаления:")
map.inspect()

print()
