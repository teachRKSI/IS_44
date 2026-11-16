package com.semasem.lesson_7.app_1;

import javax.swing.*;
import java.awt.*;

public class MainWindow extends JFrame implements CounterListener {
    private CounterWidget counterWidget;
    private JLabel statusLabel = new JLabel("Статус: ожидает нажатий");

    public MainWindow() {
        super("Счётчик нажатий");
        setSize(350, 150);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        counterWidget = new CounterWidget();
        // Подписываемся на собственный сигнал/слушатель
        counterWidget.setCountListener(this);

        add(counterWidget, BorderLayout.CENTER);
        add(statusLabel, BorderLayout.SOUTH);
    }

    @Override
    public void onCountChanged(int newCount) {
        statusLabel.setText("Внешний слушатель поймал смену: " + newCount);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new MainWindow().setVisible(true);
        });
    }
}