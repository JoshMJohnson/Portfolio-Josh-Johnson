package levels;

import graphics.Blur;
import java.util.ArrayList;
import java.util.List;

/** class for a pixel; section of in the game */
public class Block {
    public boolean solid = false;
    public static Block solidWall = new SolidBlock();
    public List<Blur> blurs = new ArrayList<Blur>();
    
    /** adds a blur to the list of blurs */
    public void addBlur(Blur blur) {
        blurs.add(blur);
    }
}