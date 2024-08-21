# oops

THIS FILE CONTAINS NOTES ON OOPS 
Hierarchy: The hierarchy can be visualized as Class > Object > Instance. 
A class acts as a blueprint, an object is an actual entity built from the blueprint, and an instance is a particular occurrence of that object.

@classmethod
--> this function transforms the regular instance method to a classmethod
--> the main diffrence between instance method and a classmethod is that:
-->INSTANCE METHOD : is bound to the bound to an instance and has access to instance attributes
--> CLASS METHOD : is bound to the class and has access to the class attributes
---EXPLAIN CLASSMETHOD TO A CHILD---
-->Imagine you have a toy factory that makes different types of toys: cars, dolls, and robots.  The factory itself has a big list of all the toys it has ever made.
Now, you want to make a new car toy. You wouldn't ask a specific car toy to make another car, right? You would tell the factory, "Hey factory, make me a new car!" The factory knows how to make cars, so it would create one and add it to its big list of all toys.
In Python code, the @classmethod is like saying "Hey factory!" It's a way to tell the whole class (the toy factory) to do something, like create a new toy.

THE __INIT__ METHOD
-->explanation to a child : Imagine you have a toy robot, and every time you get a new one, you need to give it a name and a color. The __init__ method is like the instructions you follow when you first get the robot. When you create a new robot, you tell it, “Your name is Robbie, and your color is blue.” This way, every new robot knows its name and color right from the start.
-->to an expert : The __init__ method in Python is a special method, also known as a constructor, that is automatically invoked when a new instance of a class is created. Its primary role is to initialize the instance’s attributes and perform any setup required for the object.

//SELF KEYWORD

-->self parameter is not a keyword its just a convention , you can use any other word also.
-->it used to instance methods to refer to the instance of the class to which the method is called on.
-->the primary purpose of self is to access and modify the instance's state.
-->self provides a way to access the instance's attributes and methods from within the class.


THE DIFFRENCE BETWEEN __NEW__ AND __INIT__ Methods

->Both __new__ and __init__ methods are used to object created but occurs at different stages of object's life cycle.
->The __new__ method is called first and the __init__ method is called right after the __new__ is called.

THE __NEW__ METHOD
->The __new__ mehtod is a static method is responsible for creating anf returning a new instance of the class.
->ROLE : it allocates memory for new object and returns the new instance of the class.
        -> this method is useful whe you need to control the object creation process. To maybe allocate the memory resourcefully.
-> Return Type : it can return any type of object not just the instance of the class.

THE __INIT__ METHOD
-> the __init__ method is an instance method taht is rsponsible for setting attributes for the newly created object.
-> it is called right after the __new__ method
->Return Type : it should return NONE as its work is only to set attributes for the newly created object.
 