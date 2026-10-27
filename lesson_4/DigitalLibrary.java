package com.semasem.lesson_4;

public class DigitalLibrary extends Library {
    private final String format;

    public DigitalLibrary(String format) {
        this.format = format;
    }

    @Override
    public String toString() {
        return super.toString() + ", формат цифровой библиотеки: " + format;
    }
}
