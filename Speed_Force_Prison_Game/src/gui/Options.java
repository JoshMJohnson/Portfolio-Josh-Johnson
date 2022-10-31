package gui;

import java.awt.Choice;
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
import javax.swing.JTextField;
import javax.swing.SwingConstants;
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
    private Rectangle rSubmitButton, rResolution, rDifficulty;
    private Choice resolution = new Choice();
    private Choice difficulty = new Choice();
    private JTextField textWidth, textHeight;  
    private JLabel resLabel, customWidth, customHeight, customLabel, optionsLabel, difficultyLabel;
    private int buttonWidth = 120;
    private int buttonHeight = 30;
        
    /** constructor for Options class */
    public Options(Color backgroundColor) {  
        /* window settings */
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
        
        /* allows the options window to reopen when closed using the default close operation */
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent windowEvent) {
                Launcher.optionsMenuOpened = false;                
            }
        });
    }
    
    /** creates buttons within the option menu */
    private void drawButtons() {  
        /* creating colors */
        Color buttonColor = new Color(255, 99, 71);
        Color fontColor = new Color(255, 255, 0);
        
        /* label for options */
        int optionsLabelWidth = windowWidth - 80;
        int optionsLabelHeight = 60;
        optionsLabel = new JLabel("Options", SwingConstants.CENTER);
        optionsLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 26));
        optionsLabel.setBounds((windowWidth / 2) - (optionsLabelWidth / 2) - 6, 10, optionsLabelWidth, optionsLabelHeight);
        optionsLabel.setForeground(fontColor);
        optionsLabel.setBorder(BorderFactory.createLineBorder(Color.YELLOW, 5));
        window.add(optionsLabel);
                
        /* change resolution option */
        /* label for resolution */
        int resTitleWidth = 123;
        int resWidth = 100;
        int resHeight = 20;        
        resLabel = new JLabel("Change Resolution");
        resLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        resLabel.setBounds((windowWidth / 2) - (resTitleWidth / 2) - 3, 85, resTitleWidth, resHeight);
        resLabel.setForeground(fontColor);
        window.add(resLabel);
                
        /* drop-down box for resolution */
        rResolution = new Rectangle((windowWidth / 2) - (resWidth / 2) - 3, 95 + resHeight, resWidth, resHeight);
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
        customLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        customLabel.setBounds((windowWidth / 2) - (resTitleWidth / 2) - 3, 125 + resHeight, resTitleWidth, resHeight);
        customLabel.setForeground(fontColor);
        window.add(customLabel);
        
        customWidth = new JLabel("Width:");
        customWidth.setFont(new Font("Comic Sans MS", Font.BOLD, 11));
        customWidth.setBounds((windowWidth / 2) - (resWidth / 2) - 3, 155 + resHeight, resWidth, resHeight);
        customWidth.setForeground(fontColor);
        window.add(customWidth);
        
        customHeight = new JLabel("Height:");
        customHeight.setFont(new Font("Comic Sans MS", Font.BOLD, 11));
        customHeight.setBounds((windowWidth / 2) - (resWidth / 2) - 3, 185 + resHeight, resWidth, resHeight);
        customHeight.setForeground(fontColor);
        window.add(customHeight);
        
        /* text fields for custom resolution */
        textWidth = new JTextField();
        textWidth.setBounds((windowWidth / 2) - 3, 155 + resHeight, resWidth / 2, resHeight);
        textWidth.setBackground(buttonColor);
        textWidth.setForeground(fontColor);
        window.add(textWidth);
        
        textHeight = new JTextField();
        textHeight.setBounds((windowWidth / 2) - 3, 185 + resHeight, resWidth / 2, resHeight);
        textHeight.setBackground(buttonColor);
        textHeight.setForeground(fontColor);
        window.add(textHeight);
        
        /* difficulty option */
        /* label for difficulty */
        difficultyLabel = new JLabel("Change Difficulty");
        difficultyLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        difficultyLabel.setBounds((windowWidth / 2) - (resTitleWidth / 2) - 3, 215 + resHeight, resTitleWidth, resHeight);
        difficultyLabel.setForeground(fontColor);
        window.add(difficultyLabel);
        
        /* drop-down box for difficulty */
        rDifficulty = new Rectangle((windowWidth / 2) - (resWidth / 2) - 3, 245 + resHeight, resWidth, resHeight);
        difficulty.setBounds(rDifficulty);
        difficulty.setForeground(fontColor);
        difficulty.setBackground(buttonColor);
        difficulty.add("Sandbox");
        difficulty.add("Childs Play");
        difficulty.add("Barry Allen");
        difficulty.add("The Flash!");
        difficulty.select(1);
        window.add(difficulty);
        
        /* create buttons */
        submitButton = new JButton("Save");
        rSubmitButton = new Rectangle((windowWidth / 2) - (buttonWidth / 2) - 3, windowHeight - 85, buttonWidth, buttonHeight);
        submitButton.setBounds(rSubmitButton);
        submitButton.setForeground(fontColor);
        submitButton.setBackground(buttonColor);
        submitButton.setBorder(new LineBorder(Color.YELLOW, 3));
        window.add(submitButton);
        
        /* action listeners */
        /* submit button */
        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {  
                try { /* if custom resolution is desired; both fields filled out correctly */
                    int custWidth = Integer.parseInt(textWidth.getText());
                    int custHeight = Integer.parseInt(textHeight.getText());
                    Display.windowWidth = custWidth;
                    Display.windowHeight = custHeight;
                    Display.selection = -1; 
                } catch (NumberFormatException ex) { /* else; drop-down box selected resolution */
                    Display.selection = resolution.getSelectedIndex();
                }
                
                /* adjusting difficulty level */
                Display.difficulty = difficulty.getSelectedIndex();
                
                Launcher.optionsMenuOpened = false;
                dispose();
            }
        });
    }    
}