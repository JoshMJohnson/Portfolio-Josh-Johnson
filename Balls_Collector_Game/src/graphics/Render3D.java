package graphics;

import java.util.Random;
import input.Controller;
import main.Game;

/** handles the pixel motion effects */
public class Render3D extends Render {
    public double[] zBuffer;
    private double renderDistance = 5000;
    private double forwardMovement, rightMovement, cosine, sine, up, walking;
    
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
        cosine = Math.cos(rotation);
        sine = Math.sin(rotation);
        
        /* movement */
        forwardMovement = game.controls.z;
        rightMovement =  game.controls.x;
        up = game.controls.y;
        walking = 0;
                       
        /* render effects */
        for (int y = 0; y < height; y++) {
            double ceiling = (double) (y - height / 2) / height;   
            double z = (floorPosition + up) / ceiling;
            
            if (Controller.walk) {
                walking = Math.sin(game.time / 6.0) * 0.4;
                z = (floorPosition + up + walking) / ceiling;
            }
            
            /* adjusts head bobbing amounts */
            if (Controller.crouchWalk && Controller.walk) {
                walking = Math.sin(game.time / 6.0) * 0.15;
                z = (floorPosition + up + walking) / ceiling;
            } else if (Controller.runForward && Controller.walk) {
                walking = Math.sin(game.time / 6.0) * 0.8;
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
                double xx = depth * cosine + z * sine + rightMovement;
                double yy = z * cosine - depth * sine + forwardMovement;
                int xPix = (int) (xx + rightMovement);
                int yPix = (int) (yy + forwardMovement);
                zBuffer[x + y * width] = z;
                pixels[x + y * width] = Texture.floor.pixels[(xPix & 7) + (yPix & 7) * 8];
            }
        }
    }
    
    /** render the walls */
    public void renderWall(double xLeft, double xRight, double zDistanceLeft, double zDistanceRight, double yHeight) {
        /* has wall move with users head bobbing while moving */
        double upCorrect = 0.062;
        double rightCorrect = 0.062;
        double forwardCorrect = 0.062;
        double walkCorrect = -0.062;
        
        /* left side of the wall */
        double xCalculateLeft = (xLeft - (rightMovement * rightCorrect)) * 2;
        double zCalculateLeft = (zDistanceLeft - (forwardMovement * forwardCorrect)) * 2;
        double rotationLeftSideX = xCalculateLeft * cosine - zCalculateLeft * sine;
        double yCornerTopLeft = (-yHeight - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double yCornerBottomLeft = ((+0.5 - yHeight) - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double rotationLeftSideZ = zCalculateLeft * cosine + xCalculateLeft * sine;
        
        /* right side of the wall */
        double xCalculateRight = (xRight - (rightMovement * rightCorrect)) * 2;
        double zCalculateRight = (zDistanceRight - (forwardMovement * forwardCorrect)) * 2;
        double rotationRightSideX = xCalculateRight * cosine - zCalculateRight * sine;
        double yCornerTopRight = (-yHeight - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double yCornerBottomRight = ((+0.5 - yHeight) - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double rotationRightSideZ = zCalculateRight * cosine + xCalculateRight * sine;
        
        /* pixel locations for walls */
        double xPixelLeft = (rotationLeftSideX / rotationLeftSideZ * height + width / 2);
        double xPixelRight = (rotationRightSideX / rotationRightSideZ * height + width / 2);

        /* skip rendering negative pixels */
        if (xPixelLeft >= xPixelRight) {
            return;
        }
        
        int xPixelLeftInt = (int) xPixelLeft;
        int xPixelRightInt = (int) xPixelRight;
        
        /* skip rendering pixels off screen */
        if (xPixelLeftInt < 0) {
            xPixelLeftInt = 0;
        } else if (xPixelRightInt > width) {
            xPixelRightInt = width;
        }
        
        /* four corner pins */
        double yPixelLeftTop = yCornerTopLeft / rotationLeftSideZ * height + height / 2.0;
        double yPixelLeftBottom = yCornerBottomLeft / rotationLeftSideZ * height + height / 2.0;
        double yPixelRightTop = yCornerTopRight / rotationRightSideZ * height + height / 2.0;
        double yPixelRightBottom = yCornerBottomRight / rotationRightSideZ * height + height / 2.0;

        /* texture preparation */
        double texture1 = 1 / rotationLeftSideZ;
        double texture2 = 1 / rotationRightSideZ;
        double texture3 = 0 / rotationLeftSideZ;
        double texture4 = 8 / rotationRightSideZ - texture3;
        
        /* render walls */
        for (int x = xPixelLeftInt; x < xPixelRightInt; x++) {
            double pixelRotation = (x - xPixelLeft) / (xPixelRight - xPixelLeft);          
            
            int xTexture = (int) ((texture3 + texture4 * pixelRotation) / (texture1 + (texture2 - texture1) * pixelRotation));
            
            double yPixelTop = yPixelLeftTop + (yPixelRightTop - yPixelLeftTop) * pixelRotation;          
            double yPixelBottom = yPixelLeftBottom + (yPixelRightBottom - yPixelLeftBottom) * pixelRotation;
            
            int yPixelTopInt = (int) yPixelTop;
            int yPixelBottomInt = (int) yPixelBottom;
            
            /* skip rendering pixels off screen */
            if (yPixelTopInt < 0) {
                yPixelTopInt = 0;
            } else if (yPixelBottomInt > height) {
                yPixelBottomInt = height;
            }
            
            for (int y = yPixelTopInt; y < yPixelBottomInt; y++) {
                double pixelRotationY = (y - yPixelTop) / (yPixelBottom - yPixelTop);
                int yTexture = (int) (8 * pixelRotationY);
                
                pixels[x + y * width] = xTexture * 100 + yTexture * 100;           
                zBuffer[x + y * width] = 1 / (texture1 + (texture2 - texture1) * pixelRotation) * 2; //handles render distance limiting
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