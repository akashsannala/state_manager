class LinkNode:
    def __init__(self, url, text=None):
        self.url = url
        self.text = text
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print("  " * level + f"- [{self.text or self.url}]({self.url})")
        for child in self.children:
            child.display(level + 1)


# Example usage
root = LinkNode("https://example.com", "Home")

about_page = LinkNode("https://example.com/about", "About")
contact_page = LinkNode("https://example.com/contact", "Contact")
blog_page = LinkNode("https://example.com/blog", "Blog")

root.add_child(about_page)
root.add_child(contact_page)
root.add_child(blog_page)

# Adding sub-links under "Blog"
post1 = LinkNode("https://example.com/blog/post1", "First Post")
post2 = LinkNode("https://example.com/blog/post2", "Second Post")
blog_page.add_child(post1)
blog_page.add_child(post2)

# Display the tree structure
root.display()
