package graphics;

public class Render3D extends Render {
    /** constructor for the Render3D class*/
    public Render3D(int width, int height) {
        super(width, height);
    }
    
    double time = 0;
    
    /** renders the floor and ceiling */
    public void floor() {
        for (int y = 0; y < height; y++) {
            double ceiling = (double) (y - height / 2) / height;            
            double z = 8 / ceiling;
            time += 0.0001;
            
            for (int x = 0; x < width; x++) {
                double depth = (double) (x - width / 2) / height;
                depth *= z;
                int xx = (int) (depth) & 15;
                int yy = (int) (z + time) & 15;
                pixels[x + y * width] = (xx * 16) | (yy * 16) << 8;
            }
        }
    }
}