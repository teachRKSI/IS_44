package com.semasem.lesson_5;

import javax.swing.*;
import java.awt.*;
import java.util.concurrent.atomic.AtomicInteger;

public class AppOne {
    static void main(String[] args) {

        AtomicInteger counter = new AtomicInteger();

        JFrame frame = new JFrame("Тестовое окошка");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setLayout(new GridLayout(4, 1));

        JTextField field = new JTextField("");

        JButton helloBtn = new JButton("Поздороваться");

        JButton clearBtn = new JButton("Сбросить");

        JLabel label = new JLabel("");

        frame.add(field, Component.TOP_ALIGNMENT);

        frame.add(helloBtn, Component.CENTER_ALIGNMENT);

        frame.add(label, Component.BOTTOM_ALIGNMENT);

        frame.add(clearBtn, Component.BOTTOM_ALIGNMENT);

        frame.setVisible(true);

        helloBtn.addActionListener(_ -> {
            String name = field.getText().trim();
            if (name.isBlank()) {
                label.setText("Сначала введите имя");
            } else {
                int currentCount = counter.incrementAndGet();
                label.setText(String.format("Привет, %s! Это ваше %d приветствие", name, currentCount));
            }
        });

        clearBtn.addActionListener(_ -> {
            counter.set(0);
            label.setText("");
        });
    }
}
