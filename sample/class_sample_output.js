class Test {
    foo(x = 1, b = "bar") {
        console.log(x)
    }

    bar(a = 1.23, b = 8.1) {
        return a + b
    }
}

t = new Test
t.foo(7)
console.log(t.bar())