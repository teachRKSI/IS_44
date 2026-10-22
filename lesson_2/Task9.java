package com.semasem;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;

public class Task9 {
    public static void main(String[] args) {
        task9_1();
        task9_2();
        task9_3();
    }

    private static void task9_1() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("hello.txt"))) {
            writer.write("Привет, мир!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void task9_2() {
        try {
            String content = Files.readString(Path.of("hello.txt"));
            System.out.println(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void task9_3() {
        try (BufferedReader reader = new BufferedReader(new FileReader("hello.txt"))) {
            String line;
            int lineNumber = 1;
            while ((line = reader.readLine()) != null) {
                System.out.println(lineNumber++ + ": " + line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}