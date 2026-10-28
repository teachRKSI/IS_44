package com.semasem.lesson_5;

import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;
import java.util.concurrent.atomic.AtomicInteger;

public class AppTwo {
    static void main(String[] args) {


        JFrame frame = new JFrame("Тестовое окошка");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setLayout(new GridLayout(5, 1));

        JLabel label = new JLabel();

        JTextField field = new JTextField();

        JCheckBox year = new JCheckBox();

        JCheckBox underline = new JCheckBox();

        JButton complete = new JButton("Сгенерировать");

        complete.addActionListener(_ -> {
            String name = field.getText().trim();

            if (name.isBlank()) {
                label.setText("Сначала введите имя");
                return;
            }

            String result = name;

            if (underline.isSelected()) {
                result += "_";
            }

            if (year.isSelected()) {
                result += LocalDate.now().getYear();
            }

            label.setText(result);
        });

        frame.add(label);
        frame.add(field);
        frame.add(year);
        frame.add(underline);
        frame.add(complete);

        frame.setVisible(true);
    }
}
