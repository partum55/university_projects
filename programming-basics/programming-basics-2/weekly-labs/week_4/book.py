"""Temp"""


class Book:
    """Temp"""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.bookmarked_page = None

    def turn_page(self, pages):
        self.current_page = max(1, min(self.current_page + pages, self.pages))

    def get_current_page(self):
        return self.current_page

    def get_bookmarked_page(self):
        return self.bookmarked_page

    def place_bookmark(self):
        self.bookmarked_page = self.current_page

    def turn_to_bookmark(self):
        if self.bookmarked_page:
            self.current_page = self.bookmarked_page

    def remove_bookmark(self):
        self.bookmarked_page = None

    def __str__(self):
        return (f"Book<{self.title} by {self.author}: {self.pages} "
                f"{"pages" if self.pages > 1 else "page"}, currently on page {self.current_page}"
                f"{f", page {self.bookmarked_page} bookmarked" if self.bookmarked_page else ""}>")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.author == other.author and
                self.pages == other.pages and
                self.current_page == other.current_page and
                self.bookmarked_page == other.bookmarked_page)
