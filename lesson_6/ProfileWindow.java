package com.semasem.lesson_6;

import javax.swing.*;
import java.awt.*;

public class ProfileWindow extends JFrame {
    private JTextField nameField;
    private JTextField ageField;
    private JTextField cityField;
    private JButton button;
    private JLabel label;

    public ProfileWindow() {
        super("Анкета");

        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        nameField = new JTextField();
        ageField = new JTextField();
        cityField = new JTextField();
        button = new JButton("Показать");
        button.addActionListener(_ -> btnAction());
        label = new JLabel("");
        label.setVerticalAlignment(SwingConstants.TOP);

        JPanel formPanel = new JPanel(new GridLayout(3, 2, 5, 5));
        formPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        formPanel.add(new JLabel("Имя:"));
        formPanel.add(nameField);
        formPanel.add(new JLabel("Возраст:"));
        formPanel.add(ageField);
        formPanel.add(new JLabel("Город:"));
        formPanel.add(cityField);

        setLayout(new BorderLayout());
        add(formPanel, BorderLayout.CENTER);

        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BoxLayout(bottomPanel, BoxLayout.Y_AXIS));
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        label.setAlignmentX(Component.CENTER_ALIGNMENT);

        bottomPanel.add(button);
        bottomPanel.add(Box.createVerticalStrut(10));
        bottomPanel.add(label);
        bottomPanel.setBorder(BorderFactory.createEmptyBorder(0, 10, 10, 10));

        add(bottomPanel, BorderLayout.SOUTH);
    }

    private void btnAction() {
        String stringName = nameField.getText().trim();
        String stringAge = ageField.getText().trim();
        String stringCity = cityField.getText().trim();
        boolean isName = stringName.isBlank();
        boolean isAge = stringAge.isBlank();
        boolean isCity = stringCity.isBlank();

        if (isName || isAge || isCity) {
            label.setText("Заполните все поля");
        } else {
            String text = String.format("<html>Имя: %s<br>Возраст: %s<br>Город: %s</html>", stringName, stringAge, stringCity);
            label.setText(text);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ProfileWindow().setVisible(true));
    }
}
