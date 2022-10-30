package main;

import graphics.Screen;
import gui.Launcher;
import input.Player;
import input.InputHandler;
import javax.swing.JFrame;
import javax.swing.Timer;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;

/** Created By: Josh Johnson
  * Program Description: 3-Dimensional game
  * Game Description: Catch the blur in time to regain your speed and escape the Speed Force Prison!
  */
public class Display extends Canvas implements Runnable {
    /* class objects */
    private Screen screen;
    private Game game;
    private InputHandler input;
    private static Launcher launcher;
    private Timer timer;
    private BufferStrategy bs;
    private Graphics g;
    
    /* window settings */
	public static int windowWidth;
	public static int windowHeight;
	public final static String TITLE = "Speed Force Prison";
	public static int selection = 0;
	
	/* game settings */
	private Thread thread;
	private BufferedImage img;
	private boolean running = false;
    private int[] pixels;
    private int fps; /* frames per second */
    public static int difficulty = 1; /* sets difficulty */
    private int countdown = 100; /* timer in seconds */
    public static int blurs = 5; 
    private boolean playerWon;
    private boolean gameOver = false;    
    
    /* user settings */
    private int newX = windowWidth / 2;
    private int oldX = windowWidth / 2;
    public static int mouseSpeed;
		
	/** constructor for Display class */
	public Display() {
	    /* window size */
	    Dimension size = new Dimension(windowWidth, windowHeight);
	    setPreferredSize(size);
	    setMinimumSize(size);
	    setMaximumSize(size);
	    
	    screen = new Screen(getGameWidth(), getGameHeight());
	    game = new Game();
	    img = new BufferedImage(getGameWidth(), getGameHeight(), BufferedImage.TYPE_INT_RGB);
	    pixels = ((DataBufferInt) img.getRaster().getDataBuffer()).getData();
	    setDifficulty();
	    
	    /* enable user input */
	    input = new InputHandler();
	    addKeyListener(input);
	    addFocusListener(input);
	    addMouseListener(input);
	    addMouseMotionListener(input);   
	}
	
	/** sets the difficulty of the game */
	public void setDifficulty() {
	    if (difficulty == 0) { /* if easiest mode; infinite time */
	        countdown = Integer.MAX_VALUE;
	        blurs = Integer.MAX_VALUE;	        
	    } else if (difficulty == 1) { /* else if second easiest mode */
	        countdown = 100;
	        blurs = 5; 
	    } else if (difficulty == 2) { /* else if third easiest mode */
	        countdown /= 2;
	        blurs = (int) (Math.floor(blurs * 1.5));
	    } else if (difficulty == 3) { /* else if hardest game mode */
	        countdown /= 3;
	        blurs = (int) (Math.floor(blurs * 2));
	    }    
	}
			
	/** gets the window width of the game */
	public static int getGameWidth() {
	    if (selection == 0) {
	        windowWidth = 640;
	    } else if (selection == 1) {
	        windowWidth = 800; 
	    } else if (selection == 2){
	        windowWidth = 1024;
	    }
	    else if (selection == 3) {
	        windowWidth = 1400;
	    }
	    
	    return windowWidth;
	}

	/** gets window height of the game */
	public static int getGameHeight() {
        if (selection == 0) {
            windowHeight = 480;
        } else if (selection == 1) {
            windowHeight = 600;
        } else if (selection == 2) {
            windowHeight = 768;
        } else if (selection == 3) {
            windowHeight = 1000;
        }
        
        return windowHeight;
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
	public void stop(boolean fullyPlayed, boolean mainMenu) {
	    /* if already not running */
	    if (!running) {
	        return;
	    }
	    
	    timer.stop();
	    
	    /* allow buttons to still work even after the game has reached an end point */
        while (fullyPlayed) {
            render();
        }
                
        running = false;
  
	    try {		   
            RunGame.frame.dispose();
            RunGame.frame = new JFrame();

            if (!mainMenu) { /* if Restart selected */
                blurs = 5;
                countdown = 100;
                new RunGame();
            } else { /* else; Main Menu selected */
                launcher = null;
                getLauncherInstance();
            }
	        
            thread.join(); /* stops running game thread */
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
	     
	     /* countdown timer */
         timer = new Timer(1000, new ActionListener() {
             public void actionPerformed(ActionEvent e) {
                 countdown--;                 
             }
         }); /* updates timer every 1000ms or 1 second */
         
         timer.start(); 
	     	     
         /* execute while game is running */
	     while (running) {
	         if (countdown == 0 || blurs == 0) { /* if time runs out or all blurs have been caught */
	             if (countdown == 0) {
	                 playerWon = false;
	             } else {
	                 playerWon = true;
	             }
	             
	             gameOver = true;
	             stop(true, false);
	         }
	         	                  	         
	         /* frames per second counter */
	         long currentTime = System.nanoTime();
	         long passedTime = currentTime - prevTime;
	         prevTime = currentTime;
	         unprocessedSeconds += passedTime / 1000000000.0;
	         requestFocus(); /* automatically selects window when game is started */
	         
	         while (unprocessedSeconds > secondsPerTick) {
	             tick();
	             unprocessedSeconds -= secondsPerTick;
	             ticked = true;
	             tickCount++;
	             
	             /* limits frame rate: sets game update to 60 times per second */
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
             Player.turnRight = true;
         } else if (newX < oldX) { /* if moving left; rotate left */
             Player.turnLeft = true;
         } else if (newX == oldX) { /* if still; stop rotation */
             if (newX > 100 && newX < windowWidth - 100) { /* only stop rotating if mouse is not on edge of window */
                 Player.turnRight = false;
                 Player.turnLeft = false;  
             }
         }     
         
         oldX = newX;
	 }
		 
	 /** render the screen */
	 private void render() {
	     Color standardColor = Color.YELLOW;
	     
	     bs = this.getBufferStrategy();
	     
	     if (bs == null) {
	         createBufferStrategy(3);
	         return;
	     }
	     
	     screen.render(game);
	     
	     for (int i = 0; i < getGameWidth() * getGameHeight(); i++) {
	         pixels[i] = screen.pixels[i];
	     }
	     
	     g = bs.getDrawGraphics();	     
	     g.drawImage(img, 0, 0, getGameWidth(), getGameHeight(), null);	     
	     g.setColor(standardColor);
	     g.setFont(new Font("Verdana", 0, 30));
	     g.drawString(fps + " FPS", 15, 45);
	     
	     if (difficulty == 0) {
	         g.drawString("-", windowWidth - 110, 40);
	         g.drawString("-", windowWidth / 2 - 5, windowHeight - 130);
	     } else {
	         if (countdown < 10) {
	             g.drawString(countdown + "", windowWidth - 110, 40);
	         } else if (countdown < 100) {
	             g.drawString(countdown + "", windowWidth - 120, 40);
	         } else {
	             g.drawString(countdown + "", windowWidth - 130, 40);
	         }
	         
	         if (blurs < 10) {
	             g.drawString(blurs + "", windowWidth / 2 - 5, windowHeight - 130);
	         } else {
	             g.drawString(blurs + "", windowWidth / 2 - 15, windowHeight - 130);
	         }
	     }
	     
	     g.setFont(new Font("Verdana", 0, 15));
	     g.drawString("Seconds Remaining", windowWidth - 175, 60);	     
         g.drawString("Blur's Left to Catch", windowWidth / 2 - 70, windowHeight - 100);                  
         g.setFont(new Font("Verdana", 0, 10));
         
         if (difficulty == 0) { /* sandbox difficulty */
             g.drawString("Difficulty: Sandbox", windowWidth / 2 - 50, windowHeight - 75);
         } else if (difficulty == 1) { /* easiest difficulty */
             g.drawString("Difficulty: Childs Play", windowWidth / 2 - 55, windowHeight - 75);
         } else if (difficulty == 2) { /* second easiest difficulty */
             g.drawString("Difficulty: Average Joe", windowWidth / 2 - 60, windowHeight - 75);
         } else { /* hardest difficulty */
             g.drawString("Difficulty: God Mode", windowWidth / 2 - 55, windowHeight - 75);
         }
         
         renderButtons(standardColor);	     
         
         if (gameOver) {
             winnerLoser(standardColor);
         }
         
         bs.show();
    }
	 
	 /** creates the Quit and Restart buttons while in game */
	 private void renderButtons(Color standardColor) {   
	     Color hoveredColor = new Color(255, 155, 0);
	     
	     /* in-game quit button */
	     g.setColor(standardColor);
         g.setFont(new Font("Verdana", 0, 20));
	     g.drawString("Quit", 15, windowHeight - 50);
	     
	     if (InputHandler.mouseX > 10 && InputHandler.mouseX < 60
	             && InputHandler.mouseY > windowHeight - 90 && InputHandler.mouseY < windowHeight) {
	         g.setColor(hoveredColor);
	         g.drawString("Quit", 15, windowHeight - 50);
	         
	         if (InputHandler.mouseButton == 1) { /* clicking on the quit button */
	             System.exit(0);
	         }
	     }
	     	     
	     /* in-game Restart button */
	     g.setColor(standardColor);
	     g.drawString("Restart", 85, windowHeight - 50);
	     
	     if (InputHandler.mouseX > 80 && InputHandler.mouseX < 190
                 && InputHandler.mouseY > windowHeight - 90 && InputHandler.mouseY < windowHeight) {
             g.setColor(hoveredColor);
             g.drawString("Restart", 85, windowHeight - 50);
             
             if (InputHandler.mouseButton == 1) { /* clicking on the Restart button */
                 InputHandler.mouseButton = 0;
                 stop(false, false);              
             }
         }
	     
	     /* in-game Main Menu button */
	     g.setColor(standardColor);
         g.drawString("Main Menu", windowWidth - 140, windowHeight - 50);
         
         if (InputHandler.mouseX > windowWidth - 150 && InputHandler.mouseX < windowWidth
                 && InputHandler.mouseY > windowHeight - 90 && InputHandler.mouseY < windowHeight) {
             g.setColor(hoveredColor);
             g.drawString("Main Menu", windowWidth - 140, windowHeight - 50);
             
             if (InputHandler.mouseButton == 1) { /* clicking on the Main Menu button */ 
                 stop(false, true);
             }
         }
	 }
	 
	 /** winner/loser notification */
     private void winnerLoser(Color standardColor) {
        g.setFont(new Font("Comic Sans MS", 0, 50));
        g.setColor(standardColor);

        if (!playerWon) { /* if player loses the game */
            g.drawString("You're out of time!", windowWidth / 2 - 225, windowHeight / 2);
        } else { /* else player wins game */
            g.drawString("You Escaped!", windowWidth / 2 - 150, windowHeight / 2);
        }
     }
     
    /** main method */
    public static void main(String args[]) {
        getLauncherInstance();
    }
}