package main;

import input.Player;
import java.awt.event.KeyEvent;
import levels.Level;

/** overall game manager */
public class Game {
    public int time;
    public Player player;
    public Level level;
    
    /** constructor for the Game class */
    public Game() {
        player = new Player(0, 0, 0); /* player starting location */
        level = new Level(100, 100); /* arena dimensions */
    }
    
    /** game progression */
    public void tick(boolean[] key) {
        time++;
        
        /* user input */
        boolean forward = key[KeyEvent.VK_W];
        boolean backward = key[KeyEvent.VK_S];
        boolean left = key[KeyEvent.VK_A];
        boolean right = key[KeyEvent.VK_D];
        boolean jump = key[KeyEvent.VK_SPACE];
        boolean crouch = key[KeyEvent.VK_CONTROL];
        boolean run = key[KeyEvent.VK_SHIFT];
        
        player.tick(forward, backward, left, right, jump, crouch, run);
    }
}