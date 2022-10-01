package graphics;

import java.util.Random;
import main.Game;

/** keeps track of pixels on the screen */
public class Screen extends Render {
    private Render test;
    private Render3D render;
    
    /** constructor for Screen class 
      * @param width
      * @param height */
    public Screen(int width, int height) {
        super(width, height);
        
        Random random = new Random();
        render = new Render3D(width, height);
        test = new Render(250, 250);
        
        for (int i = 0; i < 250 * 250; i++) {
            test.pixels[i] = random.nextInt() * (random.nextInt(5) / 4);
        }
    }

    /** renders the pixels */
    public void render(Game game) {
        /* refreshes the pixels where the rendering is no longer happening;
         * gets rid of trail */
        for (int i = 0; i < width * height; i++) {
            pixels[i] = 0;
        }
        
        /* for loop adds a trail behind animated object;
         * to keep animation, but remove trail - keep contents but remove loop */
        for (int i = 0; i < 50; i++) {
            int animation = (int) (Math.sin((game.time + i * 2) % 1000.0 / 100) * 100);
        }
        
        render.floor();
        draw(render, 0, 0);
    }
}
