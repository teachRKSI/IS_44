package com.semasem;

import java.util.*;
import java.util.function.Function;

public class Task5 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(calculateStats(List.of(1.0, 5.0, 3.0))));
        System.out.println(isPrime(7));
        System.out.println(countWords("hello world hello"));
        System.out.println(applyTwice(x -> x + 3, 5));
    }

    public static Double[] calculateStats(List<Double> numbers) {
        if (numbers == null || numbers.isEmpty()) {
            return new Double[]{null, null, null};
        }
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        return new Double[]{min, max, sum / numbers.size()};
    }

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static Map<String, Integer> countWords(String text) {
        Map<String, Integer> map = new HashMap<>();
        String[] words = text.split("\\s+");
        for (String w : words) {
            map.put(w, map.getOrDefault(w, 0) + 1);
        }
        return map;
    }

    public static int applyTwice(Function<Integer, Integer> func, int x) {
        return func.apply(func.apply(x));
    }
}