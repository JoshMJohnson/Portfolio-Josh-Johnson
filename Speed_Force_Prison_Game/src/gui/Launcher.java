package gui;

import input.InputHandler;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.image.BufferStrategy;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;
import main.RunGame;

/** launcher menu that appears when the program runs */
public class Launcher extends Canvas implements Runnable {
    /* java classes */
    protected JPanel window = new JPanel();
    
    /* window dimensions */
    private int windowWidth = 700;
    private int windowHeight = 500;
        
    /* running variables */
    private Thread thread;
    public JFrame frame = new JFrame();
    public boolean running = false;
    
    /** constructor for the Launcher class */
    public Launcher() {       
        /* window settings */                                
        frame.setUndecorated(true);
        frame.setTitle("Ball Collector Game Launcher");
        frame.setSize(new Dimension(windowWidth, windowHeight));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.setLocationRelativeTo(null);
        frame.setResizable(false);
        frame.setVisible(true);
        window.setLayout(null);
                
        /* user input */
        InputHandler input = new InputHandler();
        addKeyListener(input);
        addFocusListener(input);
        addMouseListener(input);
        addMouseMotionListener(input);
        
        startMenu();
        frame.repaint();
    }
    
    /** render the menu */
    private void renderMenu() throws IllegalStateException {
        BufferStrategy bs = this.getBufferStrategy();
        
        if (bs == null) {
            createBufferStrategy(3);
            return;
        }
                          
        Graphics g = bs.getDrawGraphics();       
        g.fillRect(0,  0, 700, 500);
        
        try {
            g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_background.png")), 0, 0, 700, 500, null);
            
            /* moving selected icon */
            if (InputHandler.mouseX > 20 && InputHandler.mouseX < 95
                    && InputHandler.mouseY > ((windowHeight / 2) - 150) && InputHandler.mouseY < ((windowHeight / 2) - 110)) { /* if play button hovered */
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 95, (windowHeight / 2) - 150, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the play button */                    
                    frame.dispose();
                    new RunGame();
                }
            } else if(InputHandler.mouseX > 20 && InputHandler.mouseX < 170
                    && InputHandler.mouseY > ((windowHeight / 2) - 70) && InputHandler.mouseY < ((windowHeight / 2) - 30)) { /* else if; options button hovered */
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 170, (windowHeight / 2) - 70, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the options button */                    
                    new Options();
                }
            } else if (InputHandler.mouseX > 20 && InputHandler.mouseX < 110
                    && InputHandler.mouseY > ((windowHeight / 2) + 10) && InputHandler.mouseY < ((windowHeight / 2) + 50)) { /* else if; help button hovered*/
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 110, (windowHeight / 2) + 10, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the help button */
                    System.out.println("Help Clicked!");
                }
            } else if (InputHandler.mouseX > 20 && InputHandler.mouseX < 110
                    && InputHandler.mouseY > ((windowHeight / 2) + 90) && InputHandler.mouseY < ((windowHeight / 2) + 130)) { /* else if quit button hovered */
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 110, (windowHeight / 2) + 90, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the exit button */
                    System.exit(0);
                }
            }
        } catch(IOException e) {
            e.printStackTrace();
        }
        
        /* creating buttons */
        Color buttonColor = new Color(139, 0, 0);
        g.setColor(buttonColor);
        g.setFont(new Font("Comic Sans MS", 0, 40));
        g.drawString("Play", 20, (windowHeight / 2) - 120);
        g.drawString("Options", 20, (windowHeight / 2) - 40);
        g.drawString("Help", 20, (windowHeight / 2) + 40);
        g.drawString("Quit", 20, (windowHeight / 2) + 120);
        g.dispose();
        
        bs.show();
    }
    
    /** continuously updates contents on the frame */
    public void updateFrame() {
        if (InputHandler.dragged) {
            Point curLocation = frame.getLocation();
            frame.setLocation(curLocation.x + InputHandler.mouseDragX - InputHandler.mousePressedX, 
                        curLocation.y + InputHandler.mouseDragY - InputHandler.mousePressedY);             
        }        
    }

    /** run method implemented from the implemented java class Runnable */
    @Override
    public void run() {
        requestFocus();
        while (running) {
            try {
                renderMenu();
            } catch (IllegalStateException e) {
                e.printStackTrace();
            }
            
            updateFrame();
        }
    }
    
    /** creates start-up menu */
    public void startMenu() {
        running = true;
        thread = new Thread(this, "menu");
        thread.start();
    }
    
    /** terminates the start-up menu */
    public void stopMenu() {
        try {
            thread.join();
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}