from extensionError import ExtensionError
from operations import MarkdownManager

print("MarkOrganizer")

# Input of manrkdown file
path = input("Enter the markdown file path:")
newPath = input("Enter the new markdown folder path:")

# Confirm file path
if (MarkdownManager.confirm(path)):
    # Create a markdown folder
    mdManager = MarkdownManager(path, newPath)
    mdManager.createMdFolder()

else:
    raise ExtensionError("Error: the file is not markdown")


