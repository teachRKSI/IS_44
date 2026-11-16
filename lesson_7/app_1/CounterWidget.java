package com.semasem.lesson_7.app_1;

import javax.swing.*;
import java.awt.*;

public class CounterWidget extends JPanel {
    private CounterListener listener;
    private int count = 0;
    private JLabel label = new JLabel("Нажатий: 0");
    private JButton button = new JButton("Нажать");

    public CounterWidget() {
        setLayout(new FlowLayout());

        button.addActionListener(_ -> {
            count++;
            label.setText("Нажатий: " + count);

            if (listener != null) {
                listener.onCountChanged(count);
            }
        });

        add(label);
        add(button);
    }

    public void setCountListener(CounterListener listener) {
        this.listener = listener;
    }
}
