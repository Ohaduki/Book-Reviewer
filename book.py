class Book:
    def __init__(self, title=None, author=None, summary=None, price=None, category=None, min_age=None, max_age=None):
        self.title = title
        self.author = author
        self.summary = summary
        self.price = price
        self.category = category
        self.min_age = min_age
        self.max_age = max_age

    def to_tuple(self):
        return self.title, self.author, self.summary, self.price, self.category, self.min_age, self.max_age
