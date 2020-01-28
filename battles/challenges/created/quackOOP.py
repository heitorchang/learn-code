desc = """

You are given a hierarchy of classes in the single-inheritance language **Schmython** and an accompanying program. Being a simple language, a class and its methods can be defined in a single line, using a statement such as:

```
class MyClass(MyParent): ['aMethod', 'anotherMethod']
```

`MyParent` may be empty if the class has no ancestor. When using this simplified syntax, each method will simply print a string:

```
"ClassNameOfObject will methodName"
```

An object is created with the statement `objectName = ClassName()`. Nothing is printed after this kind of statement.

An object's method is called in this manner: `someObject.doAction()`.

When calling an object's method, this object's class' method is called if it exists. Otherwise, the inheritance tree will be followed until a matching method (by name) is found. 

**Important Note:** When the method belongs to an ancestor, the calling object's class name will be printed, not the name of the ancestor class actually containing the method.

If no method is found in this inheritance chain, the string `"NoSuchMethodException"` is printed. The execution of the program is not interrupted.

__Example__

For 

```classDefs:
["class Bird(): ['walk', 'fly', 'eat']",
 "class Duck(Bird): ['quack']",
 "class Mallard(Duck): ['quack', 'swim']"]

program:
["daffy = Duck()",
 "jonas = Mallard()",
 "jonas.quack()",
 "daffy.quack()",
 "daffy.swim()",
 "jonas.eat()"]
```

The expected output is:

```
["Mallard will quack",
 "Duck will quack",
 "NoSuchMethodException", 
 "Mallard will eat"]
```

Explanation:

`jonas` is a Mallard, which overrides the Duck's `quack`. So, `"Mallard will quack"` is printed.

Then, `daffy`, being a Duck, calls its own class' method.

Ducks (and their ancestors) do not define `swim`, so the error is printed.

Finally, when `jonas` wants to `eat`, the method of its ancestor, Bird, will be called. However, the calling object, `jonas`, is a Mallard, so `"Mallard will eat"` is printed.

"""


def methnames2defs(strs):
    out = ""
    for s in strs:
        out += """
    def {}(self):
        return "{{}} will {}".format(self.__class__.__name__)
""".format(s, s)
    return out
        

def quack(classDefs, program):
    defcode = ""
    
    for clstr in classDefs:
        if len(clstr) > 1:
            cls, actions = clstr.split(": ")
            defcode += '\n' + cls + ":\n"
            # print(actions)
            defcode += methnames2defs(eval(actions))

    # print(defcode)
    exec(defcode)

    out = []
    for prstr in program:
        try:
            if '=' in prstr:
                exec(prstr)
            else:
                s = eval(prstr)
                out.append(s)
        except AttributeError:
            out.append("NoSuchMethodException")

    # print(out)
    return out


pairtest(quack(["class Bird(): ['walk', 'fly', 'eat']", 
 "class Duck(Bird): ['quack']", 
 "class Mallard(Duck): ['quack', 'swim']"],
["daffy = Duck()", 
 "jonas = Mallard()", 
 "jonas.quack()", 
 "daffy.quack()", 
 "daffy.swim()", 
 "jonas.eat()"]),
         ["Mallard will quack", 
 "Duck will quack", 
 "NoSuchMethodException", 
 "Mallard will eat"],

         quack(["class Bird(): ['walk', 'fly', 'eat']", 
 "class Duck(Bird): ['quack']", 
 "class Mallard(Duck): ['quack', 'swim']"],
["daffy = Duck()", 
 "jonas = Mallard()",
 "brett = Bird()",
 "brett.fly()", 
 "brett.swim()",
 "jonas.walk()"]),

         ["Bird will fly",
          "NoSuchMethodException",
          "Mallard will walk"],
         

         quack(["class LivingThing(): ['grow', 'perish']",
                "class Vegetable(LivingThing): ['photosynthesize', 'absorbWater']",
                "class Animal(LivingThing): ['move', 'eat', 'defecate']",
                "class Invertebrate(Animal): ['slither']",
                "class Mammal(Animal): ['nurse', 'run']",],

               ["cabbage = Vegetable()",
                "leopard = Mammal()",
                "cabbage.grow()",
                "slug = Invertebrate()",
                "slug.run()",
                "leopard.perish()"]),

         ['Vegetable will grow', 'NoSuchMethodException', 'Mammal will perish'],
         

         quack(["class LivingThing(): ['grow', 'perish']",
                "class Vegetable(LivingThing): ['photosynthesize', 'absorbWater']",
                "class Animal(LivingThing): ['move', 'eat', 'defecate']",
                "class Invertebrate(Animal): ['slither']",
                "class Mammal(Animal): ['nurse', 'run']",],

               ["amoeba = LivingThing()",
                "oyster = Invertebrate()",
                "amoeba.perish()",
                "oyster.slither()",
                "oyster.absorbWater()",
                "elephant = Mammal()",
                "elephant.photosynthesize()",
               ]),

         ["LivingThing will perish",
          "Invertebrate will slither",
          "NoSuchMethodException",
          "NoSuchMethodException"],
         
         quack(["class Programmer(): ['code', 'drinkCoffee']",
                "class Noob(Programmer): ['useGlobals']",
                "class ScriptKiddie(Noob): ['copyScripts']",
                "class Professional(Programmer): ['consumeAPIs']",
                "class Hacker(Programmer): ['magic']"],

               ["k = ScriptKiddie()",
                "h = Hacker()",
                "k.drinkCoffee()",
                "h.magic()",
                "k.magic()"
               ]

               ),
         
                ["ScriptKiddie will drinkCoffee", "Hacker will magic", "NoSuchMethodException"],

         quack(["class Muse(): ['inspire']",
                "class Idol(Muse): ['perfect']",
                "class Artist(Idol): ['perform']",
                "class Human(Artist): ['do']"],

               ["h = Human()",
                "h.perfect()"]),

               ["Human will perfect"],

         quack(["class Muse(): ['inspire']",
                "class Idol(Muse): ['perfect']",
                "class Artist(Idol): ['perform']",
                "class Human(Artist): ['do']"],

               ["h = Human()",
                "i = Idol()",
                "h.perfect()",
                "i.do()",
                "h.inspire()"]),

         ["Human will perfect", "NoSuchMethodException", "Human will inspire"]
         
               
        )
