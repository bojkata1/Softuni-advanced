from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
         return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11 + "\n"
        res = separator
        for page in self.photos:
            res += " ".join(["[]" for _ in page]) + "\n"
            res += separator
        return res.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

test = PhotoAlbum.from_photos_count(12)
a = 5