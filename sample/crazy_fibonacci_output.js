function fibonacci(n = 1) {
    if (n == 1) {
        return 1
    } else if (n == 0) {
        return 1
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }

}

n = 0
x = [1, 2, 3, 4, 6, 7, 8, 9, 0, 4]
while (n < 10) {
    console.log((fibonacci(x[n]) % 5) ** 3)
    n += 1
}