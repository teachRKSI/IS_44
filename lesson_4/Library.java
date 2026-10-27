package com.semasem.lesson_4;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Library implements Iterable<Book> {
    protected List<Book> books = new ArrayList<>();

    public void add(Book book) {
        books.add(book);
    }

    public List<Book> findByAuthor(String author) {
        return this.books.stream().filter(book -> book.getAuthor().equals(author)).toList();
    }

    public List<Book> unread() {
        return this.books.stream().filter(book -> !book.isRead()).toList();
    }

    public int size() {
        return books.size();
    }



    @Override
    public Iterator<Book> iterator() {
        return books.iterator();
    }

    @Override
    public String toString() {
        return "Библиотека содержит книг: " + books.size();
    }
}
