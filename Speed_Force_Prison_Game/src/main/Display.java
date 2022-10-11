package main;

import graphics.Screen;
import gui.Launcher;
import input.Controller;
import input.InputHandler;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;

/** Created By: Josh Johnson
  * Program Description: 3-Dimensional game
  * Game Description: Catch the blur in time to regain your speed and escape the Speed Force Prison!
  *  - TODO: run around and collect blur's before time runs out
  *  - TODO: collect enough blur's before time expires = winner!; else loser
  *  - TODO: have a end-game menu showing results with return to launcher button */
public class Display extends Canvas implements Runnable {
    /* class objects */
    private Screen screen;
    private Game game;
    private InputHandler input;
    private static Launcher launcher;
    
    /* window settings */
	public static int width;
	public static int height;
	public final static String TITLE = "Speed Force Prison";
	public static int selection = 0;
	
	/* game settings */
	private Thread thread;
	private BufferedImage img;
	private boolean running = false;
    private int[] pixels;
    private int fps;
    
    /* user settings */
    private int newX = width / 2;
    private int oldX = width / 2;
    public static int mouseSpeed;
		
	/** constructor for Display class */
	public Display() {
	    /* window size */
	    Dimension size = new Dimension(width, height);
	    setPreferredSize(size);
	    setMinimumSize(size);
	    setMaximumSize(size);
	    
	    screen = new Screen(getGameWidth(), getGameHeight());
	    game = new Game();
	    img = new BufferedImage(getGameWidth(), getGameHeight(), BufferedImage.TYPE_INT_RGB);
	    pixels = ((DataBufferInt) img.getRaster().getDataBuffer()).getData();
	    
	    /* enable user input */
	    input = new InputHandler();
	    addKeyListener(input);
	    addFocusListener(input);
	    addMouseListener(input);
	    addMouseMotionListener(input);   
	}
	
	/** gets the window width of the game */
	public static int getGameWidth() {
	    if (selection == 0) {
	        width = 640;
	    } else if (selection == 1) {
	        width = 800; 
	    } else if (selection == 2){
	        width = 1024;
	    }
	    else if (selection == 3) {
	        width = 1400;
	    }
	    
	    return width;
	}

	/** gets window height of the game */
	public static int getGameHeight() {
        if (selection == 0) {
            height = 480;
        } else if (selection == 1) {
            height = 600;
        } else if (selection == 2) {
            height = 768;
        } else if (selection == 3) {
            height = 1000;
        }
        
        return height;
    }
	
	/** returns the launcher; used to close the launcher when leaving window */
	public static Launcher getLauncherInstance() {
	    if (launcher == null) {
	        launcher = new Launcher();
	    }
	    
	    return launcher;
	}
	
	/** starts the game */
	public void start() {
	    /* if already running  */
	    if (running) {
	        return;
	    }
	    
	    running = true;
	    thread = new Thread(this, "game");
	    thread.start();
	}
	
	/** stops the game */
	public void stop() {
	    /* if already not running */
	    if (!running) {
	        return;
	    }
	    
	    running = false;
	    
	    try {
            thread.join();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1); /* exited on error */
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
	             
	             if (tickCount % 60 == 0) {
	                 fps = frames;
	                 prevTime += 1000;
	                 frames = 0;
	             }
	             
	             if (ticked) {
	                 render();
	                 frames++;
	             }
	         }	    
         }
     }
	 
     /** game progression update */
	 private void tick() {
	     game.tick(input.key);
	     
	     /* mouse actions */
         newX = InputHandler.mouseX;
         
         if (newX > oldX) { /* if moving right; rotate right */
             Controller.turnRight = true;
         } else if (newX < oldX) { /* if moving left; rotate left */
             Controller.turnLeft = true;
         } else if (newX == oldX) { /* if still; stop rotation */
             if (newX > 100 && newX < width - 100) { /* only stop rotating if mouse is not on edge of window */
                 Controller.turnRight = false;
                 Controller.turnLeft = false;  
             }
         }     
         
         oldX = newX;
	 }
	 
	 /** render the screen */
	 private void render() {
	     BufferStrategy bs = this.getBufferStrategy();
	     
	     if (bs == null) {
	         createBufferStrategy(3);
	         return;
	     }
	     
	     screen.render(game);
	     
	     for (int i = 0; i < getGameWidth() * getGameHeight(); i++) {
	         pixels[i] = screen.pixels[i];
	     }
	     
	     Graphics g = bs.getDrawGraphics();
	     g.drawImage(img, 0, 0, getGameWidth(), getGameHeight(), null);
	     g.setFont(new Font("Verdana", 0, 50));
	     g.setColor(Color.yellow);
	     g.drawString(fps + " FPS", 20, 50);
	     g.dispose();
	     bs.show();
    }
	 
    /** main method */
    public static void main(String args[]) {
        getLauncherInstance();
    }
}