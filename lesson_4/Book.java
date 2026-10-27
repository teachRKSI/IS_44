package com.semasem.lesson_4;

public class Book {
    private final String title;
    private final String author;
    private final int year;
    private boolean isRead;

    public Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
        this.isRead = false;
    }

    public Book(String title, String author, int year, boolean isRead) {
        this.title = title;
        this.author = author;
        this.year = year;
        this.isRead = isRead;
    }


    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getYear() {
        return year;
    }

    public boolean isRead() {
        return isRead;
    }

    public void setRead(boolean read) {
        isRead = read;
    }

    public void markAsReady() {
        this.isRead = true;
    }

    @Override
    public String toString() {
        return String.format("«%s» — %s (%d г.) [%s]",
                title, author, year, isRead ? "прочитана" : "не прочитана");
    }


}
