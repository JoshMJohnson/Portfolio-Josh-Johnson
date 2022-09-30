import graphics.Render;
import graphics.Screen;
import javax.swing.JFrame;
import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;

/** Created By: Josh Johnson
  * Description: 3-Dimensional game
  */
public class Display extends Canvas implements Runnable {
    /* window settings */
	private final static int WIDTH = 1700;
	private final static int HEIGHT  = 850;
	private final static String TITLE = "Balls Collector Game";
	
	/* game settings */
	private Thread thread;
	private BufferedImage img;
	private boolean running = false;
    private int[] pixels;

	/* other java classes */
	private Render render;
	private Screen screen;
		
	/** constructor for Display class */
	public Display() {
	    screen = new Screen(WIDTH, HEIGHT);
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
		frame.setSize(WIDTH, HEIGHT);
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
	     while (running) {
	         tick();
	         render();
         }
     }
	 
	 /***/
	 private void tick() {
	     
	 }
	 
	 /** render the screen */
	 private void render() {
	     BufferStrategy bs = this.getBufferStrategy();
	     
	     if (bs == null) {
	         createBufferStrategy(3);
	         return;
	     }
	     
	     screen.render();
	     
	     for (int i = 0; i < WIDTH * HEIGHT; i++) {
	         pixels[i] = screen.pixels[i];
	     }
	     
	     Graphics g = bs.getDrawGraphics();
	     g.drawImage(img, 0, 0, WIDTH, HEIGHT, null);
	     g.dispose();
	     bs.show();
	 }
}