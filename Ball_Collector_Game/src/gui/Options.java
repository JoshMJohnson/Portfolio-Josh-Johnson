package gui;

import java.awt.Choice;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.border.LineBorder;

import main.Display;

/** creates a window for the options menu */
public class Options extends Launcher {
    /* window settings */
    private int windowWidth = 300;
    private int windowHeight = 400;
   
    /* buttons */
    private JButton submitButton;
    private Rectangle rSubmitButton, rResolution;
    private Choice resolution = new Choice();
    private JLabel resLabel = new JLabel();
      
    /** constructor for Options class */
    public Options(Color fontColor, Color buttonColor) {
        super(1);
        setTitle("Options");
        setSize(new Dimension(windowWidth, windowHeight));
        setLocationRelativeTo(null);
        drawButtons(fontColor, buttonColor);
    }
    
    /** creates buttons within the option menu */
    private void drawButtons(Color fontColor, Color buttonColor) {
        /* create buttons */
        submitButton = new JButton("Save");
        rSubmitButton = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 100, buttonWidth, buttonHeight - 10);
        submitButton.setBounds(rSubmitButton);
        submitButton.setForeground(fontColor);
        submitButton.setBackground(buttonColor);
        submitButton.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(submitButton);
        
        /* change resolution option */
        /* label for resolution */
        int resLabelWidth = 110;
        int resLabelHeight = 20;        
        resLabel = new JLabel("Change Resolution");
        resLabel.setBounds((windowWidth / 2) - (resLabelWidth / 2) - 3, 10, resLabelWidth, resLabelHeight);
        resLabel.setForeground(fontColor);
        window.add(resLabel);
                
        /* drop-down box for resolution */
        rResolution = new Rectangle((windowWidth / 2) - (resLabelWidth / 2) , 20 + resLabelHeight, 100, 30);
        resolution.setBounds(rResolution);
        resolution.setForeground(fontColor);
        resolution.setBackground(buttonColor);
        resolution.add("640 x 480");
        resolution.add("800 x 600");
        resolution.add("1024 x 768");
        resolution.add("1400 x 1000");
        resolution.select(0);
        window.add(resolution);
        
        /* action listeners */
        /* submit button */
        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                Display.selection = resolution.getSelectedIndex();
                dispose();
                new Launcher(0);
            }
        });
    }
}