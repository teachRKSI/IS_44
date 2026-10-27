package com.semasem.lesson_4;

public record Student(String name, int age) {
    public static String university = "МГУ";

    public static boolean isAdult(int age) {
        return age >= 18;
    }

    public static Student fromString(String s) {
        String[] parts = s.split(",");
        return new Student(parts[0].trim(), Integer.parseInt(parts[1].trim()));
    }
}