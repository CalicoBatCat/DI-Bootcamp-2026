
import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []

        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size

        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("out of range")

        self.current_idx = page_num - 1


    def first_page(self):
        self.current_idx = 0


    def last_page(self):
        self.current_idx = self.total_pages - 1


    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1


    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1

items = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
pagination = Pagination(items, 6)

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(pagination.get_visible_items())

pagination.next_page()
print(pagination.get_visible_items())

pagination.last_page()
print(pagination.get_visible_items())

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

# p.go_to_page(10)
# print(p.current_idx + 1)
# Output: ValueError

# p.go_to_page(0)
