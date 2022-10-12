package gui;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.border.LineBorder;

/** handles the help window accessed from the launcher */
public class Help extends JFrame {
    /* window settings */
    private JPanel window = new JPanel();
    private int windowWidth = 600;
    private int windowHeight = 400;
    
    /* buttons */
    private JButton submitButton;
    private Rectangle rSubmitButton;
    private int buttonWidth = 120;
    private int buttonHeight = 40;
    private JLabel helpLabel;
    
    /** constructor for the Help java class */
    public Help(Color backgroundColor) {    
        /* window settings */
        setTitle("Help");
        setSize(new Dimension(windowWidth, windowHeight));
        add(window);
        setLocationRelativeTo(null);
        setResizable(false);
        setVisible(true);
        window.setLayout(null);  
        window.setBackground(backgroundColor);
        window.repaint();
        
        /* creating colors */
        Color fontColor = new Color(255, 255, 0);
                
        /* fill in window with content */
        createText(fontColor);
        drawButtons(fontColor);
    }
    
    /** creates the labels and text on the help window */
    private void createText(Color fontColor) {
        /* label for Help */        
        int helpLabelWidth = windowWidth - 60;
        int helpLabelHeight = 60;
        helpLabel = new JLabel("Help", SwingConstants.CENTER);
        helpLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 26));
        helpLabel.setBounds((windowWidth / 2) - (helpLabelWidth / 2) - 6, 10, helpLabelWidth, helpLabelHeight);
        helpLabel.setForeground(fontColor);
        helpLabel.setBorder(BorderFactory.createLineBorder(Color.YELLOW, 5));
        window.add(helpLabel);
        
        /* how to play game content */
        
        
        /* control content */        
    }
    
    /** creates the buttons on the help window */
    private void drawButtons(Color fontColor) {
        /* creating colors */
        Color buttonColor = new Color(255, 99, 71);
        
        /* create buttons */
        /* submit button */
        submitButton = new JButton("Save");
        rSubmitButton = new Rectangle((windowWidth / 2) - (buttonWidth / 2) - 3, windowHeight - 100, buttonWidth, buttonHeight - 10);
        submitButton.setBounds(rSubmitButton);
        submitButton.setForeground(fontColor);
        submitButton.setBackground(buttonColor);
        submitButton.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(submitButton);
        
        /* action listeners */
        /* submit button */
        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {  
                Launcher.helpMenuOpened = false;
                dispose();
            }
        });
    }
}