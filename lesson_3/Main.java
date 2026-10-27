package com.semasem.lesson_3;

import java.util.List;

public class Main {
    static void main(String[] args) {
        System.out.println("Задание 1");
        Temperature temperature = new Temperature(25);
        System.out.printf("C: %f, -> F: %f%n", temperature.getCelsius(), temperature.getFahrenheit());

        System.out.println("Задание 2");
        Vehicle car = new Car("Toyota", 2020, "бензин");
        Vehicle moto = new Motorcycle("Yamaha", 2018, 600);
        System.out.println(car.getInfo());
        System.out.println(moto.getInfo());

        System.out.println("Задание 3");
        List<Soundable> soundables = List.of(
                new Dog(),
                new Cat(),
                new Cow(),
                new Dog(),
                new Robot()
        );
        chorus(soundables);
    }

    private static void chorus(List<Soundable> animals) {
        for (Soundable animal : animals) {
            System.out.println(animal.sound());
        }
    }
}
