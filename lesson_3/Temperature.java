package com.semasem.lesson_3;

public class Temperature {
    private double celsius;

    public Temperature(double celsius) {
        if (celsius < -273.15) {
            throw new IllegalArgumentException();
        }
        this.celsius = celsius;
    }

    public void setCelsius(double celsius) {
        if (celsius < -273.15) {
            throw new IllegalArgumentException();
        }
        this.celsius = celsius;
    }

    public double getCelsius() {
        return this.celsius;
    }

    public double getFahrenheit() {
        return (this.celsius * 9/5) + 32;
    }
}
