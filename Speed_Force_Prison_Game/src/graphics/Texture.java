package graphics;

import java.awt.image.BufferedImage;

import javax.imageio.ImageIO;

/** deals with textures such as images for parts of the game */
public class Texture {
    public static Render floor = loadBitmap("/textures/temp.png");
    public static Render wall = loadBitmap("/textures/wall.png");
    
    /** locates and loads textures */
    public static Render loadBitmap(String fileName) {
        try {
            BufferedImage image = ImageIO.read(Texture.class.getResource(fileName));
            int width = image.getWidth();
            int height = image.getHeight();
            Render result = new Render(width, height);
            image.getRGB(0, 0, width, height, result.pixels, 0, width);
            return result;            
        } catch (Exception e) {
            System.err.println("Crash");
            throw new RuntimeException(e); /* crash game */
        }
    }
}