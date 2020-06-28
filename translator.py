import tree_builder
import sys
import jsbeautifier

def convert(tree):
    return tree.toJavaScript()

def translate(file_path):
    file = open(file_path, "r")
    text = file.read()

    tree = tree_builder.build_tree(text)
    js_code = convert(tree)

    beautified_code = jsbeautifier.beautify(js_code)

    file = open('out.js', 'w')
    file.write(beautified_code)
    file.close()


if __name__ == "__main__":
    translate(sys.argv[1])