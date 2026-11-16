package com.semasem.lesson_7.app_4;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.*;

public class ColorTableWindow extends JFrame {

    public ColorTableWindow() {
        super("QTableWidget: цвета");
        setSize(600, 320);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Данные для таблицы (имя, hex-код, пустое значение для цвета, комментарий)
        Object[][] colors = {
                {"Red", "#FF0000", "", "Основной красный"},
                {"Green", "#00FF00", "", "Чистый зеленый"},
                {"Blue", "#0000FF", "", "Чистый синий"},
                {"Black", "#000000", "", "Классический черный"},
                {"White", "#FFFFFF", "", "Белый цвет фона"},
                {"Electric Green", "#41CD52", "", "Яркий салатовый"},
                {"Dark Blue", "#222840", "", "Темно-синий оттенок"},
                {"Yellow", "#F9E56D", "", "Теплый желтый"}
        };

        String[] columnNames = {"Name", "Hex Code", "Color", "Комментарий"};

        JTable table = new JTable(colors, columnNames);
        table.setRowHeight(25);

        // Кастомизация цвета ячейки в колонке "Color" (индекс 2) через Renderer
        table.getColumnModel().getColumn(2).setCellRenderer(new DefaultTableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                                                           boolean isSelected, boolean hasFocus,
                                                           int row, int column) {
                Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                // Получаем Hex-код из соседней колонки (индекс 1)
                String hex = (String) table.getValueAt(row, 1);
                c.setBackground(Color.decode(hex));
                // Делаем текст невидимым или пустым для этой ячейки, чтобы виден был только цвет
                setText("");
                return c;
            }
        });

        // Добавляем таблицу в скролл-панель (чтобы отображались заголовки)
        add(new JScrollPane(table));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new ColorTableWindow().setVisible(true);
        });
    }
}