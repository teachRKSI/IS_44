package com.semasem;

import java.util.Random;

public class Task10 {
    public static void main(String[] args) {
        task10_1();
        task10_2();
        task10_3();
    }

    private static void task10_1() {
        System.out.println(Math.sqrt(144));
        System.out.println(Math.PI);
    }

    private static void task10_2() {
        Random random = new Random();
        System.out.println(random.nextInt(100) + 1);
    }

    private static void task10_3() {
        customMethod();
    }

    private static void customMethod() {
        System.out.println("Вызов из метода main");
    }
}