package gui;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.LineBorder;
import main.RunGame;

/** launcher menu that appears when the program runs */
public class Launcher extends JFrame {
    /* java classes */
    protected JPanel window = new JPanel();
    private JButton play, options, help, quit;
    private Rectangle rPlay, rOptions, rHelp, rQuit;
    
    /* window dimensions */
    private int windowWidth = 700;
    private int windowHeight = 500;
    
    /* button dimensions */
    protected int buttonWidth = 120;
    protected int buttonHeight = 40;
    
    /** constructor for the Launcher class */
    public Launcher(int id) {       
        /* window settings */ 
        Color backgroundColor = new Color(32, 3, 2);
                               
        setTitle("Ball Collector Game Launcher");
        setSize(new Dimension(windowWidth, windowHeight));
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        getContentPane().add(window);
        window.setBackground(backgroundColor);
        setLocationRelativeTo(null);
        setResizable(false);
        setVisible(true);
        window.setLayout(null);
        
        if (id == 0) {
            drawButtons();
        }     
    }
    
    /** creates buttons on the launcher window */
    private void drawButtons() {
        final Color fontColor = new Color(200, 95, 92);
        final Color buttonColor = new Color(246, 194, 170);
        
        /* play button */
        play = new JButton("Play Game!");
        rPlay = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 250, buttonWidth, buttonHeight);
        play.setBounds(rPlay);
        play.setForeground(fontColor);
        play.setBackground(buttonColor);
        play.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(play);
        
        /* options button */
        options = new JButton("Options");
        rOptions = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 200, buttonWidth, buttonHeight);
        options.setBounds(rOptions);
        options.setForeground(fontColor);
        options.setBackground(buttonColor);
        options.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(options);
        
        /* help button */
        help = new JButton("Help");
        rHelp = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 150, buttonWidth, buttonHeight);
        help.setBounds(rHelp);
        help.setForeground(fontColor);
        help.setBackground(buttonColor);
        help.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(help);
        
        /* quit button */
        quit = new JButton("Quit");
        rQuit = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 100, buttonWidth, buttonHeight);
        quit.setBounds(rQuit);
        quit.setForeground(fontColor);
        quit.setBackground(buttonColor);
        quit.setBorder(new LineBorder(Color.WHITE, 3));
        window.add(quit);
        
        /* action listeners for buttons */
        /* play button */
        play.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                dispose(); /* close the GUI when the game window loads */
                new RunGame();
            }            
        });
        
        /* options button */
        options.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                dispose();
                new Options(fontColor, buttonColor);
            }            
        });
        
        /* help button */
        help.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                
            }
            
        });
        
        /* quit button */
        quit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0); /* exited on request */
            }
        });
    }
}