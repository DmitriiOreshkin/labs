from b_map import BTreeMap


tree = BTreeMap()

print('Добавим три элемента с ключами 1, 2, 3:')
print()

tree.insert(1, 'hello')
tree.insert(2, 'hello1')
tree.insert(3, 'hello3')

print(tree.search(1))
print(tree.search(2))
print(tree.search(3))

print()
tree.delete(3)
print('После удаление элемента с ключом 3:')
print()

print(tree.search(1))
print(tree.search(2))
print(tree.search(3))