package main;

import input.Controller;

import java.awt.event.KeyEvent;

import levels.Level;

/** overall game manager */
public class Game {
    public int time;
    public Controller controls;
    public Level level;
    
    /** constructor for the Game class */
    public Game() {
        controls = new Controller();
        level = new Level(30, 30);
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
        
        controls.tick(forward, backward, left, right, jump, crouch, run);
    }
}