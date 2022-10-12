package main;

import java.awt.Cursor;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;

/** begins the game when told to start from the launcher/start-up window  */
public class RunGame {   
    /** constructor for the Launcher class */
    public RunGame() {
        BufferedImage cursor = new BufferedImage(16, 16, BufferedImage.TYPE_INT_ARGB);
        Cursor blank = Toolkit.getDefaultToolkit().createCustomCursor(cursor, new Point(0,0), "blank");
        JFrame frame = new JFrame();
        Display game = new Display();

        /* setup game window */
        frame.add(game);
        frame.setSize(Display.getGameWidth(), Display.getGameHeight());
        frame.getContentPane().setCursor(blank); // hides the cursor on the game
        frame.setTitle(Display.TITLE);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null); // center window on screen
        frame.setResizable(false);
        frame.setVisible(true);

        /* begin the game */
        game.start();
        stopMenuThread();                
    }
    
    /** stops the launcher menu from running */
    private void stopMenuThread() {
        Display.getLauncherInstance().stopMenu();
    }
}