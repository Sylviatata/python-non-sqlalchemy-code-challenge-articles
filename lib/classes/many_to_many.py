class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.author = author
        self.magazine = magazine
        self._title = title  # Use a private attribute to store the title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Article title is immutable")

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass