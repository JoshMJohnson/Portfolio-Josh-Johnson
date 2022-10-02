package graphics;

import main.Game;

/** handles the pixel motion effects */
public class Render3D extends Render {
    /** constructor for the Render3D class */
    public Render3D(int width, int height) {
        super(width, height);
    }
        
    /** renders the floor and ceiling */
    public void floor(Game game) {
        /* floor and ceiling distances away from center */
        double floorPosition = 8;
        double ceilingPosition = 50;
        
        /* rotations */
        double rotation = game.controls.rotation;
        double cosine = Math.cos(rotation);
        double sine = Math.sin(rotation);
        
        /* movement */
        double forward = game.controls.z;
        double right =  game.controls.x;
        
        /* render effects */
        for (int y = 0; y < height; y++) {
            double ceiling = (double) (y - height / 2) / height;   
            double z = floorPosition / ceiling;

            /* ensure floor and ceiling are moving in same direction */
            if (ceiling < 0) {
                z = ceilingPosition / -ceiling;
            }
                        
            for (int x = 0; x < width; x++) {
                double depth = (double) (x - width / 2) / height;
                depth *= z;
                double xx = depth * cosine + z * sine + right;
                double yy = z * cosine - depth * sine + forward;
                int xPix = (int) (xx + right);
                int yPix = (int) (yy + forward);
                pixels[x + y * width] = ((xPix & 15) * 16) | ((yPix & 15) * 16) << 8;
            }
        }
    }
}