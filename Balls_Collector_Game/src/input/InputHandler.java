package input;

import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

/** handles change in the program indicated by events created by user input */
public class InputHandler implements KeyListener, FocusListener, MouseListener, MouseMotionListener {
    public boolean[] key = new boolean[68836]; /* size is determined by number of possible key inputs */
    public static int mouseX;
    public static int mouseY;
    
    @Override
    /** handles action when mouse is clicked */
    public void mouseClicked(MouseEvent e) {
        
    }

    @Override
    /** handles action when mouse enters a component */
    public void mouseEntered(MouseEvent e) {
        
    }

    @Override
    /** handles action when mouse leaves a component */
    public void mouseExited(MouseEvent e) {
        
    }

    @Override
    /** handles action when mouse is pressed */
    public void mousePressed(MouseEvent e) {
        
    }

    @Override
    /** handles action when mouse is released */
    public void mouseReleased(MouseEvent e) {
        
    }    

    @Override
    /** handles action when mouse is dragged */
    public void mouseDragged(MouseEvent e) {
        
    }

    @Override
    /** handles action when mouse moves on screen */
    public void mouseMoved(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
    }

    @Override
    /** handles action when window gains selected window status */
    public void focusGained(FocusEvent e) {
        
    }

    @Override
    /** handles action when window is taking in a command but loses 
      * selected window status before action is completed */
    public void focusLost(FocusEvent e) {
        for (int i = 0; i < key.length; i++) {
            key[i] = false;
        }
    }

    @Override
    /** handles action when a key is pressed */
    public void keyPressed(KeyEvent e) {
        int keyCode = e.getKeyCode();
        
        if (keyCode > 0 && keyCode < key.length) {
            key[keyCode] = true;
        }
    }

    @Override
    /** handles action when a key is released */
    public void keyReleased(KeyEvent e) {
        int keyCode = e.getKeyCode();
        
        if (keyCode > 0 && keyCode < key.length) {
            key[keyCode] = false;
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {
        
    }
}