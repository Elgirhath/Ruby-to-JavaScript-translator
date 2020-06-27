class Test
    def foo(x = 1, b = "bar")
        puts x 
    end
    
    def bar(a = 1.23, b = 8.1)
        return a + b
    end
end

t = Test.new
t.foo 7

puts t.bar