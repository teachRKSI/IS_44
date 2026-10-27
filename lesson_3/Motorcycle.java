package com.semasem.lesson_3;

public class Motorcycle extends Vehicle {
    int engineVolume;


    public Motorcycle(String brand, int year, int engineVolume) {
        super(brand, year);
        this.engineVolume = engineVolume;
    }

    @Override
    public String getInfo() {
        return super.getInfo() + String.format(", %d", engineVolume);
    }
}
