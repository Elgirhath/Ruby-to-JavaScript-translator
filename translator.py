import tree_builder
import sys

def convert(tree):
    print(tree)
    print("\n")
    return tree.toJavaScript()

def translate(file_path):
    file = open(file_path, "r")
    text = file.read()
    tree = tree_builder.build_tree(text)
    js_code = convert(tree)
    print(js_code)

if __name__ == "__main__":
    translate(sys.argv[1])