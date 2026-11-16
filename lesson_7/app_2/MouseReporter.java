package com.semasem.lesson_7.app_2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseAdapter;

public class MouseReporter extends JPanel {
    private JLabel label;

    public MouseReporter() {
        setLayout(new BorderLayout());
        setBackground(new Color(0xf0f0f0));

        label = new JLabel("Нажмите кнопку мыши в окне", SwingConstants.CENTER);
        label.setFont(new Font("Arial", Font.PLAIN, 16));
        add(label, BorderLayout.CENTER);

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                handleMouseClick(e);
            }
        });
    }

    private void handleMouseClick(MouseEvent e) {
        if (SwingUtilities.isLeftMouseButton(e)) {
            label.setText("Левая кнопка");
        } else if (SwingUtilities.isRightMouseButton(e)) {
            label.setText("Правая кнопка");
        } else {
            label.setText("Другая кнопка");
        }
    }
}