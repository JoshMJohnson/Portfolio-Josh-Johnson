package graphics;

import java.util.Random;
import main.Game;

/** keeps track of pixels on the screen */
public class Screen extends Render {
    /* class objects */
    private Render test;
    private Render3D render;
    
    /** constructor for Screen class */
    public Screen(int width, int height) {
        super(width, height);
        
        Random random = new Random();
        render = new Render3D(width, height);
        test = new Render(250, 250);
        
        for (int i = 0; i < 250 * 250; i++) {
            test.pixels[i] = random.nextInt() * (random.nextInt(5) / 4);
        }
    }

    /** renders pixels */
    public void render(Game game) {
        /* refreshes the pixels where the rendering is no longer happening;
         * gets rid of trail */
        for (int i = 0; i < width * height; i++) {
            pixels[i] = 0;
        }
                
        render.floor(game);
//        render.renderWall(0, 0.5, 2.5, 2.5, 0);
//        render.renderWall(0, 0, 2, 2.5, 0);
//        render.renderWall(0, 0.5, 2, 2, 0);
//        render.renderWall(0.5, 0.5, 2, 2.5, 0);
        render.renderDistanceLimiter();
        
        draw(render, 0, 0);
    }
}