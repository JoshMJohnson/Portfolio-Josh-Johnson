package main;

import graphics.Screen;
import javax.swing.JFrame;
import java.awt.Canvas;
import java.awt.Dimension;
import java.awt.Graphics;
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
    /* window settings */
	public final static int WIDTH = 1700;
	public final static int HEIGHT  = 850;
	public final static String TITLE = "Balls Collector Game";
	
	/* game settings */
	private Thread thread;
	private BufferedImage img;
	private boolean running = false;
    private int[] pixels;

	/* other java classes */
	private Screen screen;
	private Game game;
		
	/** constructor for Display class */
	public Display() {
	    /* window size */
	    Dimension size = new Dimension(WIDTH, HEIGHT);
	    setPreferredSize(size);
	    setMinimumSize(size);
	    setMaximumSize(size);
	    
	    screen = new Screen(WIDTH, HEIGHT);
	    game = new Game();
	    img = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
	    pixels = ((DataBufferInt) img.getRaster().getDataBuffer()).getData();
	}
	
	/** main method */
	public static void main (String args[]) {
	    JFrame frame = new JFrame();
		Display game = new Display();
		
		/* setup game window */
		frame.add(game);
		frame.pack(); /* sizes frame to ensure all contents are at or above their preferred sizes */
		frame.setTitle(TITLE);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    frame.setLocationRelativeTo(null); //center window on screen
		frame.setResizable(false);
		frame.setVisible(true);
		
		/* begin the game */
		game.start();
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
	
	 /** thread use; start-up method when the game is set to run */
	 public void run() {
	     int frames = 0;
	     double unprocessedSeconds = 0;
	     long prevTime = System.nanoTime();
	     double secondsPerTick = 1 / 60.0;
	     int tickCount = 0;
	     boolean ticked = false;
	     
	     /* frames per second counter */
	     while (running) {
	         long currentTime = System.nanoTime();
	         long passedTime = currentTime - prevTime;
	         prevTime = currentTime;
	         unprocessedSeconds += passedTime / 1000000000.0;
	         
	         while (unprocessedSeconds > secondsPerTick) {
	             tick();
	             unprocessedSeconds -= secondsPerTick;
	             ticked = true;
	             tickCount++;
	             
	             if (tickCount %60 == 0) {
	                 System.out.println(frames + "fps");
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
         }
     }
	 
    /** game progression */
	 private void tick() {
	     game.tick();
	 }
	 
	 /** render the screen */
	 private void render() {
	     BufferStrategy bs = this.getBufferStrategy();
	     
	     if (bs == null) {
	         createBufferStrategy(3);
	         return;
	     }
	     
	     screen.render(game);
	     
	     for (int i = 0; i < WIDTH * HEIGHT; i++) {
	         pixels[i] = screen.pixels[i];
	     }
	     
	     Graphics g = bs.getDrawGraphics();
	     g.drawImage(img, 0, 0, WIDTH, HEIGHT, null);
	     g.dispose();
	     bs.show();
	 }
}