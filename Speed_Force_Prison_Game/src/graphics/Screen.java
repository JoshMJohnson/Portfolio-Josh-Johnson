package graphics;

import main.Game;

/** keeps track of pixels on the screen */
public class Screen extends Render {
    /* class objects */
    private Render3D render;
    
    /** constructor for Screen class */
    public Screen(int width, int height) {
        super(width, height);
        render = new Render3D(width, height);
    }

    /** renders pixels */
    public void render(Game game) {
        /* refreshes the pixels where the rendering is no longer happening;
         * gets rid of trail */
        for (int i = 0; i < width * height; i++) {
            pixels[i] = 0;
        }
                
        render.arena(game);
        render.renderDistanceLimiter();        
        draw(render, 0, 0);
    }
}