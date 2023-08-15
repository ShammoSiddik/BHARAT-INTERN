import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

class TemperatureConverter
{
    public static JFrame Converter;
    public static JLabel Celsius;
    public static JTextField CelsiusText;
    public static JLabel Fahrenheit;
    public static JTextField FahrenheitText;
    public static JButton Celsius2Fahrenheit;
    public static JButton Fahrenheit2Celsius;
    
    public static void main(String[] args)
    {
        Converter = new JFrame("Made By Shammo Siddik");
        Converter.setSize(375, 200);
        Converter.setLayout(new FlowLayout());
        Celsius = new JLabel("Celsius:");
        CelsiusText = new JTextField(10);
        Fahrenheit = new JLabel("Fahrenheit:");
        FahrenheitText = new JTextField(10);
        Celsius2Fahrenheit = new JButton("Convert");
        Celsius2Fahrenheit.addActionListener
        (
            new ActionListener()
            {
                public void actionPerformed(ActionEvent e)
                {
                    String cText = CelsiusText.getText();
                    double c = Double.parseDouble(cText);
                    double f = (c * 9 / 5) + 32;
                    FahrenheitText.setText(String.valueOf(f));
                }
            }
        );
        
        Fahrenheit2Celsius = new JButton("Convert");
        Fahrenheit2Celsius.addActionListener
        (
            new ActionListener()
            {
                public void actionPerformed(ActionEvent e)
                {
                    String fText = FahrenheitText.getText();
                    double f = Double.parseDouble(fText);
                    double c = (f - 32) * 5 / 9;
                    CelsiusText.setText(String.valueOf(c)); 
                }
            }
        );
        Converter.add(Celsius);
        Converter.add(CelsiusText);
        Converter.add(Fahrenheit);
        Converter.add(FahrenheitText);
        Converter.add(Celsius2Fahrenheit);
        Converter.add(Fahrenheit2Celsius);
        Converter.setVisible(true);
    }
}