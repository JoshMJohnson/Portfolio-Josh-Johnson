package graphics;

import java.util.Random;

/** keeps track of pixels on the screen */
public class Screen extends Render {
    private Render test;
    
    /** constructor for Screen class 
      * @param width
      * @param height */
    public Screen(int width, int height) {
        super(width, height);
        
        Random random = new Random();
        test = new Render(250, 250);
        
        for (int i = 0; i < 250 * 250; i++) {
            test.pixels[i] = random.nextInt();
        }
    }

    /** renders the pixels */
    public void render() {
        /* refreshes the pixels where the rendering is no longer happening;
         * gets rid of trail */
        for (int i = 0; i < width * height; i++) {
            pixels[i] = 0;
        }
        
        /* for loop adds a trail behind animated object;
         * to keep animation, but remove trail - keep contents but remove loop */
        for (int i = 0; i < 50; i++) {
            int animation = (int) (Math.sin((System.currentTimeMillis() + i * 8) % 1000.0 / 1000 * Math.PI * .15) * 500);
            draw(test, 100, 100 + animation);
        }
    }
}
