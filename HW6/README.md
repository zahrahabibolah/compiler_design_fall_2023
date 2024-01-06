# All entities in Create/Couple/Declare

- in this HW we eant to see all entities from Create.createby/Couple.coupleby/Declare.declarein  in openunderstand and understand

### `Java Couple and Coupleby`
- Indicates a coupling link as counted in the OO coupling metrics. A link is created from a class to any external class (a class that is not in the extends/implements hierarchy) that is referenced.
  ```bash
   public class c1 {
    ... 
  }
  public class c2 {
   cl obj;
  }
| Reference kind string | Entity performing references	 | Entity being referenced |
|-----------------------|-------------------------------|-------------------------|
| Java Couple           | c2                            | c1                      |
| Java Coupleby         | c1                            | c2                      |


### `Java Extend Couple and Extendby Coupleby`
- Indicates one class or interface extends another. This extends relation is used when the extended class is in a file that is part of the project. If the extended class was found in a classpath .jar file, the relation is Java Extend Couple External. If the Indicates class implicitly extends the java.lang.Object class, the relation is Java Extend Couple Implicit.

- [ ] Todo: add a short definition with and an example code and corresponding table for Java Extend Couple Implicit External and Java Extendby Coupleby Implicit External reference kind.
  ```bash
  // Example 1:
  class class1 {
   ...
  }
  class class2 extends class1 {
   ...
  }
  // Example 2:
  class some_class extends java.io.Writer {
   ...
  }
  // Example 3:
  class some_class {
   ...
  }
  // Example 4:
  //Todo

| Reference kind string                     | Entity performing references	 | Entity being referenced |
|-------------------------------------------|-------------------------------|-------------------------|
| Java Extend Couple	                       | Ex 1: class2	                 | Ex 1: class2            |
| Java Extendby Coupleby	                   | Ex 1: class1	                 | Ex 1: class1            |
| Java Extend Couple External	              | Ex 2: some_class	             | Ex 2: java.io.Writer    |
| Java Extendby Coupleby External	          | Ex 2: java.io.Writer	         | Ex 2: some_class        |
| Java Extend Couple Implicit	              | Ex 3: some_class	             | Ex 3: java.lang.Object  |
| Java Extendby Coupleby Implicit           | 	Ex 3: java.lang.Object	      | Ex 3: some_class        |
| Java Extend Couple Implicit External	     | Todo	                         | Todo                    |
| Java Extendby Coupleby Implicit External	 | Todo                          | 	Todo                   |


### `Java Implement Couple and Implementby Coupleby`
- Indicates a class implements an interface.
  ```bash
  interface some_interface {
   ...
  }

  class some_class implements some_interface {
   ...
  }

|Reference kind string	      | Entity performing references	 | Entity being referenced |
|----------------------------|-----------------|-------------|
| Java Implement Couple      | some_class	| some_interface |
| Java Implementby Coupleby	 | some_interface  | some_class |


### `Java Create and Createby`
- Indicates that an instance of a class is created (new operator) in a scope.
  ```bash
  class c1 {
   ...
  }

  class c2 {
   c1 a = new c1();
  }

| Reference kind string	 | Entity performing references | 	Entity being referenced |
|------------------------|----------------------------|-----------------|
| Java Create            | c2                         | c1              |
| Java Createby          | c1                         | c2              |


### `Java Declare and Declarein`
- Indicates that a package is declared in a file or in a (parent) package.

![](https://m-zakeri.github.io/OpenUnderstand/figs/Declare-Declarein-example.png)
    ```bash
      
    ackage technology.tabula.debug;

    import java.awt.BasicStroke;
    import java.awt.Color;

    class Debug {
     ...
    }
| Reference kind string	 | Entity performing references        | 	Entity being referenced |
|------------------------|-------------------------------------|-------------------|
| Java Declare           |	Debug.java|	technology, technology.tabula.debug|
| Java Declarein	        | technology, technology.tabula.debug | 	Debug.java       |

## how to use 
![0](D:\ME\11111.png)

# Output/Input
## Output in OpenUnderstand
![1](D:\ME\333.png)

## Output in Understand

![2](C:\Users\black\Downloads\photo_5818699192019829995_y.jpg)
![3](C:\Users\black\Downloads\photo_5818699192019830010_w.jpg)
