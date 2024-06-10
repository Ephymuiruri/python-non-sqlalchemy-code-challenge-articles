class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title,str) and len(title)>=5 and len(title)<=50:
            self._title = title
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author,Author):
            self._author = author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine,Magazine) and magazine not in Article.all:
            self._magazine = magazine
        
class Author:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name,str) and not hasattr(self,'name'):
            self._name = name


    def articles(self):
        articles =[]
        for article in Article.all:
            if article.author == self:
                articles.append(article)
        return articles

    def magazines(self):
        magazines = set()
        for article in Article.all:
            if article.author == self:
                magazines.add(article.magazine)
        return list(magazines)
        
            

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        topic_areas = set()
        for article in Article.all:
            if article.author == self:
                topic_areas.add(article.magazine.category)
        return None if list(topic_areas) ==[] else list(topic_areas)

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name,str) and len(name)>=2 and len(name)<=16:
            self._name = name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category,str) and len(category)> 0:
            self._category = category

    def articles(self):
        articles = []
        for article in Article.all:
            if article.magazine == self:
                articles.append(article)
        return articles

    def contributors(self):
        authors = set()
        for article in Article.all:
            if article.magazine == self:
                authors.add(article.author)
        return list(authors)

    def article_titles(self):
        titles = []
        for article in Article.all:
            if article.magazine == self:
                titles.append(article.title)
        return None if titles == [] else titles
    def contributing_authors(self):
        author_list =[]
        for author in Article.all:
            if author.magazine == self:
                author_list.append(author.author)
        empt2=[]
        for author in author_list:
            if author_list.count(author) > 2:
                empt2.append(author)
        return empt2