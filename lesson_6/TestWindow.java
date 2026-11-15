package com.semasem.lesson_6;

import javax.swing.*;
import java.awt.*;

public class TestWindow extends JFrame {
    private JLabel label;
    private JTextField nameField;
    private JButton helloBtn;
    private JButton clearBtn;
    private int count = 0;

    public TestWindow() {
        super("Hello counter");

        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        label = new JLabel("");
        nameField = new JTextField("");
        helloBtn = new JButton("Hello");
        helloBtn.addActionListener(_ -> helloBtnAction());
        clearBtn = new JButton("Clear");
        clearBtn.addActionListener(_ -> clearBtnAction());

        JPanel infoPain = new JPanel();
        infoPain.setLayout(new BoxLayout(infoPain, BoxLayout.Y_AXIS));
        infoPain.add(label);
        infoPain.add(nameField);

        JPanel buttonPane = new JPanel();
        buttonPane.setLayout(new GridLayout(0, 2, 5, 5));
        buttonPane.add(helloBtn);
        buttonPane.add(clearBtn);

        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));
        add(infoPain);
        add(buttonPane);
    }

    public void helloBtnAction() {
        String name = nameField.getText().trim();
        if (name.isBlank()) {
            label.setText("Сначала введите имя");
        } else {
            count++;
            label.setText(String.format("Привет, %s! Это ваше %d приветствие", name, count));
        }
    }

    public void clearBtnAction() {
        count = 0;
        label.setText("");
        nameField.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new TestWindow().setVisible(true);
        });
    }
}
