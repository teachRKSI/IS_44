package com.semasem;

import java.util.*;

public class Task7 {
    public static void main(String[] args) {
        task7_1();
        task7_2();
        task7_3();
        task7_4();
    }

    private static void task7_1() {
        List<Integer> nums = List.of(4, 1, 7, 3);
        int sum = nums.stream().mapToInt(Integer::intValue).sum();
        int min = Collections.min(nums);
        int max = Collections.max(nums);
        List<Integer> sorted = new ArrayList<>(nums);
        Collections.sort(sorted);
        System.out.println("Сумма: " + sum + ", Мин: " + min + ", Макс: " + max + ", Отсортировано: " + sorted);
    }

    private static void task7_2() {
        List<Integer> nums = List.of(4, 1, 7, 3);
        for (int i = 0; i < nums.size(); i++) {
            System.out.println(i + ": " + nums.get(i));
        }
    }

    private static void task7_3() {
        List<String> names = List.of("Анна", "Борис");
        List<Integer> ages = List.of(20, 22);
        for (int i = 0; i < names.size(); i++) {
            System.out.println(names.get(i) + " - " + ages.get(i));
        }
    }

    private static void task7_4() {
        List<Integer> nums = List.of(4, 1, 7, 3);
        boolean hasGreaterThan10 = nums.stream().anyMatch(x -> x > 10);
        boolean allPositive = nums.stream().allMatch(x -> x > 0);
        System.out.println("Есть > 10: " + hasGreaterThan10);
        System.out.println("Все > 0: " + allPositive);
    }
}