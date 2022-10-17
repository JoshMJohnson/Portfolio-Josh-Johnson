package main;

import gui.Launcher;
import java.awt.Cursor;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JFrame;

/** begins the game when told to start from the launcher/start-up window  */
public class RunGame {   
    /** constructor for the Launcher class */
    public RunGame() {
        Toolkit toolkit = null;
        Image cursorImage = null;
        
        try {
            toolkit = Toolkit.getDefaultToolkit();
            cursorImage = ImageIO.read(Launcher.class.getResource("/textures/launcher_arrow.png"));
        } catch(IOException e) {
            e.printStackTrace();
        }
        
        Cursor cursorIcon = toolkit.createCustomCursor(cursorImage, new Point(0,0), "img");        
        JFrame frame = new JFrame();
        Display game = new Display();

        /* setup game window */
        frame.add(game);
        frame.setSize(Display.getGameWidth(), Display.getGameHeight());
        frame.getContentPane().setCursor(cursorIcon); // hides the cursor on the game
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