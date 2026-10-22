package com.semasem;

import java.util.*;

public class Task3 {
    public static void main(String[] args) {
        task3_1();
        task3_2();
        task3_3();
        task3_4();
    }

    private static void task3_1() {
        List<Integer> nums = new ArrayList<>(List.of(1, 2, 2, 3, 4, 4, 5, 1));
        Set<Integer> unique = new HashSet<>(nums);
        List<Integer> sortedList = new ArrayList<>(unique);
        sortedList.sort(Collections.reverseOrder());
        System.out.println(sortedList);
    }

    private static void task3_2() {
        List<Integer> nums = List.of(1, 2, 2, 3, 4, 4, 5, 1);
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        System.out.println(counts);
    }

    private static void task3_3() {
        List<Integer> a = List.of(1, 2, 3, 4);
        List<Integer> b = List.of(3, 4, 5, 6);

        Set<Integer> intersection = new HashSet<>(a);
        intersection.retainAll(b);

        Set<Integer> onlyA = new HashSet<>(a);
        onlyA.removeAll(b);

        Set<Integer> allUnique = new HashSet<>(a);
        allUnique.addAll(b);

        System.out.println("Пересечение: " + intersection);
        System.out.println("Только из a: " + onlyA);
        System.out.println("Все уникальные: " + allUnique);
    }

    private static void task3_4() {
        Map<String, Integer> grades = Map.of("Анна", 5, "Борис", 3, "Вика", 4);
        for (Map.Entry<String, Integer> entry : grades.entrySet()) {
            if (entry.getValue() >= 4) {
                System.out.println(entry.getKey());
            }
        }
    }
}