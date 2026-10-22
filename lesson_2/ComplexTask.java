package com.semasem;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class ComplexTask {
    public static void main(String[] args) {
        Map<String, List<Integer>> students = Map.of(
                "Анна", List.of(4, 5, 3, 4),
                "Борис", List.of(3, 3, 2, 5),
                "Вика", List.of(5, 5, 5, 5),
                "Глеб", List.of(2, 3, 4, 3)
        );

        Map<String, Double> averages = calculateAverages(students);
        String bestStudent = findBestStudent(averages);
        List<String> excellent = findExcellent(averages);
        List<String> withTwos = findStudentsWithTwos(students);

        System.out.println("Средние баллы: " + averages);
        System.out.println("Лучший студент: " + bestStudent);
        System.out.println("Отличники: " + excellent);
        System.out.println("Есть двойки у: " + String.join(", ", withTwos));

        saveReport("report.txt", averages, bestStudent);
    }

    /**
     * Вычисляет средний балл каждого студента.
     */
    public static Map<String, Double> calculateAverages(Map<String, List<Integer>> students) {
        Map<String, Double> averages = new LinkedHashMap<>();
        for (var entry : students.entrySet()) {
            double avg = entry.getValue().stream()
                    .mapToInt(Integer::intValue)
                    .average()
                    .orElse(0.0);
            averages.put(entry.getKey(), avg);
        }
        return averages;
    }

    public static String findBestStudent(Map<String, Double> averages) {
        return Collections.max(averages.entrySet(), Map.Entry.comparingByValue()).getKey();
    }

    public static List<String> findExcellent(Map<String, Double> averages) {
        return averages.entrySet().stream()
                .filter(e -> e.getValue() >= 4.5)
                .map(Map.Entry::getKey)
                .toList();
    }

    public static List<String> findStudentsWithTwos(Map<String, List<Integer>> students) {
        return students.entrySet().stream()
                .filter(e -> e.getValue().contains(2))
                .map(Map.Entry::getKey)
                .toList();
    }

    public static void saveReport(String filename, Map<String, Double> averages, String bestStudent) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            for (var entry : averages.entrySet()) {
                writer.write(entry.getKey() + ": " + entry.getValue() + "\n");
            }
            writer.write("Лучший студент: " + bestStudent + "\n");
        } catch (IOException e) {
            System.err.println("Ошибка при записи файла: " + e.getMessage());
        }
    }
}