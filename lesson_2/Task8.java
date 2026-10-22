package com.semasem;

import java.util.Scanner;

public class Task8 {
    public static void main(String[] args) {
        task8_1();
        task8_2();
        task8_3();
    }

    private static void task8_1() {
        Scanner scanner = new Scanner(System.in);
        try {
            int num = Integer.parseInt(scanner.nextLine());
            System.out.println(num);
        } catch (NumberFormatException e) {
            System.out.println("Ошибка: введено не число");
        }
    }

    private static void task8_2() {
        Scanner scanner = new Scanner(System.in);
        try {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            System.out.println(a / b);
        } catch (ArithmeticException e) {
            System.out.println("Деление на ноль невозможно");
        }
    }

    private static void task8_3() {
        try {
            int x = Integer.parseInt("123");
            System.out.println("Успешно: " + x);
        } catch (NumberFormatException e) {
            System.out.println("Ошибка конвертации");
        } finally {
            System.out.println("Блок finally выполняется всегда");
        }
    }
}