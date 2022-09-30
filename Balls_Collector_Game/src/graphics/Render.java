package graphics;

/** renders the pixels in the game */
public class Render {
    public final int width;
    public final int height;
    public final int[] pixels;
    
    /** constructor for Render class 
      * @param width: number of pixels to render along x-axis
      * @param height: number of pixels to render along y-axis
      */
    public Render(int width, int height) {
        this.width = width;
        this.height = height;
        pixels = new int[width * height];
    }
    
    /** colors pixels 
      * @param render
      * @param xOffset: x offset value - origin is top left corner of window below title
      * @param yOffset: y offset value - origin is top left corner of window below title
      */
    public void draw(Render render, int xOffset, int yOffset) {        
        for (int y = 0; y < render.height; y++) {
            int yPixels = y + yOffset;
            
            /* if pixel is off screen vertically */
            if (yPixels < 0 || yPixels >= 850) {
                continue;
            }
            
            for (int x = 0; x < render.width; x++) {
                int xPixels = x + xOffset;
                
                /* if pixel is off screen horizontally */
                if (xPixels < 0 || xPixels >= 1700) {
                    continue;
                }
                
                pixels[xPixels + yPixels * width] = render.pixels[x + y * render.width];
            }
        }
    }
}
