# Pa1_2025
Producto academico  1

```mermaid
classDiagram
direction TB
    class Animal {
	    +int age
	    +String gender
	    +isMammal()
	    +mate()
    }

    class Duck {
	    +String beakColor
	    +swim()
	    +quack()
    }

    class Fish {
	    -int sizeInFeet
	    -canEat()
    }

    class Zebra {
	    +bool is_wild
	    +run()
    }

    Animal <|-- Duck
    Animal <|-- Fish
    Animal <|-- Zebra

