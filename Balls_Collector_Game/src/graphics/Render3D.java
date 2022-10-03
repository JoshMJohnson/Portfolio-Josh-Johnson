package graphics;

import input.Controller;
import main.Game;

/** handles the pixel motion effects */
public class Render3D extends Render {
    public double[] zBuffer;
    private double renderDistance = 5000;
    
    /** constructor for the Render3D class */
    public Render3D(int width, int height) {
        super(width, height);
        zBuffer = new double[width * height];
    }
        
    /** renders the floor and ceiling */
    public void floor(Game game) {
        /* floor and ceiling distances away from center */
        double floorPosition = 8;
        double ceilingPosition = 40;
        
        /* rotations */
        double rotation = game.controls.rotation;
        double cosine = Math.cos(rotation);
        double sine = Math.sin(rotation);
        
        /* movement */
        double forward = game.controls.z;
        double right =  game.controls.x;
        double up = game.controls.y;
        double walking = Math.sin(game.time / 6.0) * 0.4;
        
        /* adjusts head bobbing amounts */
        if (Controller.crouchWalk) {
            walking = Math.sin(game.time / 6.0) * 0.15;
        } else if (Controller.runForward) {
            walking = Math.sin(game.time / 6.0) * 0.8;
        }
        
        /* render effects */
        for (int y = 0; y < height; y++) {
            double ceiling = (double) (y - height / 2) / height;   
            double z = (floorPosition + up) / ceiling;
            
            if (Controller.walk) {
                z = (floorPosition + up + walking) / ceiling;
            }

            /* ensure floor and ceiling are moving in same direction */
            if (ceiling < 0) {
                z = (ceilingPosition - up) / -ceiling;
                
                if (Controller.walk) {
                    z = (ceilingPosition - up - walking) / -ceiling;
                }
            }
                        
            for (int x = 0; x < width; x++) {
                double depth = (double) (x - width / 2) / height;
                depth *= z;
                double xx = depth * cosine + z * sine + right;
                double yy = z * cosine - depth * sine + forward;
                int xPix = (int) (xx + right);
                int yPix = (int) (yy + forward);
                zBuffer[x + y * width] = z;
                pixels[x + y * width] = Texture.floor.pixels[(xPix & 7) + (yPix & 7) * 8];
            }
        }
    }
    
    /** limits the distance away for rendering */
    public void renderDistanceLimiter() {
        for (int i = 0; i < width * height; i++) {
            int color = pixels[i];
            int brightness = (int) (renderDistance / zBuffer[i]);
            
            /* minimum brightness value */
            if (brightness < 0) {
                brightness = 0;
            }
            
            /* maximum brightness value */
            if (brightness > 255) {
                brightness = 255;
            }
            
            int r = (color >> 16) & 0xff;
            int g = (color >> 8) & 0xff;
            int b = (color) & 0xff;
            
            r = r * brightness / 255;
            g = g * brightness / 255;
            b = b * brightness / 255;
            
            pixels[i] = r << 16 | g << 8 | b;
        }
    }
}