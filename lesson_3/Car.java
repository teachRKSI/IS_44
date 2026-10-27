package com.semasem.lesson_3;

public class Car extends Vehicle {
    String fuelType;

    public Car(String brand, int year, String fuelType) {
        super(brand, year);
        this.fuelType = fuelType;
    }

    @Override
    public String getInfo() {
        return super.getInfo() + String.format(", %s", this.fuelType);
    }
}


