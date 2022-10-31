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
    private JLabel helpLabel, gameAbout, gameAboutTitle, gameControlsTitle;
    private JLabel moveForwardLabel, moveBackwardLabel, moveLeftLabel, moveRightLabel;
    private JLabel jumpLabel, sprintLabel, crouchLabel, lookLeftLabel, lookRightLabel;
    
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
        
        /* fill in window with content */
        Color fontColor = new Color(255, 255, 0);
        createText(fontColor);
        drawButtons(fontColor);
        window.repaint();
        
        /* allows the help window to reopen when closed using the default close operation */
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent windowEvent) {
                Launcher.helpMenuOpened = false;              
            }
        });
    }
    
    /** creates the labels and text on the help window */
    private void createText(Color fontColor) {
        /* label for Help */        
        int helpLabelWidth = windowWidth - 80;
        int helpLabelHeight = 60;
        helpLabel = new JLabel("Help", SwingConstants.CENTER);
        helpLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 26));
        helpLabel.setBounds((windowWidth / 2) - (helpLabelWidth / 2) - 6, 10, helpLabelWidth, helpLabelHeight);
        helpLabel.setForeground(fontColor);
        helpLabel.setBorder(BorderFactory.createLineBorder(Color.YELLOW, 5));
        window.add(helpLabel);
        
        /* game description content */        
        /* title of game description */
        int aboutTitleWidth = 120;
        gameAboutTitle = new JLabel("About Game");
        gameAboutTitle.setFont(new Font("Comic Sans MS", Font.BOLD, 20));
        gameAboutTitle.setForeground(fontColor);
        gameAboutTitle.setBounds((windowWidth / 4) - (aboutTitleWidth / 2), helpLabelHeight + 30, aboutTitleWidth, 50);
        gameAboutTitle.setBorder(BorderFactory.createMatteBorder(0, 0, 1, 0, Color.YELLOW));
        window.add(gameAboutTitle);
                        
        /* body of game description */
        int aboutBodyWidth = 150;
        String aboutGame = "Catch the blur in time to regain your speed and escape the Speed Force Prison!";
        gameAbout = new JLabel();
        gameAbout.setText("<html><p style='text-align: center;'>" + aboutGame + "</p></html>");
        gameAbout.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        gameAbout.setForeground(fontColor);
        gameAbout.setBounds((windowWidth / 4) - (aboutBodyWidth / 2), 100, aboutBodyWidth, 200);
        window.add(gameAbout);
        
        /* how to play game content */   
        /* title label for how to play game */
        int gameControlsTitleWidth = 80;
        gameControlsTitle = new JLabel("Controls");
        gameControlsTitle.setFont(new Font("Comic Sans MS", Font.BOLD, 20));
        gameControlsTitle.setForeground(fontColor);
        gameControlsTitle.setBounds((windowWidth / 4 * 3) - (gameControlsTitleWidth / 2), helpLabelHeight + 10, gameControlsTitleWidth, 50);
        gameControlsTitle.setBorder(BorderFactory.createMatteBorder(0, 0, 1, 0, Color.YELLOW));
        window.add(gameControlsTitle);
        
        /* body of how to play game */
        int controlLabelWidth = windowWidth / 2;
        int controlLabelHeight = 20;
        
        /* control label for moving forward */
        String moveForwardText = "Move Forward - W";
        moveForwardLabel = new JLabel(moveForwardText, SwingConstants.CENTER);
        moveForwardLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveForwardLabel.setForeground(fontColor);
        moveForwardLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10, controlLabelWidth, controlLabelHeight);
        window.add(moveForwardLabel);
        
        /* control label for moving backward */
        String moveBackwardText = "Move Backward - S";
        moveBackwardLabel = new JLabel(moveBackwardText, SwingConstants.CENTER);
        moveBackwardLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveBackwardLabel.setForeground(fontColor);
        moveBackwardLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight, controlLabelWidth, controlLabelHeight);
        window.add(moveBackwardLabel);
        
        /* control label for moving left */
        String moveLeftText = "Move Left - A";
        moveLeftLabel = new JLabel(moveLeftText, SwingConstants.CENTER);
        moveLeftLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveLeftLabel.setForeground(fontColor);
        moveLeftLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 2, controlLabelWidth, controlLabelHeight);
        window.add(moveLeftLabel);
        
        /* control label for moving right */
        String moveRightText = "Move Right - D";
        moveRightLabel = new JLabel(moveRightText, SwingConstants.CENTER);
        moveRightLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveRightLabel.setForeground(fontColor);
        moveRightLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 3, controlLabelWidth, controlLabelHeight);
        window.add(moveRightLabel);
        
        /* control label for jumping */
        String jumpText = "Jump - SPACE";
        jumpLabel = new JLabel(jumpText, SwingConstants.CENTER);
        jumpLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        jumpLabel.setForeground(fontColor);
        jumpLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 4, controlLabelWidth, controlLabelHeight);
        window.add(jumpLabel);
        
        /* control label for sprinting */
        String sprintText = "Sprint - SHIFT";
        sprintLabel = new JLabel(sprintText, SwingConstants.CENTER);
        sprintLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        sprintLabel.setForeground(fontColor);
        sprintLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 5, controlLabelWidth, controlLabelHeight);
        window.add(sprintLabel);
        
        /* control label for crouching */
        String crouchText = "Crouch - CTRL";
        crouchLabel = new JLabel(crouchText, SwingConstants.CENTER);
        crouchLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        crouchLabel.setForeground(fontColor);
        crouchLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 6, controlLabelWidth, controlLabelHeight);
        window.add(crouchLabel);
        
        /* control label for looking left */
        String lookLeftText = "Look Left - Move Mouse Left";
        lookLeftLabel = new JLabel(lookLeftText, SwingConstants.CENTER);
        lookLeftLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        lookLeftLabel.setForeground(fontColor);
        lookLeftLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 7, controlLabelWidth, controlLabelHeight);
        window.add(lookLeftLabel);
        
        /* control label for looking right */
        String lookRightText = "Look Right - Move Mouse Right";
        lookRightLabel = new JLabel(lookRightText, SwingConstants.CENTER);
        lookRightLabel.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        lookRightLabel.setForeground(fontColor);
        lookRightLabel.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 10 + controlLabelHeight * 8, controlLabelWidth, controlLabelHeight);
        window.add(lookRightLabel);        
    }
    
    /** creates the buttons on the help window */
    private void drawButtons(Color fontColor) {
        /* creating colors */
        Color buttonColor = new Color(255, 99, 71);
        
        /* submit button */
        submitButton = new JButton("Save");
        rSubmitButton = new Rectangle((windowWidth / 2) - (buttonWidth / 2) - 3, windowHeight - 85, buttonWidth, buttonHeight - 10);
        submitButton.setBounds(rSubmitButton);
        submitButton.setForeground(fontColor);
        submitButton.setBackground(buttonColor);
        submitButton.setBorder(new LineBorder(Color.YELLOW, 3));
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