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
import javax.swing.border.Border;
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
    private JLabel moveForwardL, moveBackwardL, moveLeftL, moveRightL, jumpL, sprintL, crouchL; /* label for controls */
    
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
        window.repaint();
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
        gameControlsTitle.setBounds((windowWidth / 4 * 3) - (gameControlsTitleWidth / 2), helpLabelHeight + 30, gameControlsTitleWidth, 50);
        gameControlsTitle.setBorder(BorderFactory.createMatteBorder(0, 0, 1, 0, Color.YELLOW));
        window.add(gameControlsTitle);
        
        /* body of how to play game */
        int controlLabelWidth = windowWidth / 2;
        int controlLabelHeight = 20;
        
        /* control label for moving forward */
        String moveForwardText = "W - Move Forward";
        moveForwardL = new JLabel(moveForwardText, SwingConstants.CENTER);
        moveForwardL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveForwardL.setForeground(fontColor);
        moveForwardL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30, controlLabelWidth, controlLabelHeight);
        window.add(moveForwardL);
        
        /* control label for moving backward */
        String moveBackwardText = "S - Move Backward";
        moveBackwardL = new JLabel(moveBackwardText, SwingConstants.CENTER);
        moveBackwardL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveBackwardL.setForeground(fontColor);
        moveBackwardL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30 + controlLabelHeight, controlLabelWidth, controlLabelHeight);
        window.add(moveBackwardL);
        
        /* control label for moving left */
        String moveLeftText = "A - Move Left";
        moveLeftL = new JLabel(moveLeftText, SwingConstants.CENTER);
        moveLeftL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveLeftL.setForeground(fontColor);
        moveLeftL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30 + controlLabelHeight * 2, controlLabelWidth, controlLabelHeight);
        window.add(moveLeftL);
        
        /* control label for moving right */
        String moveRightText = "D - Move Right";
        moveRightL = new JLabel(moveRightText, SwingConstants.CENTER);
        moveRightL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        moveRightL.setForeground(fontColor);
        moveRightL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30 + controlLabelHeight * 3, controlLabelWidth, controlLabelHeight);
        window.add(moveRightL);
        
        /* control label for jumping */
        String jumpText = "SPACE - Jump";
        jumpL = new JLabel(jumpText, SwingConstants.CENTER);
        jumpL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        jumpL.setForeground(fontColor);
        jumpL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30 + controlLabelHeight * 4, controlLabelWidth, controlLabelHeight);
        window.add(jumpL);
        
        /* control label for sprinting */
        String sprintText = "SHIFT - Sprint";
        sprintL = new JLabel(sprintText, SwingConstants.CENTER);
        sprintL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        sprintL.setForeground(fontColor);
        sprintL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30 + controlLabelHeight * 5, controlLabelWidth, controlLabelHeight);
        window.add(sprintL);
        
        /* control label for crouching */
        String crouchText = "CTRL - Crouch";
        crouchL = new JLabel(crouchText, SwingConstants.CENTER);
        crouchL.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
        crouchL.setForeground(fontColor);
        crouchL.setBounds(windowWidth / 2, helpLabelHeight + helpLabelHeight + 30 + controlLabelHeight * 6, controlLabelWidth, controlLabelHeight);
        window.add(crouchL);
        
    }
    
    /** creates the buttons on the help window */
    private void drawButtons(Color fontColor) {
        /* creating colors */
        Color buttonColor = new Color(255, 99, 71);
        
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