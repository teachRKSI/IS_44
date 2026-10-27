package com.semasem.lesson_3;

public class Vehicle {
    protected String brand;
    protected int year;

    public Vehicle(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }

    public String getInfo() {
        return String.format("%s, %d г.", brand, year);
    }
}

