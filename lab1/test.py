from priority_queue import PriorityQueue

q = PriorityQueue()

print("Добавим элемент 3")
q.add(3)
print("После добавления элемента: " + str(q.container))

print()


print("Добавим элемент 4")
q.add(4)
print("После добавления элемента: " + str(q.container))

print()


print("Добавим элемент 25")
q.add(25)
print("После добавления элемента: " + str(q.container))

print()


print("Добавим элемент 9")
q.add(9)
print("После добавления элемента: " + str(q.container))

print()


print("Добавим элемент 2")
q.add(2)
print("После добавления элемента: " + str(q.container))

print()


print(f"очередь содержит элементы: {q.container}")
print(f"пуста ли очередь?: {q.is_free()}")

print(f"максимальный элемент очереди: {q.max()}")
print(f"количество элементов в очереди: {q.quantity()}")

print()

print("Удалим элемент 4")
q.delete(4)
print(f"После удаления элемента: {q.container}")
print(f"количество элементов: {q.quantity()}")

print()

print("Удалим элемент 9")
q.delete(9)
print("После удаления элемента: " + str(q.container))
print(f"максимальный элемент: {q.max()}")
print(f"количество элементов: {q.quantity()}")

print()
