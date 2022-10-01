package graphics;

import main.Game;

public class Render3D extends Render {
    /** constructor for the Render3D class*/
    public Render3D(int width, int height) {
        super(width, height);
    }
        
    /** renders the floor and ceiling */
    public void floor(Game game) {
        /* floor and ceiling distances away */
        double floorPosition = 8;
        double ceilingPosition = 50;
        
        /* rotations */
        double rotation = 0;
        double cosine = Math.cos(rotation);
        double sine = Math.sin(rotation);
        
        /* movement */
        double forward = game.time / 2.0;
        double right = 0;
        
        for (int y = 0; y < height; y++) {
            double ceiling = (double) (y - height / 2) / height;   
            double z = floorPosition / ceiling;

            if (ceiling < 0) {
                z = ceilingPosition / -ceiling;
            }
                        
            for (int x = 0; x < width; x++) {
                double depth = (double) (x - width / 2) / height;
                depth *= z;
                double xx = depth * cosine + z * sine - right;
                double yy = z * cosine - depth * sine + forward;
                int xPix = (int) xx;
                int yPix = (int) yy;
                pixels[x + y * width] = ((xPix & 15) * 16) | ((yPix & 15) * 16) << 8;
            }
        }
    }
}