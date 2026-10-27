package com.semasem.lesson_4;

public class Dog extends Animal {
    private final String breed;

    public Dog(String name, String breed) {
        super(name);
        this.breed = breed;
    }

    public String info() {
        return name + ", порода: " + breed;
    }

    @Override
    public String speak() {
        return super.speak() + " (Гав!)";
    }
}
