package graphics;

/** renders the pixels in the game */
public class Render {
    public final int width;
    public final int height;
    public final int[] pixels;
    
    /** constructor for Render class */
    public Render(int width, int height) {
        this.width = width;
        this.height = height;
        pixels = new int[width * height];
    }
    
    /** renders pixels */
    public void draw(Render render, int xOffset, int yOffset) {        
        for (int y = 0; y < render.height; y++) {
            int yPixels = y + yOffset;
            
            /* if pixel is off screen vertically */
            if (yPixels < 0 || yPixels >= height) {
                continue;
            }
            
            for (int x = 0; x < render.width; x++) {
                int xPixels = x + xOffset;
                
                /* if pixel is off screen horizontally */
                if (xPixels < 0 || xPixels >= width) {
                    continue;
                }
                
                /* alpha support */
                int alpha = render.pixels[x + y * render.width];
                
                /* if pixels need to be rendered */
                if (alpha > 0) {
                    pixels[xPixels + yPixels * width] = alpha;
                }
            }
        }
    }
}