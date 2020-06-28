class Test {

    constructor(x, y) {
        console.log("Hello")
        this.myvar = x + y
        console.log(this.myvar)
    }

    foo(x = 1, b = "bar") {
        console.log(x)
    }

    bar(a = 1.23, b = 8.1) {
        return a + b
    }
}

t = new Test(3, 6)
console.log(t.myvar)
t.foo(7)
console.log(t.bar())