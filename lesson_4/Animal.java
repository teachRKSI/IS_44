package com.semasem.lesson_4;

public class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public String speak() {
        return name + " издаёт звук";
    }
}
