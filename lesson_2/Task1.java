package com.semasem;

import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        task1_1();
        task1_2();
        task1_3();
    }

    private static void task1_1() {
        String name = "Иван";
        int age = 20;
        double height = 1.80;
        System.out.printf("Меня зовут %s, мне %d лет, мой рост %.2f м.%n", name, age, height);
    }

    private static void task1_2() {
        String a = "5";
        int b = 5;
        System.out.println(a + b);
    }

    private static void task1_3() {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        System.out.println(x + y);
    }
}