package com.semasem;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Task6 {
    public static void main(String[] args) {
        task6_1();
        task6_2();
        task6_3();
        task6_4();
    }

    private static void task6_1() {
        List<Integer> squares = IntStream.rangeClosed(1, 10)
                .map(x -> x * x)
                .boxed()
                .toList();
        System.out.println(squares);
    }

    private static void task6_2() {
        List<Integer> nums = List.of(1, -2, 3, -4, 5, -6);
        List<Integer> positive = nums.stream()
                .filter(x -> x > 0)
                .toList();
        System.out.println(positive);
    }

    private static void task6_3() {
        Map<Integer, Integer> map = IntStream.range(0, 5)
                .boxed()
                .collect(Collectors.toMap(x -> x, x -> x * x));
        System.out.println(map);
    }

    private static void task6_4() {
        String str = "quick brown fox";
        List<Integer> lengths = Arrays.stream(str.split(" "))
                .map(String::length)
                .toList();
        System.out.println(lengths);
    }
}