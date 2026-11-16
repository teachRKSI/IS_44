package com.semasem.lesson_7.app_2;

import javax.swing.*;

public class MainWindow extends JFrame {
    public MainWindow() {
        super("Детектор мыши");
        setSize(400, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        MouseReporter reporter = new MouseReporter();
        add(reporter);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new MainWindow().setVisible(true);
        });
    }
}