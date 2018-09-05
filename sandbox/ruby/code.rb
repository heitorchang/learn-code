puts "My code"

class Code
  def initialize(name)
    @name = name.capitalize
  end

  def sayHi
    puts "Hello #{@name}!"
  end
end

hello = Code.new("tim")
hello.sayHi
