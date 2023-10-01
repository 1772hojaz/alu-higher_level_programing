1. JavaScript Objects:
In JavaScript, an object is a collection of properties, and a property is an association between a name (or key) and a value. The value can be a primitive value, function, or another object.

Creating Objects:

You can create objects using the object literal syntax or the new keyword with a constructor.

2. Scopes:
In JavaScript, scope determines the accessibility of variables, objects, and functions from different parts of the code.

Global Scope: Variables declared outside a function are in the global scope and can be accessed from any part of the code.
Function Scope: Variables declared within a function are accessible only within that function.
Block Scope (ES6): With the introduction of let and const in ES6, it's now possible to have block-level scope, meaning a variable is limited in scope to the block, statement, or expression where it's defined.
3. Closures:
A closure is a feature in JavaScript where an inner function has access to the outer (enclosing) function's variables. This scope chain consists of:

The inner function's own scope (variables defined between its curly brackets).
The outer function's variables.
Global variables.
