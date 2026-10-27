package com.semasem.lesson_4;

public class Main {

    public static void main(String[] args) {
        System.out.println("Задание 1");
        Dog dog = new Dog("Рекс", "Лабродор");
        System.out.println(dog.info());
        System.out.println(dog.speak());

        System.out.println("Задание 2");
        System.out.println(Student.isAdult(20)); // true
        Student s = new Student("Иван", 15);
        System.out.println(s.isAdult(20));

        Student studentFromStr = Student.fromString("Аня,20");
        System.out.println(studentFromStr);

        System.out.println("Задание 3");
        DigitalLibrary lib = new DigitalLibrary("pdf");
        lib.add(new Book("Война и мир", "Толстой", 1869));
        lib.add(new Book("Анна Каренина", "Толстой", 1878));
        lib.add(new Book("Преступление и наказание", "Достоевский", 1866));

        System.out.println(lib);
        System.out.println("Всего книг: " + lib.size());

        System.out.println("\nКниги Толстого:");
        for (Book b : lib.findByAuthor("Толстой")) {
            System.out.println(b);
        }
    }
}
