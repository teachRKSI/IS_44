package com.semasem;

import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        task2_1();
        task2_2();
        task2_3();
        task2_4();
    }

    private static void task2_1() {
        for (int i = 1; i <= 20; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }

    private static void task2_2() {
        int i = 1;
        while (i <= 20) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
            i++;
        }
    }

    private static void task2_3() {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        System.out.println(sum);
    }

    private static void task2_4() {
        StringBuilder result = new StringBuilder();
        for (int i = 1; i <= 100; i++) {
            if (i % 7 == 0 && i % 5 != 0) {
                result.append(i).append(" ");
            }
        }
        System.out.println(result.toString().trim());
    }
}