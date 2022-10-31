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
    public static int mouseDragX;
    public static int mouseDragY;
    public static int mousePressedX;
    public static int mousePressedY;
    public static int mouseButton;
    public static boolean dragged = false;
    
    /** handles action when mouse is clicked */
    public void mouseClicked(MouseEvent e) {}

    /** handles action when mouse enters a component */
    public void mouseEntered(MouseEvent e) {}

    /** handles action when mouse leaves a component */
    public void mouseExited(MouseEvent e) {}

    /** handles action when mouse is pressed */
    public void mousePressed(MouseEvent e) {
        mouseButton = e.getButton();
        mousePressedX = e.getX();
        mousePressedY = e.getY();     
    }

    /** handles action when mouse is released */
    public void mouseReleased(MouseEvent e) {
        dragged = false;
        mouseButton = 0;
    }    

    /** handles action when mouse is dragged */
    public void mouseDragged(MouseEvent e) {
        dragged = true;
        mouseDragX = e.getX();
        mouseDragY = e.getY();
    }

    /** handles action when mouse moves on screen */
    public void mouseMoved(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
    }

    /** handles action when window gains selected window status */
    public void focusGained(FocusEvent e) {}

    /** handles action when window is taking in a command but loses 
      * selected window status before action is completed */
    public void focusLost(FocusEvent e) {
        for (int i = 0; i < key.length; i++) {
            key[i] = false;
        }
    }

    /** handles action when a key is pressed */
    public void keyPressed(KeyEvent e) {
        int keyCode = e.getKeyCode();
        
        if (keyCode > 0 && keyCode < key.length) {
            key[keyCode] = true;
        }
    }

    /** handles action when a key is released */
    public void keyReleased(KeyEvent e) {
        int keyCode = e.getKeyCode();
        
        if (keyCode > 0 && keyCode < key.length) {
            key[keyCode] = false;
        }
    }

    /** handles action when a key is typed */
    public void keyTyped(KeyEvent e) {}
}