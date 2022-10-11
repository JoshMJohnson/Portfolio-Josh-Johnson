package gui;

import java.awt.Choice;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.LineBorder;
import main.Display;

/** creates a window for the options menu */
public class Options extends JFrame {
    /* window settings */
    private JPanel window = new JPanel();
    private int windowWidth = 300;
    private int windowHeight = 400;
   
    /* buttons */
    private JButton submitButton;
    private Rectangle rSubmitButton, rResolution;
    private Choice resolution = new Choice();
    private JTextField textWidth, textHeight;  
    private JLabel resLabel, customWidth, customHeight, customLabel;
    private int buttonWidth = 120;
    private int buttonHeight = 40;
    
    /** constructor for Options class */
    public Options() {
        Color backgroundColor = new Color(139, 0 , 0);
                
        setTitle("Options");
        setSize(new Dimension(windowWidth, windowHeight));
        add(window);
        setLocationRelativeTo(null);
        setResizable(false);
        setVisible(true);
        window.setLayout(null);  
        window.setBackground(backgroundColor);
        drawButtons();
        window.repaint();
    }
    
    /** creates buttons within the option menu */
    private void drawButtons() {
        /* creating colors */
        Color fontColor = new Color(255, 255, 0);
        Color buttonColor = new Color(255, 99, 71);
        
        /* create buttons */
        submitButton = new JButton("Save");
        rSubmitButton = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 75, buttonWidth, buttonHeight - 10);
        submitButton.setBounds(rSubmitButton);
        submitButton.setForeground(fontColor);
        submitButton.setBackground(buttonColor);
        submitButton.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(submitButton);
        
        /* change resolution option */
        /* label for resolution */
        int resTitleWidth = 110;
        int resWidth = 100;
        int resHeight = 20;        
        resLabel = new JLabel("Change Resolution");
        resLabel.setBounds((windowWidth / 2) - (resTitleWidth / 2) + 3, 10, resTitleWidth, resHeight);
        resLabel.setForeground(fontColor);
        window.add(resLabel);
                
        /* drop-down box for resolution */
        rResolution = new Rectangle((windowWidth / 2) - (resWidth / 2) , 20 + resHeight, resWidth, resHeight);
        resolution.setBounds(rResolution);
        resolution.setForeground(fontColor);
        resolution.setBackground(buttonColor);
        resolution.add("640 x 480");
        resolution.add("800 x 600");
        resolution.add("1024 x 768");
        resolution.add("1400 x 1000");
        resolution.select(0);
        window.add(resolution);
               
        /* labels for custom resolution */
        customLabel = new JLabel("Custom Resolution");
        customLabel.setBounds((windowWidth / 2) - (resTitleWidth / 2) + 3, 70, resTitleWidth, resHeight);
        customLabel.setForeground(fontColor);
        window.add(customLabel);
        
        customWidth = new JLabel("Width:");
        customWidth.setBounds((windowWidth / 2) - (resWidth / 2), 80 + resHeight, resWidth, resHeight);
        customWidth.setForeground(fontColor);
        window.add(customWidth);
        
        customHeight = new JLabel("Height:");
        customHeight.setBounds((windowWidth / 2) - (resWidth / 2), 110 + resHeight, resWidth, resHeight);
        customHeight.setForeground(fontColor);
        window.add(customHeight);
        
        /* text fields for custom resolution */
        textWidth = new JTextField();
        textWidth.setBounds((windowWidth / 2), 80 + resHeight, resWidth / 2, resHeight);
        textWidth.setBackground(buttonColor);
        textWidth.setForeground(fontColor);
        window.add(textWidth);
        
        textHeight = new JTextField();
        textHeight.setBounds((windowWidth / 2), 110 + resHeight, resWidth / 2, resHeight);
        textHeight.setBackground(buttonColor);
        textHeight.setForeground(fontColor);
        window.add(textHeight);
        
        /* action listeners */
        /* submit button */
        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {  
                try { /* if custom resolution is desired; both fields filled out correctly */
                    int custWidth = Integer.parseInt(textWidth.getText());
                    int custHeight = Integer.parseInt(textHeight.getText());
                    Display.width = custWidth;
                    Display.height = custHeight;
                    Display.selection = -1; 
                } catch (NumberFormatException ex) { /* else; drop-down box selected resolution */
                    Display.selection = resolution.getSelectedIndex();
                }

                dispose();
            }
        });
    }
}