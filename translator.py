import tree_builder
import sys

def convert(tree):
    return tree.toJavaScript()

def translate(file_path):
    file = open(file_path, "r")
    text = file.read()

    tree = tree_builder.build_tree(text)
    js_code = convert(tree)

    file = open('out.js', 'w')
    file.write(js_code)
    file.close()

if __name__ == "__main__":
    translate(sys.argv[1])