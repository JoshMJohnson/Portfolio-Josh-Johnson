package main;

import graphics.Screen;
import input.Controller;
import input.InputHandler;

import javax.swing.JFrame;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;

/** Created By: Josh Johnson
  * Description: 3-Dimensional game
  *  - TODO: have a start-up menu with game rules/controls shown
  *  - TODO: control character in center of screen
  *  - TODO: run around and collect bouncing balls before time runs out
  *  - TODO: collect all bouncing balls = winner!; else loser
  *  - TODO: have a end-game menu (start-up menu to play again/quit)
  *     - collect all bouncing balls = winner!; else loser */
public class Display extends Canvas implements Runnable {
    /* class objects */
    private Screen screen;
    private Game game;
    private InputHandler input;
    
    /* window settings */
	public final static int width = 1700;
	public final static int height  = 850;
	public final static String title = "Balls Collector Game";
	
	/* game settings */
	private Thread thread;
	private BufferedImage img;
	private boolean running = false;
    private int[] pixels;
    private int fps;
    
    /* user settings */
    private int newX = 0;
    private int oldX = 0;
		
	/** constructor for Display class */
	public Display() {
	    /* window size */
	    Dimension size = new Dimension(width, height);
	    setPreferredSize(size);
	    setMinimumSize(size);
	    setMaximumSize(size);
	    
	    screen = new Screen(width, height);
	    game = new Game();
	    img = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
	    pixels = ((DataBufferInt) img.getRaster().getDataBuffer()).getData();
	    
	    /* enable user input */
	    input = new InputHandler();
	    addKeyListener(input);
	    addFocusListener(input);
	    addMouseListener(input);
	    addMouseMotionListener(input);   
	}
	
	/** starts the game */
	private void start() {
	    /* if already running  */
	    if (running) {
	        return;
	    }
	    
	    running = true;
	    thread = new Thread(this);
	    thread.start();
	}
	
	/** stops the game */
	private void stop() {
	    /* if already not running */
	    if (!running) {
	        return;
	    }
	    
	    running = false;
	    
	    try {
            thread.join();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(0);
        }
	}
	
	 /** thread use; start-up method when the game is set to start */
	 public void run() {
	     int frames = 0;
	     double unprocessedSeconds = 0;
	     long prevTime = System.nanoTime();
	     double secondsPerTick = 1 / 60.0;
	     int tickCount = 0;
	     boolean ticked = false;
	     
	     while (running) {
	         long currentTime = System.nanoTime();
	         long passedTime = currentTime - prevTime;
	         prevTime = currentTime;
	         unprocessedSeconds += passedTime / 1000000000.0;
	         requestFocus(); /* automatically selects window when game is started */
	         
	         /* frames per second counter */
	         while (unprocessedSeconds > secondsPerTick) {
	             tick();
	             unprocessedSeconds -= secondsPerTick;
	             ticked = true;
	             tickCount++;
	             
	             if (tickCount %60 == 0) {
	                 fps = frames;
	                 prevTime += 1000;
	                 frames = 0;
	             }
	         }
	         
	         if (ticked) {
	             render();
	             frames++;
	         }
	         
	         render();
	         frames++;
	         
	         /* mouse actions */
	         newX = InputHandler.mouseX;
	         
	         if (newX > oldX) { /* if moving right */
	             Controller.turnRight = true;
	         } else if (newX < oldX) { /* if moving left */
	             Controller.turnLeft = true;
	         } else if (newX == oldX) { /* if still */
	             Controller.turnRight = false;
	             Controller.turnLeft = false;
	         }	         
	         oldX = newX;
         }
     }
	 
    /** game progression */
	 private void tick() {
	     game.tick(input.key);
	 }
	 
	 /** render the screen */
	 private void render() {
	     BufferStrategy bs = this.getBufferStrategy();
	     
	     if (bs == null) {
	         createBufferStrategy(3);
	         return;
	     }
	     
	     screen.render(game);
	     
	     for (int i = 0; i < width * height; i++) {
	         pixels[i] = screen.pixels[i];
	     }
	     
	     Graphics g = bs.getDrawGraphics();
	     g.drawImage(img, 0, 0, width, height, null);
	     g.setFont(new Font("Verdana", 0, 50));
	     g.setColor(Color.yellow);
	     g.drawString(fps + " FPS", 20, 50);
	     g.dispose();
	     bs.show();
    }

    /** main method */
    public static void main(String args[]) {
        BufferedImage cursor = new BufferedImage(16, 16, BufferedImage.TYPE_INT_ARGB);
        Cursor blank = Toolkit.getDefaultToolkit().createCustomCursor(cursor, new Point(0,0), "blank");
        JFrame frame = new JFrame();
        Display game = new Display();

        /* setup game window */
        frame.add(game);
        frame.pack(); /* sizes frame to ensure all contents are at or above their preferred sizes */
//        frame.getContentPane().setCursor(blank);
        frame.setTitle(title);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null); // center window on screen
        frame.setResizable(false);
        frame.setVisible(true);

        /* begin the game */
        game.start();
    }
}