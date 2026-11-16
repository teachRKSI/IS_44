package com.semasem.lesson_7.app_3;

import javax.swing.*;
import java.awt.*;

public class StyledButtons extends JPanel {

    public StyledButtons() {
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JButton btnOne = new JButton("Одна");
        JButton btnTwo = new JButton("Две");
        JButton btnThree = new JButton("Три");

        Color commonBg = new Color(0x3498db);
        Color commonFg = Color.WHITE;
        Font buttonFont = new Font("Arial", Font.BOLD, 14);

        applyCommonStyle(btnOne, commonBg, commonFg, buttonFont);
        applyCommonStyle(btnTwo, commonBg, commonFg, buttonFont);

        applyCommonStyle(btnThree, new Color(0xffcccc), new Color(0x333333), buttonFont);

        add(btnOne);
        add(Box.createVerticalStrut(10));
        add(btnTwo);
        add(Box.createVerticalStrut(10));
        add(btnThree);
    }

    private void applyCommonStyle(JButton button, Color bg, Color fg, Font font) {
        button.setBackground(bg);
        button.setForeground(fg);
        button.setFont(font);
        button.setFocusPainted(false);
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        button.setMaximumSize(new Dimension(150, 40));
    }
}