class Test
    attr_reader :myvar
    def initialize(x, y)
        puts "Hello"
        @myvar = x + y
        puts @myvar
    end

    def foo(x = 1, b = "bar")
        puts x 
    end
    
    def bar(a = 1.23, b = 8.1)
        return a + b
    end
end

t = Test.new(3, 6)

puts t.myvar
t.foo 7

puts t.bar()