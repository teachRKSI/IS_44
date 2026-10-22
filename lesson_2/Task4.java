package com.semasem;

import java.util.Arrays;

public class Task4 {
    public static void main(String[] args) {
        task4_1();
        task4_2();
        task4_3();
        task4_4();
    }

    private static void task4_1() {
        String str = "  Java — это здорово!  ";
        String cleaned = str.trim().toLowerCase();
        System.out.println(cleaned);
        System.out.println(cleaned.length());
    }

    private static void task4_2() {
        String str = "яблоко,банан,вишня";
        String[] items = str.split(",");
        for (String item : items) {
            System.out.println(item.toUpperCase());
        }
    }

    private static void task4_3() {
        String str = "А роза упала на лапу Азора";
        String cleaned = str.replaceAll("\\s+", "").toLowerCase();
        String reversed = new StringBuilder(cleaned).reverse().toString();
        System.out.println(cleaned.equals(reversed));
    }

    private static void task4_4() {
        String str = "hello world";
        System.out.println(str.replace(" ", "_"));
    }
}