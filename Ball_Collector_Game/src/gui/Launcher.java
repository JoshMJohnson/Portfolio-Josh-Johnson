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
import main.Display;

/** launcher menu that appears when the program runs */
public class Launcher extends Canvas implements Runnable {
    /* java classes */
    protected JPanel window = new JPanel();
    
    /* window dimensions */
    private int windowWidth = 700;
    private int windowHeight = 500;
    
    /* button dimensions */
    protected int buttonWidth = 120;
    protected int buttonHeight = 40;
    
    /* running variables */
    private Thread thread;
    public JFrame frame = new JFrame();
    public boolean running = false;
    
    /** constructor for the Launcher class */
    public Launcher(int id, Display display) {       
        /* window settings */ 
//        Color backgroundColor = new Color(32, 3, 2);
                               
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
        display.start();
        frame.repaint();
    }
    
    /** render the menu */
    private void renderMenu() {
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
                    && InputHandler.mouseY > 40 && InputHandler.mouseY < 100) { /* if play button hovered */
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 95, 60, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the exit button */
                    System.out.println("Play Clicked!");
                }
            } else if(InputHandler.mouseX > 20 && InputHandler.mouseX < 200
                    && InputHandler.mouseY > 100 && InputHandler.mouseY < 160) { /* else if; options button hovered */
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 170, 120, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the exit button */
                    System.out.println("Options Clicked!");
                }
            } else if (InputHandler.mouseX > 20 && InputHandler.mouseX < 110
                    && InputHandler.mouseY > 160 && InputHandler.mouseY < 220) { /* else if; help button hovered*/
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 110, 180, 40, 40, null);
                
                if (InputHandler.mouseButton == 1) { /* clicking on the exit button */
                    System.out.println("Help Clicked!");
                }
            } else if (InputHandler.mouseX > 20 && InputHandler.mouseX < 110
                    && InputHandler.mouseY > 200 && InputHandler.mouseY < 280) { /* else if quit button hovered */
                g.drawImage(ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png")), 110, 240, 40, 40, null);
                
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
        g.drawString("Play", 20, 90);
        g.drawString("Options", 20, 150);
        g.drawString("Help", 20, 210);
        g.drawString("Quit", 20, 270);
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
            renderMenu();
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